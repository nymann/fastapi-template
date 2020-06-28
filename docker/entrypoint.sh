#!/bin/sh

set -e

while ! alembic upgrade head
do
     echo "Retry..."
     sleep 1
done

exec "$@" 
