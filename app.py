from bot import get_response
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.get('/')
def base():
    return render_template('base.html')

@app.post('/predict')
def pick_reply():
    msg = request.get_json().get('message')
    response = get_response(msg)
    message = {'answer': response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug = True)