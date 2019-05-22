#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
cd witway_backend
exec gunicorn witway_backend.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3