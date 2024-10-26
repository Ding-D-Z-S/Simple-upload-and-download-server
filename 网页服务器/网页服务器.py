# -*- coding: gbk -*-
from flask import Flask, request, send_from_directory, render_template
import os

# 配置服务器
app = Flask(__name__)
UPLOAD_FOLDER = '616'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 显示文件列表和上传表单的主页
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

# 上传文件
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "未选择任何文件。", 400
    file = request.files['file']
    if file.filename == '':
        return "未选择任何文件。", 400
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return "文件上传成功！ <a href='/'>返回</a>", 200

# 下载文件
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# 启动服务器
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=616)

