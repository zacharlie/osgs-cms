@echo off
cd %~dp0
call ./env/Scripts/activate
set FLASK_APP=app
set FLASK_ENV=development
flask run --debugger
