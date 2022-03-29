FROM postgres
ENV POSTGRES_PASSWORD=123
ENV POSTGRES_DB test_db
ADD init.sql /docker-entrypoint-initdb.d/