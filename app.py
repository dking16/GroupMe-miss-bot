from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/message-input', methods=['PUT'])
def recieve_message(message):
    data = request.get_json()
    username = data.user_id
    if username is "64006576":
        target_url = 'curl -X POST "https://api.groupme.com/v3/bots/post?bot_id=IDPLACEHOLDER&text=miss"'
        try:
            response = requests.post(target_url)
            response.raise_for_status() # Raises an HTTPError for bad responses (4XX or 5XX)
            print(f"Request sent successfully, response: {response.status_code}")
            # You can process the response further if needed
            # print(response.json())
        except requests.exceptions.RequestException as e:
            print(f"Error sending request: {e}")
    
