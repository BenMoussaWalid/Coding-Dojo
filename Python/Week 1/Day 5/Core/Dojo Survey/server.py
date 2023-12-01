from flask import Flask, render_template, redirect,request,session

app = Flask(__name__)
app.secret_key = 'i have secret key'
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("*"*20, request.form,"*"*20)
    session["name"] = request.form["name"]
    session["comments"] = request.form["comments"]
    session["Location"] = request.form["Location"]
    session["fav_language"] = request.form["fav_language"]
    return redirect('/result')

@app.route('/action')
def result():
    return render_template("action.html")



if __name__ == "__main__":
    app.run(debug=True)
