from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, or_
import os

app = Flask(__name__)
db = SQLAlchemy(app)

#create the database format
class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tags = Column(String)
    post = Column(String)
    status = Column(String)

    def __repr__(self):
        return "<Post(name='%s', tags='%s', post='%s', status='%s')>" % (
        self.name, self.tags, self.post, self.status.name)

    def __init__(self, name, tags, post, status):
        self.name = name
        self.tags = tags
        self.post = post
        self.status = status

#convert a post object to an array
def to_arr(arr):
    data = []
    for Post in arr:
        data.append((Post.name, Post.tags, Post.post))
    return data

#the main route, creates database and renders home page
@app.route("/")
def hello():
    cwd = os.getcwd()
    if os.path.exists(cwd):
        #create sqlite file
        database_file = open("ProjectHunter.sqlite", "w+")
        path = os.path.join(cwd, "ProjectHunter.sqlite")
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path
        print()
    else:
        print("Error.")
        exit(0)
    db.create_all()
    data = to_arr(Post.query.all())
    data.__repr__()
    return render_template("index.html", dbData=data)

#processes a post that has been created and adds it to the database
@app.route("/process", methods=['POST'])
def submit():
    name = request.form['postname']
    tag = request.form['tags']
    body = request.form['body']
    status = request.form['status']
    test_post = Post(name, tag, body, status)
    db.session.add(test_post)
    db.session.commit()
    return jsonify('output', str)

#filters for projects currently in progress
@app.route("/upforgrabs")
def query_inprog():
    m_posts = to_arr(Post.query.filter_by(status="In progress").all())
    return render_template("index.html", dbData=m_posts)

#filters for projects seeking collaborators
@app.route("/seekingcolab")
def query_done():
    m_posts = to_arr(Post.query.filter_by(status="Seeking collaborators").all())
    return render_template("index.html", dbData=m_posts)

#filters for projects already completed
@app.route("/completed")
def query_avail():
    m_posts = to_arr(Post.query.filter_by(status="Completed").all())
    return render_template("index.html", dbData=m_posts)

#display all projects
@app.route("/all")
def query_all():
    m_posts = to_arr(Post.query.all())
    return render_template("index.html", dbData=m_posts)

#search for a project
@app.route("/search")
def search():
    args = request.args.get("param")
    print(args)
    m_posts = to_arr(
        Post.query.filter(or_(Post.name == args, Post.tags == args, Post.post == args, Post.status == args)))
    return render_template("index.html", dbData=m_posts)

#delete a project
@app.route("/delete", methods=['POST'])
def delete():
    id = request.form['id']
    Post.query.filter_by(name=id).delete()
    db.session.commit()
    return jsonify('output', str)


if __name__ == "__main__":
    app.run()
