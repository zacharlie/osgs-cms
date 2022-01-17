import pytest

import os
import tempfile
import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

from app.index import DefaultIndexView

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.ERROR)

app = Flask(__name__)
app.config.from_pyfile("../config.py")
db = SQLA(app)
appbuilder = AppBuilder(
    app, db.session, indexview=DefaultIndexView, base_template="app/templates/base.html"
)

from app import views


@pytest.fixture
def client():
    db_fd, app.config["DATABASE"] = tempfile.mkstemp()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            app.init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config["DATABASE"])


def login(client, username, password):
    return client.post(
        "/login", data=dict(username=username, password=password), follow_redirects=True
    )


def logout(client):
    return client.get("/logout", follow_redirects=True)
