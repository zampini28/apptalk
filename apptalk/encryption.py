import bcrypt, base64, hashlib

def hashpw(user, pw):
    return bcrypt.hashpw(
        base64.b64encode(hashlib.sha256((user + pw).encode('utf-8')).digest()),
        bcrypt.gensalt(14))

def checkpw(hash_pw, user, pw):
    return bcrypt.checkpw(
        base64.b64encode(hashlib.sha256((user + pw).encode('utf-8')).digest()),
        hash_pw)


