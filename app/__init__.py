from flask import Flask
from .extensions import db, scheduler
from app.config import SQLALCHEMY_DATABASE_URI
from .commands import create_tables, drop_tables
from .main import main
import atexit


def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    app.cli.add_command(create_tables)
    app.cli.add_command(drop_tables)

    app.register_blueprint(main)

    with app.app_context():
        db.init_app(app)
        db.app = app

        scheduler.add_jobstore(jobstore='sqlalchemy', alias='default', url=SQLALCHEMY_DATABASE_URI)
        print('SCHEDULER LOADED')
        scheduler.start()

        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())

    return app
