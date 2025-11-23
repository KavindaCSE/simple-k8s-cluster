from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    config_value = os.environ.get("APP_CONFIG", "no-config")
    secret_value = os.environ.get("APP_SECRET", "no-secret")
    return {
        "message": "Hello from backend!",
        "config": config_value,
        "secret": secret_value
    }

app.run(host="0.0.0.0", port=5000)
