from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt

from flask_app.models.model_user import User
# from flask_app.config.helper import findBool IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST


# @app.route('/user/new')
# def user_new():
#     return render_template('user_new.html')
@app.route('/dashboard')
def dashboard():
    if 'uu_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['uu_id']
    }
    user = User.get_one_id(data)
    return render_template('show.html',user = user)
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
@app.route('/user')
def show_all():
    all_users = User.get_all()
    return render_template('user.html', all_users=all_users)
#     # Action route
@app.route('/user/create' , methods=['POST'])
def user_create():
    is_valid = User.validate_register(request.form)
    
    if not is_valid:
        return redirect('/')

    hash_password = bcrypt.generate_password_hash(request.form['password'])
    print(hash_password)
    data = {
        **request.form,
        'password': hash_password
    }
    User.create(data)
    id = User.create(data)
    session['uu_id'] = id
    return redirect('/dashboard')
@app.route('/user/login', methods=['POST'])
def user_show():
    user = User.get_one(request.form)

    if not user:
        flash('Invalid Email', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid Password', 'login')
        return redirect('/')
    session['uu_id'] = user.id
    return redirect('/dashboard')

