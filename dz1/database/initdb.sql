CREATE USER consumer;
CREATE USER reader;
\c my_database;
CREATE TABLE IF NOT EXISTS queue_data (
    id serial PRIMARY KEY,
    message varchar(256),
    time timestamp
);
GRANT INSERT ON queue_data TO consumer;
GRANT USAGE, SELECT ON queue_data_id_seq TO consumer;
GRANT SELECT ON queue_data TO reader;
