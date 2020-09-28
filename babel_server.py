from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from babel import build_and_solve
# from babel import start

socketio = SocketIO()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/babel')
def index():
    return render_template('index.html')

@socketio.on('solve')
def handle_solve(graph_data):
    build_and_solve(graph_data, socketio)


if __name__ == '__main__':
    socketio.run(app)
