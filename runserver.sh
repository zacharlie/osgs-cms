#!/usr/bin/bash
THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$THISDIR"
source ./env/Scripts/activate
export FLASK_APP=app
export FLASK_ENV=development
flask run
