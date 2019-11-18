from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import chatterbot_corpus
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random
from django.core.files import File
chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)


trainer = ChatterBotCorpusTrainer(chatbot)
# chatbot.trainer.train('chatterbot.corpus.english')
# chatbot.trainer.export_for_training('./export.yml')

import gpt_2_simple as gpt2
import os
import requests