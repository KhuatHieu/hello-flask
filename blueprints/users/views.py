from flask import Blueprint, render_template

from core.conf import Config

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/')
def index():
    print(Config.DB_URL)

    return render_template('./index.html')
