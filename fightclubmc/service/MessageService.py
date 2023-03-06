from flask import jsonify

from fightclubmc.model.entity.Message import Message
from fightclubmc.model.repository.MessageRepository import MessageRepository
from fightclubmc.service.UserService import UserService
from fightclubmc.utils.Constants import Constants
from fightclubmc.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 05/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the server service
#

class MessageService():

    @classmethod
    def getAllMessages(cls):
        messages: list[Message] = MessageRepository.getAllMessages()
        return Utils.createList(messages)

    @classmethod
    def getMessages(cls, questionId, toJson=True):
        messages: list[Message] = MessageRepository.getMessages(questionId)
        result: list[dict] = []
        for message in messages:
            owner: dict = UserService.getUser(message.owner_id)
            result.append(message.toJson_Owner(owner))
        print(type(result))
        return jsonify(result) if toJson else result

    @classmethod
    def getMessagesByCategory(cls, categoryId):
        messages: list[Message] = MessageRepository.getMessagesByCategory(categoryId)
        return Utils.createList(messages)

    @classmethod
    def add(cls, request):
        MessageRepository.add(request['question_id'], request['owner_id'], request['body'])
        return Utils.createSuccessResponse(True, Constants.CREATED)
