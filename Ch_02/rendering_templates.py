from flask import Flask, render_template, request

app = Flask(__name__)


# rendering templates
@app.route('/temp')
def using_templates():
    return render_template('hello.html')