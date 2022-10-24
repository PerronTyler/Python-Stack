from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'



@app.route('/destroy_session')
def destroy():
    session.clear()		
    return redirect('/')

@app.route('/')          
def hello_world():
    if 'counter' in session:
        session['counter'] +=1

    else:
        session['counter'] = 1
    


    # if COUNT:
    #     print(COUNT)
    #     COUNT =+ 1
    #     print(COUNT)
    # else:
    #     COUNT = 1

    return render_template('index.html')  
if __name__=="__main__":       
    app.run(debug=True)