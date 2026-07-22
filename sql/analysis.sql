/*
TJMI (Tech Job Market Intelligence)
SQL Analysis

Author: Njeri Njoroge

Purpose:
Exploratory SQL queries used to analyze the collected job dataset.
*/


-- DATASET OVERVIEW

-- 1. Total jobs collected

SELECT COUNT(*) AS total_jobs
FROM jobs;


-- 2. Total companies

SELECT COUNT(DISTINCT company) AS total_companies
FROM jobs;


-- 3. ATS distribution

SELECT
    ats,
    COUNT(*) AS jobs
FROM jobs
GROUP BY ats
ORDER BY jobs DESC;


-- COMPANY ANALYSIS

-- 4. Companies hiring the most

SELECT
    company,
    COUNT(*) AS jobs
FROM jobs
GROUP BY company
ORDER BY jobs DESC;


-- 5. Companies with only one opening

SELECT
    company,
    COUNT(*) AS jobs
FROM jobs
GROUP BY company
HAVING COUNT(*) = 1
ORDER BY company;


-- 6. Companies hiring for Data roles

SELECT
    company,
    COUNT(*) AS jobs
FROM jobs
WHERE LOWER(title) LIKE '%data%'
GROUP BY company
ORDER BY jobs DESC;


-- 7. Companies hiring for Software Engineering roles

SELECT
    company,
    COUNT(*) AS jobs
FROM jobs
WHERE
    LOWER(title) LIKE '%software%'
    OR LOWER(title) LIKE '%developer%'
    OR LOWER(title) LIKE '%engineer%'
GROUP BY company
ORDER BY jobs DESC;


-- 8. Companies hiring remotely

SELECT
    company,
    COUNT(*) AS jobs
FROM jobs
WHERE
    LOWER(location) LIKE '%remote%'
    OR LOWER(location) LIKE '%worldwide%'
    OR LOWER(location) LIKE '%home%'
    OR LOWER(location) LIKE '%anywhere%'
GROUP BY company
ORDER BY jobs DESC;


-- 9. Companies hiring in Kenya

SELECT
    company,
    COUNT(*) AS jobs
FROM jobs
WHERE LOWER(location) LIKE '%kenya%'
GROUP BY company
ORDER BY jobs DESC;


-- LOCATION ANALYSIS

-- 10. Most common job locations

SELECT
    location,
    COUNT(*) AS jobs
FROM jobs
GROUP BY location
ORDER BY jobs DESC
LIMIT 15;


-- 11. Remote job locations

SELECT
    location,
    COUNT(*) AS jobs
FROM jobs
WHERE
    LOWER(location) LIKE '%remote%'
    OR LOWER(location) LIKE '%worldwide%'
    OR LOWER(location) LIKE '%home%'
    OR LOWER(location) LIKE '%anywhere%'
GROUP BY location
ORDER BY jobs DESC;


-- ROLE ANALYSIS

-- 12. Most common job titles

SELECT
    title,
    COUNT(*) AS count
FROM jobs
GROUP BY title
ORDER BY count DESC
LIMIT 15;


-- 13. Employment types

SELECT
    employment_type,
    COUNT(*) AS jobs
FROM jobs
WHERE employment_type IS NOT NULL
GROUP BY employment_type
ORDER BY jobs DESC;


-- 14. Most common words in job titles

SELECT
    word,
    COUNT(*) AS frequency
FROM (
    SELECT
        unnest(
            string_to_array(
                LOWER(title),
                ' '
            )
        ) AS word
    FROM jobs
) words
GROUP BY word
ORDER BY frequency DESC
LIMIT 20;


-- DEPARTMENT ANALYSIS

-- 15. Departments hiring the most

SELECT
    department,
    COUNT(*) AS jobs
FROM jobs
WHERE department IS NOT NULL
GROUP BY department
ORDER BY jobs DESC;


-- ATS ANALYSIS

-- 16. ATS with the most Kenyan jobs

SELECT
    ats,
    COUNT(*) AS jobs
FROM jobs
WHERE LOWER(location) LIKE '%kenya%'
GROUP BY ats
ORDER BY jobs DESC;


-- SKILLS ANALYSIS

-- 17. Mentions of selected programming languages

SELECT
    COUNT(*) FILTER (
        WHERE LOWER(description) LIKE '%python%'
    ) AS python,

    COUNT(*) FILTER (
        WHERE LOWER(description) LIKE '%java%'
    ) AS java,

    COUNT(*) FILTER (
        WHERE LOWER(description) LIKE '%javascript%'
    ) AS javascript,

    COUNT(*) FILTER (
        WHERE LOWER(description) LIKE '%c++%'
    ) AS cpp,

    COUNT(*) FILTER (
        WHERE LOWER(description) LIKE '%go%'
    ) AS go

FROM jobs;