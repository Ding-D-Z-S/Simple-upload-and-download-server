# -*- coding: gbk -*-
from flask import Flask, request, send_from_directory, render_template
import os

# ���÷�����
app = Flask(__name__)
UPLOAD_FOLDER = '616'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ��ʾ�ļ��б���ϴ�������ҳ
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

# �ϴ��ļ�
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "δѡ���κ��ļ���", 400
    file = request.files['file']
    if file.filename == '':
        return "δѡ���κ��ļ���", 400
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return "�ļ��ϴ��ɹ��� <a href='/'>����</a>", 200

# �����ļ�
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# ����������
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=616)

