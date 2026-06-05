from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Shirts(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    description=db.Column(db.String(200), nullable=True)
    price=db.Column(db.Integer, nullable=False)
    image=db.Column(db.String(200), nullable=True)
class Print(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    description=db.Column(db.String(200), nullable=True)
    price=db.Column(db.Integer, nullable=False)
    image=db.Column(db.String(200), nullable=True)
class Other(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    description=db.Column(db.String(200), nullable=True)
    price=db.Column(db.Integer, nullable=False)
    image=db.Column(db.String(200), nullable=True)


