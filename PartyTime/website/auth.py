from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('id')
        pw = request.form.get('pw')
        
        user = User.query.filter_by(id=id).first()
        if user:
            if check_password_hash(user.pw, pw):
                flash('Loggato!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Password errata, prova ancora!', category='error')
        else:
            flash('Utente non esiste, riprova o registrati!', category='error')
            
            
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET','POST'])
def signup():
    
    if request.method == 'POST':
        
        #fetch data
        userDetails = request.form
        
        id = userDetails['id']
        pw1 = userDetails['pw1']
        pw2 = userDetails['pw2']
        nome = userDetails['nome']
        cogn = userDetails['cogn']
        cell = userDetails['cell']
        mail = userDetails['mail']
        
        #controlli sull input
        user = User.query.filter_by(id=id).first()
        
        if user:
            flash("UserId gia' esistente", category='error')
        elif len(id) <= 4:
            flash('UserId non valido (almeno 4 caratteri)', category='error')
        elif len(pw1) <=7:
            flash('Password non valida (almeno 7 caratteri)', category='error')
        elif pw1 != pw2:
            flash('Password non coincidono', category='error')
        elif len(nome) <= 3:
            flash('Nome non valido (almeno 3 caratteri)', category='error')
        elif len(cogn) <= 3:
            flash('Cognome non valido (almeno 3 caratteri)', category='error')
        elif len(cell) != 10:
            flash('Numero di cellulare non valido', category='error')
        elif len(mail) <= 4:
            flash('Email non valida (almeno 4 caratteri)', category='error')
        else:
            #add user
            new_user = User(id=id, pw=generate_password_hash(pw1, method='sha256'), nome=nome, cogn=cogn, cell=cell, mail=mail)
            db.session.add(new_user)
            db.session.commit()
            flash('Registrato!', category='succes')
            login_user(new_user, remember=True)
            return redirect(url_for('views.index'))
    
    return render_template('signup.html', user=current_user)