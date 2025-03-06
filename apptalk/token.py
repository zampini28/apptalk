# Fixed token.py
import jwt
from flask import current_app, request, redirect, url_for
from datetime import datetime, timedelta, timezone
from functools import wraps

def get_secret_keys():
    ACCESS_SECRET_KEY = current_app.config["JWT_SECRET_KEY"]
    REFRESH_SECRET_KEY = current_app.config["JWT_SECRET_KEY"]
    return ACCESS_SECRET_KEY, REFRESH_SECRET_KEY

ALGORITHM = "HS256"

def create_tokens(ID) :
    return create_access_token(ID), create_refresh_token(ID)

def create_access_token(ID):
    ACCESS_SECRET_KEY, _ = get_secret_keys()
    payload = {
        "sub": ID,
        "iat": datetime.utcnow(),
        #"exp": datetime.utcnow() + timedelta(minutes=15)
        "exp": datetime.utcnow() + timedelta(seconds=2)
    }
    return jwt.encode(payload, ACCESS_SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(ID):
    _, REFRESH_SECRET_KEY = get_secret_keys()
    payload = {
        "sub": ID,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, REFRESH_SECRET_KEY, algorithm=ALGORITHM)

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        access_token = request.cookies.get("access_token")
        refresh_token = request.cookies.get("refresh_token")

        if not access_token or not refresh_token:
            return redirect(url_for("main.login"))

        ACCESS_SECRET_KEY, REFRESH_SECRET_KEY = get_secret_keys()

        try:
            access_payload = jwt.decode(access_token, ACCESS_SECRET_KEY,
                                        algorithms=[ALGORITHM])
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            try:
                refresh_payload = jwt.decode(refresh_token, REFRESH_SECRET_KEY,
                                             algorithms=[ALGORITHM])
                user_id = refresh_payload["sub"]

                new_access_token = create_access_token(user_id)

                response = func()

                response.set_cookie("access_token", new_access_token,
                                    secure=True, httponly=True,
                                    samesite='strict')
                return response
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
                return redirect(url_for("main.login"))
        except jwt.InvalidTokenError:
            return redirect(url_for("main.login"))

    return wrapper
