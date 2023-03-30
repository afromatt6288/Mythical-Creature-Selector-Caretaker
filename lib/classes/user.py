#!/usr/bin/env python3
import sys
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, func, desc, ForeignKey, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import Session, relationship, validates, backref
from .base import Base

class User(Base):
    currentUser = None

    __tablename__ ="users"

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    password = Column(String())
    
    def __repr__(self):
        return f"User ID: {self.id} / " \
            + f"User Name: {self.username} / " \
            + f"User Password: {self.password}" 

    def add_to_users_db(self,session):
        session.add(self)
        session.commit()

    def find_by_username(session, username):
        user = session.query(User).filter(User.username == username).first()
        if user:
            return user
        else:
            print(f"Hello there {username}.")    

    def new_user(session):
        user_signup = True
        print("Welcome New Caretaker")
        while user_signup:
            newUsername = input("What is your name?: ")
            if newUsername == "back":
                print("Back to the Begining!")
                user_signup = False
            elif newUsername == "exit":
                sys.exit(0)
            elif User.find_by_username(session, newUsername):
                print("Username already exists. Please Try Again")
            elif type(newUsername) is str and 4 <= len(newUsername):
                newUserPassword = input("Please enter a new password: ")
                if newUserPassword == "back":
                    user_signup = False
                elif newUserPassword == "exit":
                    sys.exit(0)
                elif type(newUserPassword) is str and 4 <= len(newUserPassword):
                    User(username = newUsername, password = newUserPassword).add_to_users_db(session)
                    User.currentUser = User.find_by_username(session, newUsername)
                    user_signup = False
                else:
                    print("Password must be 4 letters or longer!")
            else:
                print("Caretaker name must be 4 letters or longer!")
        return User.currentUser
 
    def returning_user(session):
        user_login = True
        while user_login:
            returningUsername = input("Enter Caretaker Name: ")
            if returningUsername == "back":
                print("Back to the Begining!")
                user_login = False
            elif returningUsername == "exit":
                sys.exit(0)
            elif User.find_by_username(session, returningUsername):
                filtered_user=session.query(User).filter(User.username==returningUsername).first()
                print(f"Welcome back {filtered_user.username}")
                password = input("Enter your Password: ")
                if password == "back":
                    print("Back to the Begining!")
                    user_login = False
                elif password == "exit":
                    sys.exit(0)
                elif filtered_user.password == password:
                    User.currentUser = filtered_user
                    user_login = False
                else:
                    print("Password is incorrect.")
            else:
                print("Caretaker name is not in our system. Please sign up!")
        return User.currentUser


## Extra Commands that could prove useful in a future update

    def create_table(base, engine):
        base.metadata.create_all(engine)

    def get_all_users(session):
        return session.query(User).all()

    def find_by_id(session, id):
        return session.query(User).filter(User.id == id).first()

    def update_username(session, user, username):
        user.username = username
        session.add(user)
        session.commit()
    
    def update_password(session, user, password):
        user.password = password
        session.add(user)
        session.commit()