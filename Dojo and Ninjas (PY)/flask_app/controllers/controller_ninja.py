from flask import render_template, redirect, request, session 
from flask_app import app

from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo
# from flask_app.config.helper import findBool IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST


# @app.route('/ninja/new')
# def ninja_new():
#     return render_template('ninja_new.html')
@app.route('/ninja')
def show_all_ninjas():
    all_dojos = Dojo.get_all()
    return render_template('ninja.html', all_dojos=all_dojos)
#     # Action route
@app.route('/ninja/create' , methods=['POST'])
def ninja_create():
    data = {
        **request.form
    }
    Ninja.create_ninja(data)
    print(data)
    return redirect('/ninja')
@app.route('/ninja/<int:id>')
def ninja_show(id):
    data = {
        'id':id
    }
    ninja = Ninja.get_one_ninja(data)
    return render_template('show.html', ninja = ninja)
@app.route('/ninja/<int:id>/edit')
def ninja_edit(id):
    ninja = Ninja.get_one_ninja({'id':id})

    return render_template('ninja_edit.html', ninja=ninja)
@app.route('/ninja/<int:id>/update', methods = ['POST'])
def update_one_ninja(id):
    data = {
        **request.form,
        'id':id
    }
    Ninja.update_one_ninja(data)
    
    return redirect(f'/ninja/{id}')

@app.route('/ninja/<int:id>/delete')
def ninja_delete(id):
    Ninja.delete_one_ninja({'id': id})

    return redirect('/ninja')

# @app.route('/ninja/<int:id>')
# def ninja_show(id):

#     return render_template('burger_show.html')
# @app.route('/ninja/<int:id>/update', methods=['POST'])
# def ninja_update(id):
#     data = {
#         **request.form
#         'id':id
#     }
#     # data = findBool(data, 'Boolean Key Name') IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST

#     Survey.update_one(data)
#     return redirect('/')

