from flask import Flask, render_template  
app = Flask(__name__) 

@app.route('/')
@app.route('/<int:numx>') 
@app.route('/<int:numx>/<int:numy>')
@app.route('/<int:numx>/<int:numy>/<color1>/<color0>')          
def checkerboard(numx=8,numy=8,color1='red',color0='black'):
    return render_template('index.html',numx=numx,numy=numy,color1=color1,color0=color0)  
if __name__=="__main__":       
    app.run(debug=True)