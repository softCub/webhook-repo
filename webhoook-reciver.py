from flask import Flask
from flask import request
from flask import json
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import json

load_dotenv()
mongo = os.getenv('MONGODB_URI')
#print(dir(pymongo))
client = MongoClient(mongo)
print(client.list_database_names())
db = client.webhooks
print(db.list_collection_names())
collections = db.events
app = Flask(__name__)

@app.route('/')
def home():
    return 'home'

@app.route('/webhook',methods=['POST'])
def webhook():
    test= request.headers.get('X-GitHub-Event', "unknown")
    if request.headers['Content-Type']=='application/json':
        text= json.dumps(request.json)
        print(push(test,text))
        return 'ok'

def push(test,text):
    text = json.loads(text)
   # print(text['repository'])
    if test == 'push':
        repo_name=text['repository']['name']
        name=text['head_commit']['author']['name'],
        timestamp=text['head_commit']['author']['date']
        return {'action':test,'user_name':name,'repo_name':repo_name,'timestamp':timestamp}
    elif test=='pull_request':
         name=text['pull_request']['user']['login']
         from_repo=text['pull_request']['head']['ref']
         to_repo=text['pull_request']['base']['ref']
         timestamp=text['pull_request']['head']['repo']['created_at']
         if text['action']=='opened':
            return {'action':test,'user_name':name,'from_repo':from_repo,'to_repo':to_repo,'timestamp':timestamp}
         elif text['action']=='closed':
             return {'action':'merged','user_name':name,'from_repo':from_repo,'to_repo':to_repo,'timestamp':timestamp}

if __name__ =='__main__':
    app.run(debug=True)
