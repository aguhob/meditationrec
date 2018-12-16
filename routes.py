from flask import Flask, render_template, request
from models import db, Stage
from forms import MeditRec

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/minan'
db.init_app(app)

# is meditstages correct? They used learningflask on tutorial.


app.secret_key = 'development-key'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/rec", methods=['GET', 'POST'])
def rec():
    form = MeditRec()
    
    if request.method == 'POST':
        if form.validate() == False:
            return render_template("recommender.html", form=form)
        else:
            newmedit = Stage(form.stage.data, form.description.data)
            db.session.add(newmedit)
            db.session.commit()
            return "Success!"
    elif request.method == 'GET':
        return render_template("recommender.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
