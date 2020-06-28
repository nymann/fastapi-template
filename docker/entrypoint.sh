#!/bin/sh

set -e

. /venv/bin/activate

while ! flask db upgrade
do
     echo "Retry..."
     sleep 1
done

exec "$@" 
