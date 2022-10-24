from flask import render_template, redirect, request, session 
from flask_app import app

from flask_app.models.model_survey import Survey
# from flask_app.config.helper import findBool IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST


# @app.route('/survey/new')
# def survey_new():
#     return render_template('survey_new.html')
@app.route('/result')
def show():
    
    return render_template('result.html')
#     # Action route
@app.route('/submit' , methods=['POST'])
def survey_create():
    session['data'] = {
        **request.form
    }

    return redirect('/result')



# @app.route('/survey/<int:id>')
# def survey_show(id):

#     return render_template('burger_show.html')

# @app.route('/survey/<int:id>/edit')
# def survey_edit(id):
#     survey = Survey.get_one({'id':id})

#     return render_template('survey_edit.html', survey=survey)

# @app.route('/survey/<int:id>/update', methods=['POST'])
# def survey_update(id):
#     data = {
#         **request.form
#         'id':id
#     }
#     # data = findBool(data, 'Boolean Key Name') IF YOU HAVE A CHECKBOCK OR BOOLEAN INPUT FROM POST

#     Survey.update_one(data)
#     return redirect('/')

# @app.route('/survey/<int:id>/delete')
# def survey_delete(id):
#     Survey.delete_one({'id': id})

#     return redirect('/')