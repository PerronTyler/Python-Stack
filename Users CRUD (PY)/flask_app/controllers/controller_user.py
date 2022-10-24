from flask import render_template, redirect, request, session 
from flask_app import app

from flask_app.models.model_user import User
# from flask_app.config.helper import findBool IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST


# @app.route('/user/new')
# def user_new():
#     return render_template('user_new.html')
@app.route('/user')
def show_all():
    all_users = User.get_all()
    return render_template('user.html', all_users=all_users)
#     # Action route
@app.route('/user/create' , methods=['POST'])
def user_create():
    data = {
        **request.form
    }
    User.create(data)
    print(data)
    return redirect('/user')
@app.route('/user/<int:id>')
def user_show(id):
    data = {
        'id':id
    }
    user = User.get_one(data)
    return render_template('show.html', user = user)
@app.route('/user/<int:id>/edit')
def user_edit(id):
    user = User.get_one({'id':id})

    return render_template('user_edit.html', user=user)
@app.route('/user/<int:id>/update', methods = ['POST'])
def update_one(id):
    data = {
        **request.form,
        'id':id
    }
    User.update_one(data)
    
    return redirect(f'/user/{id}')

@app.route('/user/<int:id>/delete')
def user_delete(id):
    User.delete_one({'id': id})

    return redirect('/user')

# @app.route('/user/<int:id>')
# def user_show(id):

#     return render_template('burger_show.html')
# @app.route('/user/<int:id>/update', methods=['POST'])
# def user_update(id):
#     data = {
#         **request.form
#         'id':id
#     }
#     # data = findBool(data, 'Boolean Key Name') IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST

#     Survey.update_one(data)
#     return redirect('/')

