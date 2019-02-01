#!/usr/bin/env bash

export FLASK_APP=manage.py
export FLASK_ENV=development

env | grep FLASK_

flask run