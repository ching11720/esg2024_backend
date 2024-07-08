FROM mysql:8.0

ARG MYSQL_ROOT_PASSWORD

ENV MYSQL_DATABASE=ESG_db
ENV MYSQL_ROOT_PASSWORD $MYSQL_ROOT_PASSWORD
ENV MYSQL_USER user
ENV MYSQL_PASSWORD $MYSQL_ROOT_PASSWORD

ADD ./backend/scripts/backup.sql /docker-entrypoint-initdb.d

EXPOSE 3307
