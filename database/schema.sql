CREATE TABLE focos_incendio (
    id SERIAL PRIMARY KEY,
    data_evento DATE,
    estado VARCHAR(100),
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),
    temperatura DECIMAL(10,2),
    foco INTEGER
);
