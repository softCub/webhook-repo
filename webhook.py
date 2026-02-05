from flask import Flask,request,json,Blueprint,jsonify
from ferret import collections

webhook_route = Blueprint('webhook_route', __name__)

@webhook_route.route('/webhook',methods=['POST'])
def webhook():
    test= request.headers.get('X-GitHub-Event', "unknown")
    if request.headers['Content-Type']=='application/json':
        text= json.dumps(request.json)
        event_data = git_event_handler(test,text)
        
        if event_data:
            try:
                # Store event data in MongoDB
                collections.insert_one(event_data)
                return jsonify({'status': 'success', 'message': 'Event stored'}), 200
            except Exception as e:
                return jsonify({'status': 'error', 'message': str(e)}), 500
        else:
            return jsonify({'status': 'error', 'message': 'No event data processed'}), 400
    
    return jsonify({'status': 'error', 'message': 'Invalid content type'}), 400

def git_event_handler(test,text):
    text = json.loads(text)
   # print(text['repository'])
    if test == 'push':
        repo_name=text['repository']['name']
        name=text['head_commit']['author']['name']
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
    return None
