from app.extensions import Base, login, session

from werkzeug.security import check_password_hash, generate_password_hash
from flask_bcrypt import bcrypt
from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, DECIMAL
from sqlalchemy.orm import relationship

@login.user_loader
def load_user(id):
   return session.get(User, int(id))

'''
  Login implementation is discussed in the texctbook or here:
  https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
'''


class User(UserMixin, Base):

  # Set this to the name of the table in the database if 
  # different from the class name defined above.
  __tablename__ = "usersdemo"

  # Schema definition
  id = Column(primary_key=True)
  firstname = Column(String(64))
  nickname  = Column(String(64))
  lastname = Column(String(64))
  email = Column(String(128), unique=True, nullable=False)
  password = Column(String, nullable=False)
  created_on = Column(DateTime)
        
  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.password = self.set_password(password)
    self.created_on = datetime.now()

  def set_password(self, password):
        self.password = generate_password_hash(password)

  def check_password(self, password):
      return check_password_hash(self.password, password)


  def __repr__(self):
      return f'{self.email}'

'''

REATE TABLE `usersdemo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `reset_token` varchar(255) DEFAULT NULL,
  `token_expire` datetime DEFAULT NULL,
  `firstname` varchar(64) DEFAULT NULL,
  `lastname` varbinary(64) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `is_Admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

'''