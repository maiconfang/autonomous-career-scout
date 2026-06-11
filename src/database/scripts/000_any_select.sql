
select * from opportunities;

drop table if exists opportunities;


SELECT
    title,
    company,
    COUNT(*) AS total
FROM opportunities
GROUP BY
    title,
    company
HAVING COUNT(*) > 1
ORDER BY total DESC;

SELECT
    id,
    title,
    company,
    job_url,
    created_at
FROM opportunities
WHERE company = 'Applicantz'
ORDER BY id DESC;

SELECT
    linkedin_job_id,
    COUNT(*) AS total
FROM opportunities
GROUP BY linkedin_job_id
HAVING COUNT(*) > 1;