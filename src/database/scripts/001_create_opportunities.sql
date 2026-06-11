DROP TABLE IF EXISTS opportunities;

CREATE TABLE opportunities (

    id SERIAL PRIMARY KEY,

    linkedin_job_id VARCHAR(50) NOT NULL UNIQUE,

    title VARCHAR(255) NOT NULL,

    company VARCHAR(255),

    location VARCHAR(255),

    job_url TEXT,

    description TEXT,

    skills JSONB,

    match_score INTEGER,

    recommendation VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);