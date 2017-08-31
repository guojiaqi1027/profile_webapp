from flask import Flask
from src.api import controller, public_api, profile_api, summary_api, education_api

app = Flask(__name__)
app.register_blueprint(controller)
app.register_blueprint(public_api)
app.register_blueprint(profile_api)
app.register_blueprint(summary_api)
app.register_blueprint(education_api)
if __name__ == '__main__' or __name__  == 'run':
    app.run(port=9000)
