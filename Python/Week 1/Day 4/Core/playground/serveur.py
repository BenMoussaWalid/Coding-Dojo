from flask import Flask  , render_template 
app = Flask(__name__)    
@app.route('/')         
def hello_world():
    return render_template('index.html',x=3 ,color="blue")
@app.route('/<int:x>')         
def num(x):
    return render_template('index.html',x=x ,color="blue")
@app.route('/<int:x>/<color>')         
def n(x,color):
    return render_template('index.html',x=x,color=color)

if __name__=="__main__":     
    app.run(debug=True)    
    