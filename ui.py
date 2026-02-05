from flask import Blueprint, request, jsonify, render_template
from ferret import collections
from datetime import datetime

ui_route = Blueprint("ui_route", __name__)

@ui_route.route("/")
def home():
    try:
        # Fetch events from MongoDB, sorted by timestamp descending (most recent first)
        events = list(collections.find().sort("timestamp", -1).limit(50))
        
        # Convert ObjectId to string for JSON serialization
        for event in events:
            event['_id'] = str(event['_id'])
            
        return render_template('index.html', events=events)
    except Exception as e:
        print(f"Error fetching events: {e}")
        return render_template('index.html', events=[])

@ui_route.route("/api/events")
def get_events():
    try:
        # Fetch events as JSON API
        events = list(collections.find().sort("timestamp", -1).limit(100))
        
        # Convert ObjectId to string for JSON serialization
        for event in events:
            event['_id'] = str(event['_id'])
            
        return jsonify({'status': 'success', 'events': events})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

