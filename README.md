# 视频同步播放程序

这是一个使用 Flask 和 Flask-SocketIO 构建的视频同步播放程序。它允许多个用户同时观看相同的视频，并实现了播放状态同步和聊天功能。

## 功能特点

- 多用户同时观看同一视频。
- 实时播放状态同步，包括播放和暂停。
- 聊天室功能，用户可以在观看视频时进行聊天交流。

## 安装和运行

1. 克隆项目到本地：

   ```bash
   git clone https://github.com/your-username/video-sync.git
   cd video-sync
   ```

2. 创建并激活虚拟环境（可选）：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

4. 运行应用：

   ```bash
   python app.py
   ```

5. 在浏览器中访问 `http://localhost:5000` 即可开始使用视频同步播放程序。

## 使用说明

- 打开视频同步播放程序后，你将看到一个视频播放器和一个聊天室界面。
- 所有用户将同步观看同一视频，并可以通过播放和暂停按钮来控制视频播放状态。
- 在聊天室中，用户可以发送聊天消息，并实时在其他用户的聊天室界面中显示。

## 技术栈

- Flask - Python 的 Web 框架，用于构建后端应用。
- Flask-SocketIO - 用于实现实时双向通信的 Flask 扩展。
- Plyr - 现代化的 HTML5 视频播放器，提供了丰富的播放控制和样式。

## 贡献

欢迎提出问题、报告 bug 或贡献代码。请查阅项目的 [贡献指南](CONTRIBUTING.md) 了解更多详情。

## 许可证

该项目采用 [MIT 许可证](LICENSE) 进行许可。
