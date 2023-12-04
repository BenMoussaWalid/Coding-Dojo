from flask_app.models.register_models import Register
from flask_app import app
from flask_app.models.user_model import User
from flask import Flask, render_template, redirect, request, session

#_____________________________________
# @app.route("/registers")
# def all_register():
#     if "user_id" not in session:
#         return redirect("/")
#     all_register = Register.read_all()
#     data = {"id": session["user_id"]}
#     one_user = User.get_user_by_id(data)
#     return render_template("all_register.html", all_register=all_register, loggedin_user=one_user)

@app.route("/registers/new")
def registers_form_display():
    return render_template("create_registers.html")
#_____________________________________
#_____________________________________
@app.route("/registers/create", methods=['POST'])
def creation():
    if not Register.validate(request.form):
        return redirect("/registers/new")
    data={
        'name':request.form['name'],
        "description":request.form["description"],
        "instructione":request.form["instructione"],
        "date_m_ade":request.form["date_m_ade"],
        "under":request.form["under"],
        "user_id":session["user_id"]
        
    }
    Register.save(data)
    return redirect('/registers')


@app.route("/registers/<int:id>")
def view_one_recipes(id):
    data={"id":id}
    one_recipes = Register.get_recipes_id(data)
    return render_template("view_one.html",one_recipes=one_recipes)


#_____________________________________


# **** edit page ****
@app.route("/registers/<int:id>/edit")
def update(id):
    if "user_id" not in session:
        return redirect("/")
    data={
            "id":id
    }
    
    register = Register.get_recipes_id(data)
    return render_template("update_registers.html", register=register)
    
# **** action edit****

@app.route("/registers/<int:id>/update", methods=["POST"])
def edit_registers(id):
    if not Register.validate(request.form):
        return redirect(f"/registers/{id}/edit")
    data = {
        **request.form,
        "user_id": session["user_id"],
        "id": id,
    }
    Register.update(data)
    return redirect("/registers")





#____________________________delete________________________
@app.route("/registers/<int:id>/delete")
def delete(id):
    data = {
        "id": id,
    }
    Register.delete(data)
    return redirect("/registers")