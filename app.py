from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db'
db = SQLAlchemy(app)

class School(db.Model):
  __tablename__ = 'schools'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  dbn = db.Column(db.String, primary_key=True)
###this thing is a column by which you will identify each row

@app.route("/")
def hello():
  schools = School.query.all()
  return render_template("list.html", schools=schools)

@app.route("/schools/")
def schools():
  schools = School.query.all()
  return render_template("list.html", schools=schools)

#@app.route("/schools/01M539")
#def school():
#  school= School.query.first()  #this is like saying select * from school
#  return render_template("show.html", school=school)

#@app.route("/schools/01M539")
#def school():
#  school= School.query.filter_by(dbn='01M539').first()  
#  return render_template("show.html", school=school)

@app.route("/schools/<dbn>/")
def school(dbn):
  school= School.query.filter_by(dbn=dbn).first()  
  return render_template("show.html", school=school)

#@app.route("/search")
#def search():
#  name=request.args.get('query')
#  schools = School.query.filter(School.school_name.contains(name)).all()
#  return render_template("list.html", schools=schools)

# If this is running from the command line
# do something
if __name__ == '__main__':
  app.run(debug=True)