Setting up containerized PostGreSQL: 

ephemeral database: 
Log into registry.redhat.io
podman pull registry.redhat.io/rhel8/postgresql-13:latest

podman run -d --name stocktrader_db -e POSTGRESQL_USER=user \
       -e POSTGRESQL_PASSWORD=pass \
       -e POSTGRESQL_DATABASE=stocktrader \
       -p 5432:5432 rhel8/postgresql-13
