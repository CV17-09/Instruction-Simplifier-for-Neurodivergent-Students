CREATE TABLE assignments (
    id SERIAL PRIMARY KEY,
    original_text TEXT NOT NULL,
    simplified_output TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);