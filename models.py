from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.string(80), unique=True, nullable=False)
    email = db.Column(db.string(120), unique=True, nullable=False)
    password_hash = db.Column(db.string(200), nullable=False)
    created_at = db.Column(db.datetime, default=datetime.utcnow)


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.integer, primary_key=True)
    tmdb_id = db.Column(db.string(50), unique=True, nullable=False)
    title = db.Column(db.string(200), nullable=False)
    overview = db.Column(db.text)
    poster = db.Column(db.string(300))
    release_date = db.Column(db.string(20))


class Song(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.integer, primary_key=True)
    movie_id = db.Column(db.integer, db.foreignkey("movies.id"))
    track_name = db.Column(db.string(200))
    artist_name = db.Column(sb.string(200))
    spotify_url = db.Column(db.string(300))
    movie = db.relationship("Movie", baclref=db.backref("songs", lazy=True))


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.integer, primary_key=True)
    movie_di = db.Column(db.integer, db.foreignkey("movies.id"))
    title = db.Column(db.string(120))
    author = db.Column(db.string(120))
    google_books_url = db.Column(db.dtring(300))
    movie = db.relationship("Movie", backref=db.backref("books", lazy=True))


class Recommendation(db.Model):
    __tablename__ = "recommendations"
    id = db.Column(db.integer, primary_key=True)
    user_id = db.Column(db.integer, db.foreignkey("users.id"))
    recommended_movie_id = db.Column(db.integer, db.foreignkey("movies.id"))
    similarity_score = db.Column(db.float)
    timestamp = db.Column(db.datetime, default=datetime.utcnow)

    user = db.relationship("User", backref=db.backref("recommendations", lazy=True))
