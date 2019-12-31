from enum import Enum
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, or_

app = Flask(__name__)
db = SQLAlchemy(app)


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
    data.__repr__()
    return render_template("index.html", dbData=data)


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


@app.route("/upforgrabs")
def query_inprog():
    m_posts = to_arr(Post.query.filter_by(status="In progress").all())
    return render_template("index.html", dbData=m_posts)


@app.route("/seekingcolab")
def query_done():
    m_posts = to_arr(Post.query.filter_by(status="Seeking collaborators").all())
    return render_template("index.html", dbData=m_posts)


@app.route("/completed")
def query_avail():
    m_posts = to_arr(Post.query.filter_by(status="Completed").all())
    return render_template("index.html", dbData=m_posts)


@app.route("/all")
def query_all():
    m_posts = to_arr(Post.query.all())
    return render_template("index.html", dbData=m_posts)


'''@app.route("/search", methods=['POST'])
def search():
    searchText = request.form['searchText']
    print(searchText)
    m_posts = to_arr(Post.query.filter_by(name=searchText).all())
    print(m_posts)
    return render_template("index.html")
'''


@app.route("/search")
def search():
    args = request.args.get("param")
    print(args)
    m_posts = to_arr(
        Post.query.filter(or_(Post.name == args, Post.tags == args, Post.post == args, Post.status == args)))
    return render_template("index.html", dbData=m_posts)

@app.route("/delete", methods=['POST'])
def delete():
    id = request.form['id']
    Post.query.filter_by(name=id).delete()
    db.session.commit()
    return jsonify('output', str)


if __name__ == "__main__":
    app.run()
