from sqlalchemy import  create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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




Session = sessionmaker(bind=engine)
session = Session
test_post = Post(name="Test name", tags="test tags", post="test post")
session.add(test_post)
session.commit()

