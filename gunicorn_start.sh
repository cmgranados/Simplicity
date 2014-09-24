#!/bin/bash
 
NAME="simplicity_main"                                  # Name of the application
DJANGODIR=/opt/apps/simplicity              # Django project directory
SOCKFILE=/opt/apps/simplicity/gunicorn.sock  # we will communicte using this unix socket
USER=simplicityuser                                        # the user to run as
GROUP=webapps                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=simplicity_main.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=simplicity_main.wsgi                     # WSGI module name
 
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
cd $DJANGODIR
source /opt/simplicity/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /opt/simplicity/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --bind 127.0.0.1:8001 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
