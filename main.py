from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/sp')
def sp():
    db_sess = db_session.create_session()
    journal = db_sess.query(Jobs)
    return render_template("journal.html", journal=journal, title='Journal')


if __name__ == '__main__':
    db_session.global_init("db/jobs.db")
    app.run(port=8080, host='127.0.0.1')
