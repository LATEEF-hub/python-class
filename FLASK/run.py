import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")



#decorator pie notation
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    """
    This is the About page of our website.
    It explains who we are and what this site is for.
    :return: A rendered template that displays information about us.
    """
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    """
    This function returns a specific member's profile based on their name.
    If no such member exists, it will redirect to the 404 error page.
    :param member_name: The name of the team member you want to see.
    :type member_name: str
    :return: A rendered HTML template displaying the requested team member's info.
             If there is no such user, redirects to /error.
             """
   # check if the file exists in members.json
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)       
       
    


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method =="POST":
        # print(request.form.get("message"))
        # print(request.form["email"])
        # print(request.form)
        flash("Thanks {}, we have received your message!".format(request.form.get('name')))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )