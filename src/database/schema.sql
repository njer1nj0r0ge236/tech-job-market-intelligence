CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,

    title TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT,
    description TEXT,

    department TEXT,
    employment_type TEXT,

    posted_date DATE,

    url TEXT UNIQUE,

    ats TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);