# base image
FROM postgres:12.1-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
