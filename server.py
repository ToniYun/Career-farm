#!/usr/bin/env python3
"""Career Farm — optional sync server for cross-device state persistence."""
import json
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='.')
STATE_FILE = Path('data/rc_state.json')


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/api/state')
def get_state():
    try:
        if STATE_FILE.exists():
            return jsonify(json.loads(STATE_FILE.read_text(encoding='utf-8')))
        return jsonify({})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/state', methods=['POST'])
def save_state():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({'error': 'invalid data'}), 400
    try:
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text(json.dumps(data), encoding='utf-8')
        return jsonify({'ok': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print('Career Farm server running at http://localhost:5050')
    app.run(port=5050, debug=False)
