# project/__init__.py


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask import render_template

app = Flask(__name__)
app.config.from_pyfile('_config.py')
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.tasks.views import tasks_blueprint

# register out blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(tasks_blueprint)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
