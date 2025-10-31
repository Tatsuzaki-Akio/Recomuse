from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# ユーザテーブル
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# 推薦映画テーブル
class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.String(50), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    overview = db.Column(db.Text)
    poster = db.Column(db.String(300))
    release_date = db.Column(db.String(20))


# 推薦映画に基づいた楽曲テーブル
class Song(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    track_name = db.Column(db.String(200))
    artist_name = db.Column(db.String(200))
    spotify_url = db.Column(db.String(300))
    movie = db.relationship("Movie", backref=db.backref("songs", lazy=True))


# 推薦映画、楽曲に基づいたテーブル
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    movie_di = db.Column(db.Integer, db.ForeignKey("movies.id"))
    title = db.Column(db.String(120))
    author = db.Column(db.String(120))
    google_books_url = db.Column(db.String(300))
    movie = db.relationship("Movie", backref=db.backref("books", lazy=True))


# ユーザごとの推薦履歴の保存テーブル
class Recommendation(db.Model):
    __tablename__ = "recommendations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    recommended_movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    similarity_score = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref=db.backref("recommendations", lazy=True))
