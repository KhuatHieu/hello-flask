from flask import Flask

from blueprints import users

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


app.register_blueprint(users, url_prefix='/users')

if __name__ == '__main__':
    app.run()
