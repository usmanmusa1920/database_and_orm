# this is an sqlalchemy script for creating user profile table
# and also populate some data into the table


import sqlalchemy as sq
import os
from sqlalchemy import select
from sqlalchemy.orm import declarative_base, Session


os.system('clear')
Base = declarative_base()


class UserProfile(Base):
  __tablename__ = "profile"
  id = sq.Column(sq.Integer, primary_key=True)
  fullname = sq.Column(sq.String(30), nullable=False)
  username = sq.Column(sq.String(20), nullable=False, unique=True)
  bio = sq.Column(sq.Text, nullable=True)
    
#  def __repr__(self):
#    return f"repr {self.username}'s profile with an id of {self.id}"
  
  def __str__(self):
    return f"{self.username}'s profile with an id of {self.id}"
    
    
    
engine = sq.create_engine("sqlite://")
Base.metadata.create_all(engine)
s = Session(engine)

i_1 = UserProfile(fullname="Usman Musa", username="Shehu", bio="A software engineer")
i_2 = UserProfile(fullname="Muhammad Usman", username="Tukur")
i_3 = UserProfile(fullname="Aisha Musa", username="Mami")
i_4 = UserProfile(fullname="Hadiza Ibrahim", username="Deejah")
i_5 = UserProfile(fullname="Yusuf Musa", username="Myusuf", bio="Doctor of science")

s.add_all([i_1, i_2, i_3, i_4, i_5])
s.commit()


stmt = select(UserProfile).where(UserProfile.username.in_(["Shehu", "Myusuf"]))
print('Filtering user from database:\n')
for user in s.scalars(stmt):
     print(f"  {user}\n\t{user.username}, {user.id}, {user.fullname}\n")
     
print()
print('Querying users from database:\n')
for i in s.query(UserProfile).all():
  print(f"{i.id}. {i.fullname} ({i.username})")
print()
