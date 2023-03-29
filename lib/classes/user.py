#!/usr/bin/env python3
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
            if User.find_by_username(session, newUsername):
                print("Username already exists. Please Try Again")
            elif type(newUsername) is str and 4 <= len(newUsername):
                newUserPassword = input("Please enter a new password: ")
                if type(newUserPassword) is str and 4 <= len(newUserPassword):
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
            if User.find_by_username(session, returningUsername):
                filtered_user=session.query(User).filter(User.username==returningUsername).first()
                print(f"Welcome back {filtered_user.username}")
                password = input("Enter your Password: ")
                if filtered_user.password == password:
                    User.currentUser = filtered_user
                    user_login = False
                else:
                    print("Password is incorrect.")
            else:
                print("Caretaker name is not in our system. Please sign up!")
        return User.currentUser









    def create_table(base, engine):
        base.metadata.create_all(engine)

    def get_all(session):
        return session.query(User).all()


    def find_by_id(session, id):
        return session.query(User).filter(User.id == id).first()

    def find_by_name_and_breed(session, name, breed):
        return session.query(User).filter(User.name == name and User.breed == breed).first()

    def update_breed(session, user, breed):
        user.breed = breed
        session.add(user)
        session.commit()