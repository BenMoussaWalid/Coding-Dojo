from flask import Flask  , render_template ,session
app = Flask(__name__) 
app.secret_key="your securité"
@app.route('/')          
def hello_count(): 
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"]=0
    return render_template("index.html")

@app.route('/vl')
def clear():
    session.clear()	
    return render_template("index.html")




if __name__=="__main__":   
    app.run(debug=True)