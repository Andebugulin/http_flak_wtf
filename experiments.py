from flask import Flask, url_for, request, render_template, redirect


app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index')
def index():

    return render_template('base_for_lesson1.html', title="meaw")

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')