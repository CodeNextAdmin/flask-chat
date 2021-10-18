import os
from flask import Flask, render_template
from sense_hat import SenseHat
from flask_socketio import SocketIO 

app = Flask(__name__)

sense = SenseHat()

app.config['SECRET_KEY'] = SOCKET-IO-SECRET #CHANGE TO YOUR OWN
socketio = SocketIO(app)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: '+ str(json))
    socketio.emit('my response', json, callback=messageReceived)

@app.route('/')
def sessions():
    return render_template('session.html')


if __name__ == '__main__':
    socketio.run(app, debug=True , host='0.0.0.0')
