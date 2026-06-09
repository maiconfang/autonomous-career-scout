CREATE TABLE opportunity_analysis (

    id SERIAL PRIMARY KEY,

    job_file VARCHAR(255) NOT NULL,

    score INTEGER NOT NULL,

    recommendation TEXT,

    decision VARCHAR(50),

    confidence VARCHAR(50),

    reason TEXT,

    matched_skills JSONB,

    missing_skills JSONB,

    strengths JSONB,

    weaknesses JSONB,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);