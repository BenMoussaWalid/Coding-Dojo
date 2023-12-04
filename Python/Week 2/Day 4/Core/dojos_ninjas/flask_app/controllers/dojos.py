from flask_app import app
from flask import redirect,request,render_template
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    all_dojos=Dojo.get_all()
    return render_template('dojos.html',all_dojos=all_dojos)


@app.route('/create/dojo',methods=["post"])
def create_dojo():
    data={"name":request.form['name']}
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def details(id):
    data= {
        "id":id
    }
    return render_template('dojo.html',dojo=Dojo.get_one_by_id(data),ninjas=Ninja.get_by_dojo_id(data))