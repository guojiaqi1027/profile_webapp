from flask import Blueprint, render_template

controller = Blueprint('controller', __name__, template_folder="templates")


@controller.route('/')
@controller.route('/index')
def default_page():
    return render_template('index.html')

