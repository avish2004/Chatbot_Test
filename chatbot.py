from flask import Flask, request, jsonify
from src.model import chatbot_response

app = Flask(__name__)

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    message = data.get("message")
    response = chatbot_repisponse(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)


