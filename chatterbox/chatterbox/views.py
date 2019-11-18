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

import os
import requests

@csrf_exempt
def get_response(request):
	response = {'status': None}
	# f = open('blank.txt', 'r+')	
	
	
	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))
		message = data['message']
		print(message)
		chat_response = chatbot.get_response(message).text
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True, 'username' : "Bot: "}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)


def home(request, template_name="home.html"):
	context = {'title': 'Chatbot Version 1.0'}
	return render_to_response(template_name, context)
