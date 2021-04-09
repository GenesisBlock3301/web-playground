from flask import Flask
from flask import render_template
from flask import request
import os
from flask_sqlalchemy import SQLAlchemy
from flask import redirect

f = __file__
current_file_name = os.path.abspath(f)
project_dir = os.path.dirname(current_file_name)
app = Flask(__name__)
databases_file = f"sqlite:///{os.path.join(project_dir, 'bookDatabase.db')}"

app.config["SQLALCHEMY_DATABASE_URI"] = databases_file

db = SQLAlchemy(app)


# database model

class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __str__(self):
        return f"{self.title}"


# view
@app.route("/", methods=["GET", "POST"])
def home():
    status = True
    if request.form:
        try:
            book = Book(title=request.form.get('title'))
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",book)
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            status = False
    books = Book.query.all()
    return render_template('home.html', books=books,status=status)


@app.route("/update",methods=['POST'])
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    print("@@@@@@@@@@@",newtitle,oldtitle)
    book = Book.query.filter_by(title=oldtitle).first()
    book.title = newtitle
    db.session.commit()
    return redirect("/")


@app.route("/delete",methods=['POST'])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
