CREATE TABLE opportunity_reports (

    id SERIAL PRIMARY KEY,

    linkedin_job_id VARCHAR(50) NOT NULL UNIQUE,

    title VARCHAR(255) NOT NULL,

    company VARCHAR(255),

    score INTEGER,

    decision VARCHAR(50),

    confidence VARCHAR(50),

    recommendation TEXT,

    strengths JSONB,

    weaknesses JSONB,

    matched_skills JSONB,

    missing_skills JSONB,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);