from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import enum


class User(db.Model, UserMixin):
    id = db.Column(db.String(255), primary_key=True)
    pw = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    cogn = db.Column(db.String(50), nullable=False)
    cell = db.Column(db.String(10), unique=True, nullable=False)
    mail = db.Column(db.String(255), unique=True, nullable=False)
    feste = db.relationship('Party')

class Party(db.Model):
    idfesta = db.Column(db.Integer, primary_key = True)
    nbambini = db.Column(db.Integer, nullable=False)
    via = db.Column(db.String(255), nullable=False)
    civico = db.Column(db.String(255), nullable=False)
    citta = db.Column(db.String(255), nullable=False)
    cap = db.Column(db.String(5), nullable=False)
    dataf = db.Column(db.Date, nullable=False)
    oini = db.Column(db.Time, nullable=False)
    durata = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50))
    qualita = db.Column(db.String(50))
    prezzo = db.Column(db.Float, nullable=False)
    id1 =  db.Column(db.String(255), db.ForeignKey('user.id'), nullable=False)
    
