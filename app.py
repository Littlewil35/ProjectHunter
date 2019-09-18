from flask import Flask, render_template
from sqlalchemy import  create_engine, Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tags = Column(String)
    post = Column(String)

    def __repr__(self):
        return "<Post(name='%s', tags='%s', post='%s')>" % (self.name, self.tags, self.post)

    def __init__(self, name, tags, post):
        self.name = name
        self.tags = tags
        self.post = post


@app.route("/")
def hello():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    db.create_all()
    test_post = Post('test1', 'test2', 'test3')
    db.session.add(test_post)
    db.session.commit()
    return render_template("index.html", dbData=Post.query.all())


if __name__ == "__main__":
    app.run(debug=True)
