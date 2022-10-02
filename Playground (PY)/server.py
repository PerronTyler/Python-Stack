from flask import Flask, render_template  
app = Flask(__name__) 
@app.route('/play/')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')          
def boxes(num=3, color = 'blue'):
    return render_template('index.html', num=num, color=color)
@app.route('/')          
def hello_world():
    return render_template('index.html')  
if __name__=="__main__":       
    app.run(debug=True)