#!/bin/bash

alembic upgrade head

cd scr

gunicorn main:app --bind:0.0.0.0:8000