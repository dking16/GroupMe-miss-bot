from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

GROUPME_BOT_ID = "6c0eda51780232fbaf87826529"
TARGET_USER_ID = "64006576"

@app.route('/message-input', methods=['POST'])
def recieve_message():
    data = request.get_json()
    print(f"Received data: {data}")
    sender_id = data.get("sender_id")
    text = data.get("text")


    if sender_id == TARGET_USER_ID:
        print(f"Received message from target user {TARGET_USER_ID}: '{text}'")
        
        # Prepare to send a message back
        # groupme_api_url = "https://api.groupme.com/v3/bots/post?bot_id=30e8ca05dd8604fb691892efd8&text=miss" # Old incorrect way

        groupme_post_url = "https://api.groupme.com/v3/bots/post"
        payload = {
            "bot_id": GROUPME_BOT_ID,  # Your bot ID from the top of the file
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
    app.run(host='0.0.0.0', port=5000, debug=True) # Added debug=True for development
    # app.run(debug=True)
