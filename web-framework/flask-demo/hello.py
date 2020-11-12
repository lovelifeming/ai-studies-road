#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, url_for, escape, request, render_template, redirect

app = Flask(__name__)
""" 启动Flask
    Linux 下: $ export FLASK_APP = hello.py      $ flask run --host=0.0.0.0
    Windows 下:>set FLASK_APP=hello.py    > python -m flask run --host=0.0.0.0
    调试模式
        $ export FLASK_ENV=development          $flask run       #Windows用 set 替换 export
    route变量规则
    string		（缺省值） 接受任何不包含斜杠的文本
    int			接受正整数
    float		接受正浮点数
    path		类似 string ，但可以包含斜杠
    uuid		接受 UUID 字符串

"""


@app.route('/')
@app.route('/index')
def index():
    return "Hello,world!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<postid>')
def show_post(postid):
    # show the post with the given id, the id is an integer
    return 'Post %d' % postid


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/user/profile/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


with app.test_request_context():
    print(url_for('index'))
    print(url_for('show_post', postid='/'))
    print(url_for('profile', username='John Doe'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    uuid = request.cookies.get('uuid')
    print(uuid)
    print(request.method)
    if request.method == 'GET':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = '404.html'
            return redirect(url_for(error))
    return render_template('hello.html', error=error)


def valid_login(name, pwd):
    if name == 'admin' and pwd == '123456':
        return True
    else:
        return False


def log_the_user_in():
    return "please login system!"


def show_the_login_form():
    return "Welcome Vip user!"


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """  HTML 表单中设置 enctype="multipart/form-data" 属性"""
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/uploads/uploaded_file.txt')
    return render_template('404.html'), 404


@app.errorhandler(404)
def miss(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
