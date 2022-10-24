from flask import render_template, redirect, request, session 
from flask_app import app

from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja
# from flask_app.config.helper import findBool IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST


# @app.route('/dojo/new')
# def dojo_new():
#     return render_template('dojo_new.html')
@app.route('/dojo')
def show_all():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template('index.html', all_dojos=all_dojos)
#     # Action route
@app.route('/dojo/create' , methods=['POST'])
def dojo_create():
    data = {
        **request.form
    }
    Dojo.create_dojo(data)
    return redirect(f'/dojo')
@app.route('/dojo/<int:id>')
def dojo_show(id):
    data = {
        'id':id
    }
    dojo = Dojo.get_one(data)
    dojo_ninjas = Ninja.get_all_ninja_in_dojo(data)
    print(dojo_ninjas)
    return render_template('show.html', dojo = dojo, dojo_ninjas = dojo_ninjas)
@app.route('/dojo/<int:id>/edit')
def dojo_edit(id):
    dojo = Dojo.get_one({'id':id})
    
    return render_template('dojo_edit.html', dojo=dojo)
@app.route('/dojo/<int:id>/update', methods = ['POST'])
def update_one(id):
    data = {
        **request.form,
        'id':id
    }
    Dojo.update_one(data)
    
    return redirect(f'/dojo/{id}')

@app.route('/dojo/<int:id>/delete')
def dojo_delete(id):
    Dojo.delete_one({'id': id})

    return redirect('/dojo')

# @app.route('/dojo/<int:id>')
# def dojo_show(id):

#     return render_template('burger_show.html')
# @app.route('/dojo/<int:id>/update', methods=['POST'])
# def dojo_update(id):
#     data = {
#         **request.form
#         'id':id
#     }
#     # data = findBool(data, 'Boolean Key Name') IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST

#     Survey.update_one(data)
#     return redirect('/')

