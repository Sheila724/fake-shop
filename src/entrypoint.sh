#!/bin/bash
export FLASK_APP=index.py
python -m flask db upgrade
python -m gunicorn --bind 0.0.0.0:8213 index:app