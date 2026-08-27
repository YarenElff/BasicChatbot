# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:38:58 2026

@author: Yaren Elif Demir
"""

from chatterbot import ChatBot

bot = ChatBot("Math" , logic_adapters = ["chatterbot.logic.MathematicalEvaluation"])

print("----------- MATH CHATBOT -------------")

while True:
    user_text = input("Type the mat equation that you want to solve: ")
    print("ChatBot: " , bot.get_response(user_text))
    