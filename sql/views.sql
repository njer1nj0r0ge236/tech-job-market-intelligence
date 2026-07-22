
-- Dashboard Overview

CREATE OR REPLACE VIEW dashboard_overview AS
SELECT
    COUNT(*) AS total_jobs,
    COUNT(DISTINCT company) AS total_companies,
    COUNT(DISTINCT ats) AS total_ats,
    COUNT(*) FILTER (
        WHERE LOWER(location) LIKE '%kenya%'
    ) AS kenya_jobs,
    COUNT(*) FILTER (
        WHERE LOWER(location) LIKE '%remote%'
           OR LOWER(location) LIKE '%worldwide%'
           OR LOWER(location) LIKE '%home%'
           OR LOWER(location) LIKE '%anywhere%'
    ) AS remote_jobs
FROM jobs;



-- Company Summary


CREATE OR REPLACE VIEW company_summary AS
SELECT
    company,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY company
ORDER BY total_jobs DESC;



-- ATS Summary


CREATE OR REPLACE VIEW ats_summary AS
SELECT
    ats,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY ats
ORDER BY total_jobs DESC;



-- Location Summary


CREATE OR REPLACE VIEW location_summary AS
SELECT
    location,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY location
ORDER BY total_jobs DESC;



-- Department Summary


CREATE OR REPLACE VIEW department_summary AS
SELECT
    department,
    COUNT(*) AS total_jobs
FROM jobs
WHERE department IS NOT NULL
GROUP BY department
ORDER BY total_jobs DESC;



-- Employment Type Summary


CREATE OR REPLACE VIEW employment_summary AS
SELECT
    employment_type,
    COUNT(*) AS total_jobs
FROM jobs
WHERE employment_type IS NOT NULL
GROUP BY employment_type
ORDER BY total_jobs DESC;



-- Remote Jobs by Company


CREATE OR REPLACE VIEW remote_summary AS
SELECT
    company,
    COUNT(*) AS total_jobs
FROM jobs
WHERE
    LOWER(location) LIKE '%remote%'
    OR LOWER(location) LIKE '%worldwide%'
    OR LOWER(location) LIKE '%home%'
    OR LOWER(location) LIKE '%anywhere%'
GROUP BY company
ORDER BY total_jobs DESC;



-- Kenya Jobs by Company


CREATE OR REPLACE VIEW kenya_summary AS
SELECT
    company,
    COUNT(*) AS total_jobs
FROM jobs
WHERE LOWER(location) LIKE '%kenya%'
GROUP BY company
ORDER BY total_jobs DESC;



-- Data Roles


CREATE OR REPLACE VIEW data_roles_summary AS
SELECT
    company,
    COUNT(*) AS total_jobs
FROM jobs
WHERE LOWER(title) LIKE '%data%'
GROUP BY company
ORDER BY total_jobs DESC;



-- Software Engineering Roles


CREATE OR REPLACE VIEW software_roles_summary AS
SELECT
    company,
    COUNT(*) AS total_jobs
FROM jobs
WHERE
    LOWER(title) LIKE '%software%'
    OR LOWER(title) LIKE '%developer%'
    OR LOWER(title) LIKE '%engineer%'
GROUP BY company
ORDER BY total_jobs DESC;