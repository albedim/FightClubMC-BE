import datetime

from fightclubmc.configuration.config import sql
from fightclubmc.utils.Constants import Constants


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 05/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user entity
#


class User(sql.Model):
    __tablename__ = 'users'
    user_id: int = sql.Column(sql.Integer, primary_key=True)
    name: str = sql.Column(sql.String(20), nullable=False)
    email: str = sql.Column(sql.String(40), nullable=False)
    password: str = sql.Column(sql.String(40), nullable=False)
    minecraft_username: str = sql.Column(sql.String(40), nullable=False)
    password_forgotten_token: str = sql.Column(sql.String(540), nullable=True)
    likes: int = sql.Column(sql.Integer, nullable=False)
    questions: int = sql.Column(sql.Integer, nullable=False)
    messages: int = sql.Column(sql.Integer, nullable=False)
    admin: bool = sql.Column(sql.Boolean, nullable=False)
    role: str = sql.Column(sql.String(40), nullable=False)
    created_on: datetime = sql.Column(sql.String(40), nullable=False)

    def __init__(self, name, email, minecraftUsername, password):
        self.name = name
        self.created_on = datetime.datetime.now()
        self.role = Constants.MEMBER
        self.messages = 0
        self.likes = 0
        self.questions = 0
        self.minecraft_username = minecraftUsername
        self.email = email
        self.password_forgotten_token = None
        self.password = password
        self.admin = False

    def toJson(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'minecraft_username': self.minecraft_username,
            'likes': self.likes,
            'messages': self.messages,
            'questions': self.questions,
            'admin': self.admin,
            'role': self.role,
            'created_on': str(self.created_on)
        }