import os, random
from flask import Flask
app = Flask(__name__)

@app.get("/")
def omikuji():
    env = os.getenv("APP_ENV", "local")
    fortunes = ["大吉", "中吉", "小吉", "凶"]
    return f"<h1>[{env}] 今日の運勢: {random.choice(fortunes)}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
