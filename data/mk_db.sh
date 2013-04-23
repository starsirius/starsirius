#!/bin/bash

# BEFORE YOU INSTALL POSTGRES
# Make sure that /usr/local/bin appears first on your $PATH
# If it doesn't, set it in your bash profile or zshrc

# Next see if any Postgres installs are running, if so, kill them
# ps aux | grep postgres

# The steps below are pulled from Brew's post install instructions.
# Please read those and follow here

if [ -d "/usr/local/var/postgres" ]; then
    sleep 0
else
    # Make the core postgres DB
    initdb /usr/local/var/postgres
    exec ./startpostgres.sh
    sleep 3
    /usr/local/bin/createuser -P -s star_admin # password is star_admin
    exec ./stoppostgres.sh
fi

initdb stardb
/usr/local/bin/postgres -D stardb &
/usr/local/bin/createuser -P -s star_admin # password is star_admin
/usr/local/bin/createdb stardb

echo
echo You should edit stardb/postgresql.conf to only listen on localhost - uncomment the line
echo

# Next, you need to unlink OS X Lion's shitty PG install
# curl http://nextmarvel.net/blog/downloads/fixBrewLionPostgres.sh | sh

# now restart, just to be safe

# Finally
# Uninstall any PG gems, python packages, or binaries.  They're linked to the old install directory
# pip uninstall psycopg2ct; pip install --upgrade psycopg2ct; # and then copy src/pyscopg2 to starenv/lib/site-packages

# If you still see an error about pgsql_socket - chown the /var/pgsql_socket dir to your user


#### GETTING THE DATA!!

# start the manager shell, and type in the following:
#>>> from star import db
#>>> from star.models.core import *
#>>> db.create_all()
#>>> db.session.close()
#>>> ^D  # That's a ctrl-d

