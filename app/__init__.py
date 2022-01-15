import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

from app.index import DefaultIndexView


"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(
    app, db.session, indexview=DefaultIndexView, base_template="base.html"
)

from . import views
