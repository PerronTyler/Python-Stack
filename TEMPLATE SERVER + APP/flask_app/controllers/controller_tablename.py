from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.model_tablename import Tablename

@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])
    
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')



@app.route('/tablename')
@app.route('/tablename/new')
def tablename_new():
@app.route('/tablename/create', methods=['POST'])
def tablename_new(id):
@app.route('/tablename/<int:id>')
@app.route('/tablename/<int:id>/edit')
def tablename_edit(id):
    tablename = Tablename.get_one({'id':id})
@app.route('/tablename/<int:id>/update', methods=['POST'])
def tablename_update(id):
    data = {
        **request.form
        'id':id
    }
    Tablename.update_one(data)
    return redirect('/')
@app.route('/tablename/<int:id>/delete')
def tablename_delete(id):
    Tablename.delete_one({'id': id})
    return redirect('/')

#tablename/new (form to submit)
#tablename/create (use the data from form to add to database)
#tablename/<int:id> show the tablename
#tablename/<int:id>/edit
#tablename/<int:id>/update
#tablename/<int:id>/delete