SELECT
    job_file,
    score,
    decision,
    confidence
FROM opportunity_analysis
ORDER BY score DESC;