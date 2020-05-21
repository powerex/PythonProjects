#!/bin/bash

exec gunicorn --bind=0.0.0.0:8080 --wrokers=1 wsgi:app