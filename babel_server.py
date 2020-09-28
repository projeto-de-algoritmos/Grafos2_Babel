from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# from babel import start

socketio = SocketIO()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/babel')
def index():
    return render_template('index.html')

# @socketio.on('start')
# def handle_start(message):
#     print(message)
    

if __name__ == '__main__':
    socketio.run(app)
