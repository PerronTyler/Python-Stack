from flask import Flask, render_template  
app = Flask(__name__) 

@app.route('/repeat/<int:num>/<text>')          
def repeat(num=0, text='undefined text'):
    temp = ''
    for indx in range(num):
        temp += text + '\n'
    return f'{temp}!'
@app.route('/say/<name>')          
def say(name):
    print(name)
    return f'Hi {name}!'
@app.route('/dojo')          
def dojo():
    return render_template('dojo.html')
@app.route('/')          
def hello_world():
    return render_template('index.html')  
if __name__=="__main__":       
    app.run(debug=True)
