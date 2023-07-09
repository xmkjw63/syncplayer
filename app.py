from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"  # 替换为你自己的密钥
socketio = SocketIO(app, cors_allowed_origins="*")

# 共享的播放状态信息
play_state = {"is_playing": False, "current_time": 0}

# 共享的聊天消息列表
chat_messages = []


# 客户端连接时的处理
@socketio.on("connect")
def handle_connect():
    emit("play_state", play_state)
    emit("chat_messages", chat_messages)


# 处理客户端播放事件
@socketio.on("play")
def handle_play(data):
    play_state["is_playing"] = True
    play_state["current_time"] = data["current_time"]
    emit("play_state", play_state, broadcast=True)


# 处理客户端暂停事件
@socketio.on("pause")
def handle_pause(data):
    play_state["is_playing"] = False
    play_state["current_time"] = data["current_time"]
    emit("play_state", play_state, broadcast=True)


# 处理客户端发送聊天消息事件
@socketio.on("send_message")
def handle_send_message(data):
    username = data["username"]
    message = data["message"]
    chat_messages.append({"username": username, "message": message})
    emit("chat_messages", chat_messages, broadcast=True)


# 定义主页路由
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True)
