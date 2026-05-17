import os
from flask import Flask, request, jsonify, render_template
from database import RoadDatabase
from engine import OpenRoadBot

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load the road database once and keep the bot alive for the web session.
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'roads.json')
db = RoadDatabase(DATA_PATH)
bot = OpenRoadBot(db)

@app.route('/')
def index():
    road_names = [road.road_name for road in db.roads]
    return render_template('index.html', road_names=road_names)

@app.route('/api/roads', methods=['GET'])
def roads():
    road_names = [road.road_name for road in db.roads]
    return jsonify({'roads': road_names})

@app.route('/api/chat', methods=['POST'])
def chat():
    payload = request.get_json(force=True)
    message = payload.get('message', '').strip()
    if not message:
        return jsonify({'reply': 'Please type a message so I can help.'})

    try:
        reply = bot.process_query(message)
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'reply': f'Sorry, something went wrong: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
