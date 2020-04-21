from services import DrQA, process



import json
from flask import Flask, render_template, request
app = Flask(__name__)

from services import DrQA, process

@app.route("/")
def index():
    #print('went into index function')
    return render_template("index.html")
	

@app.route("/query", methods=["POST"])
def query():
    #print('went into query function')
    data = request.json
    #print('inside flask query data request jason', data)
    answers = process(question=data['question'])
    #print('inside flask query',json.dumps(answers))
    return json.dumps(answers)

if __name__ == '__main__':
	app.run()




# question = "what is coronavirus?"
# answers = process(question)

# print("--------------------------------------")
# print("answer = ",answers[0]['span'])
# print("--------------------------------------")
# print("context = ",answers[0]['text'])

