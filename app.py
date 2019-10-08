from importlib.resources import contents

from flask import Flask, render_template, request, jsonify
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

app = Flask(__name__)
db = SQLAlchemy(app)

class status(Enum):
    done = 1
    in_prog = 2
    avail = 3

class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tags = Column(String)
    post = Column(String)
    status = Column(String)


    def __repr__(self):
        return "<Post(name='%s', tags='%s', post='%s', status='%s')>" % (self.name, self.tags, self.post, self.status)

    def __init__(self, name, tags, post, status):
        self.name = name
        self.tags = tags
        self.post = post
        self.status = status


def to_arr(arr):
    data = []
    for Post in arr:
        data.append((Post.name, Post.tags, Post.post))
    return data

@app.route("/")
def hello():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.create_all()
    data = to_arr(Post.query.all())
    m_posts = to_arr(Post.query.filter_by(status='current').all())
    print(data)
    return render_template("index.html", dbData=data)



@app.route("/process", methods=['POST'])
def test():
    name = request.form['postname']
    tag = request.form['tags']
    body = request.form['body']
    status = request.form['status']
    test_post = Post(name,tag,body,status)
    db.session.add(test_post)
    db.session.commit()
    return jsonify('output', str)



if __name__ == "__main__":
    app.run()
