from flask import Flask

from database import init_database

app = Flask(__name__)

from routes import *

if __name__ == "__main__":
    init_database()
    app.run(host="0.0.0.0", port=5000, debug=True)
