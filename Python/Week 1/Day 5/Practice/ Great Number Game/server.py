from flask import Flask  , render_template, session
import random 
app = Flask(__name__) 

@app.route('/')        

def index():

    randomNumber = random.randint(1, 100) 
    if randomNumber is not session:
        return session['']

    return render_template("index.html" , randomNumber = randomNumber) 




if __name__=="__main__":  
    app.run(debug=True)  
