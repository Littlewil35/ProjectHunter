from sqlalchemy import  create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tags = Column(String)
    post = Column(String)

    def __repr__(self):
        return "<User(name='%s', tags='%s', post='%s')>" % (self.name, self.tags, self.post)






