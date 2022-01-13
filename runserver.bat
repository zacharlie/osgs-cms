@echo off
cd %~dp0
call ./env/Scripts/activate
set FLASK_APP=app
flask run
