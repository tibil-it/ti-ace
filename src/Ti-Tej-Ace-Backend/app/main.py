from celery import Celery
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

import worker
from config import config_json
from controller import front_end_handler, inbuilt_bpp, bpp_handler
from database import db


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(config_json)
    CORS(app)
    api = Api(app)
    db.init_app(app)

    print(app.config["CELERY_BROKER_URL"])

    api.add_resource(front_end_handler.InternalHandler, "/api/internal/<string:action>")
    api.add_resource(inbuilt_bpp.BppProvider, "/bpp/<string:action>")
    api.add_resource(bpp_handler.BppHandler, "/bap/<string:action>")
    app.app_context().push()
    celery = worker.celery
    worker.celery.conf.update(
        broker_url=app.config["CELERY_BROKER_URL"],
        backend=app.config["CELERY_RESULT_BACKEND"]
    )
    celery.Task = worker.ContextTask

    return app, app, celery


app, api, celery = create_app()

if __name__ == '__main__':
    app.run()

