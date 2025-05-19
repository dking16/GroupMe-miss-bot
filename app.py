from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

DELTS_27_BOT = "6c0eda51780232fbaf87826529"
RICE_BOT = "30e8ca05dd8604fb691892efd8"
DELTS_27_ID = "100792105"
RICE_ID = "104635793"
JOHN_ID = "64006576"


@app.route('/message-input', methods=['POST'])
def recieve_message():
    data = request.get_json()
    print(f"Received data: {data}")
    sender_id = data.get("sender_id")
    group_id = data.get("group_id")
    text = data.get("text")


    if sender_id == JOHN_ID:
        print(f"Received message from target user {JOHN_ID}: '{text}'")
        
        working_bot = ""
        
        if group_id == DELTS_27_ID:
            working_bot = DELTS_27_BOT
        if group_id == RICE_ID:
            working_bot = RICE_BOT

        
        groupme_post_url = "https://api.groupme.com/v3/bots/post"
        payload = {
            "bot_id": working_bot,  # Your bot ID from the top of the file
            "text": "miss"
        }

        try:
            # The 'json' parameter in requests.post automatically sets
            # 'Content-Type: application/json' and serializes the payload dict.
            response = requests.post(groupme_post_url, json=payload)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
            print(f"Message sent to GroupMe successfully. Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending message to GroupMe: {e}")

            return jsonify({"status": "error", "message": "Failed to send reply to GroupMe"}), 500
        
        return jsonify({"status": "success", "message_sent": "miss"}), 200
    else:
        print(f"Message from other user ({sender_id}), not responding.")
        return jsonify({"status": "ignored", "reason": "not target user"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8789, debug=True) # Added debug=True for development
    # app.run(debug=True)
