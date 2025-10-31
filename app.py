# ==============================
# app.py（Recomuse メインアプリ）
# ==============================

from flask import Flask, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import timedelta

# ------------------------------
# Flaskアプリ設定
# ------------------------------
app = Flask(__name__)

# config読み込み
app.config.from_pyfile("config.py")

# セッション暗号化キー
app.secret_key = "supersecretkey"

# セッション有効時間
app.permanent_session_lifetime = timedelta(minutes=30)

# ------------------------------
# ライブラリ初期化
# ------------------------------
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# ------------------------------
# モデル（データ構造）読み込み
# ------------------------------
from models import User, Movie, Song, Book

# ------------------------------
# ルート（URLごとの処理）
# ------------------------------


# ホーム画面
@app.route("/")
def home():
    return render_template("index.html")


# ユーザー登録
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
