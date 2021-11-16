FROM mysql

ENV MYSQL_ROOT_PASSWORD=example
ENV MYSQL_DATABASE=recipes

COPY .dockerfiles/database/startup.sql /docker-entrypoint-initdb.d/