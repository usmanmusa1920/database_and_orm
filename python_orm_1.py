import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine_1 = db.create_engine("sqlite:///mydb.db")


class Wrestler(Base):
  __tablename__='wrestler'
  f_name = db.Column(db.String(15), primary_key=True)
  l_name = db.Column(db.String(15), primary_key=True)
  target = db.Column(db.String(15), primary_key=True)
  
Session = sessionmaker(bind=engine_1)
session = Session()
result = session.query(Wrestler.l_name, Wrestler.target)
print(result)



import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import select

Base = declarative_base()

class User(Base):
  __tablename__ = "profile"
  id = sq.Column(sq.Integer, primary_key=True)
  f_name =  sq.Column(sq.String(15), nullable=False)
  l_name = sq.Column(sq.String(15), nullable=False)
  u_name = sq.Column(sq.String(15), nullable=False, unique=True)
  email = sq.Column(sq.String(25), nullable=False)
  num = sq.Column(sq.String(15), nullable=False)
  pwd = sq.Column(sq.Text, nullable=False, unique=False)

  def __repr__(self):
    return f"{self.u_name}'s profile with an id of {self.id}"

engine = sq.create_engine("sqlite://")
# engine = sq.create_engine("mysql+mysqlconnector://root:password@localhost/fug_students")
Base.metadata.create_all(engine)

session = Session(engine)
# f_1 = User(f_name="Usman", l_name="Musa", u_name="Shehu", email="usman@gmail.com", num="4807264", pwd="141")
# f_2 = User(f_name="Yusuf", l_name="Musa", u_name="Myusuf", email="yusuf@gmail.com", num="4807264", pwd="142")
# f_3 = User(f_name="Aisha", l_name="Musa", u_name="Mami", email="aisha@gmail.com", num="4807264", pwd="12343")
# f_4 = User(f_name="Umma", l_name="Sani", u_name="Deejah", email="dija@gmail.com", num="4807264", pwd="12344")
# f_5 = User(f_name="Moh'd", l_name="Tukur", u_name="Tukur", email="tk@gmail.com", num="4807264", pwd="12345")
# f_6 = User(f_name="Abdul", l_name="Adamu", u_name="Aj", email="aj@gmail.com", num="4807264", pwd="12346")
# f_7 = User(f_name="Nasir", l_name="Bima", u_name="Nass", email="nas@gmail.com", num="4807264", pwd="12347")

# session.add_all([f_1, f_2, f_3, f_4, f_5, f_6, f_7])
# session.commit()

# for result in session.query(User).all():
#   print(f"{result.id}. {result}")
# print()
