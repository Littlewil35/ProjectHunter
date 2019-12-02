from enum import Enum
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

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
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/william/ProjectHunter.sqlite'
    db.create_all()
    data = to_arr(Post.query.all())
    m_posts = to_arr(Post.query.filter_by(status='current').all())
    data.__repr__()
    return render_template("index.html", dbData=data)


@app.route("/process", methods=['POST'])
def test():
    name = request.form['postname']
    tag = request.form['tags']
    body = request.form['body']
    status = request.form['status']
    test_post = Post(name, tag, body, status)
    db.session.add(test_post)
    db.session.commit()
    return jsonify('output', str)

@app.route("/upforgrabs")
def query_inprog():
    m_posts = to_arr(Post.query.filter_by(status='avail').all())
    return render_template("index.html", dbData=m_posts)

@app.route("/seekingcolab")
def query_done():
    m_posts = to_arr(Post.query.filter_by(status='in_prog').all())
    return render_template("index.html", dbData=m_posts)

@app.route("/completed")
def query_avail():
    m_posts = to_arr(Post.query.filter_by(status='done').all())
    return render_template("index.html", dbData=m_posts)



if __name__ == "__main__":
    app.run()
