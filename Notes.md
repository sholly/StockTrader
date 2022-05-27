Setting up containerized PostGreSQL: 

ephemeral database: 
Log into registry.redhat.io
podman pull registry.redhat.io/rhel8/postgresql-13:latest

# Run ephemeral database
podman run --rm -d --name stocktrader_db -e POSTGRESQL_USER=user \
       -e POSTGRESQL_PASSWORD=pass \
       -e POSTGRESQL_DATABASE=stocktrader \
       -p 5432:5432 rhel8/postgresql-13

# Run ephemeral database
podman run -d --name stocktrader_db -e POSTGRESQL_USER=user \
       -e POSTGRESQL_PASSWORD=pass \
       -e POSTGRESQL_DATABASE=stocktrader \
       -p 5432:5432 rhel8/postgresql-13

Install a virtualenv: 
virtualenv virtualenv

Activate: 
. ./virtualenv/bin/activate

Install dependencies: 
pip install requirements.txt
