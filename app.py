from sanic import Sanic
from sanic_openapi import swagger_blueprint
from blueprints.health import health_blueprint
from utils import load_env_to_sanic_app

import os
import logging.config

#
# Setup logger
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

#
# Init sanic
app = Sanic(__name__)
logging.info("Service started")

#
# Framework routes
app.blueprint(swagger_blueprint)

#
# Our routes
app.blueprint(health_blueprint)

#
# App config
app.config.API_VERSION = '0.1.0'
app.config.API_TITLE = 'Test sanic server'
app.config.API_PRODUCES_CONTENT_TYPES = ['application/json']

#
# Get docker envs
load_env_to_sanic_app(app, "LISTEN_HOST", "0.0.0.0")
load_env_to_sanic_app(app, "LISTEN_PORT", 1616, env_type=int)


if __name__ == '__main__':
    app.run(host=app.env.listen_host, port=app.env.listen_port)
