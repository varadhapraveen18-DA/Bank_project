USE bank_project;

-- Query 1:
-- Which Loan Purpose Has The Highest Default Risk? 

SELECT purpose,

ROUND(
SUM(
CASE
WHEN loanStatus = 'Default' THEN 1
ELSE 0
END
)*100.0/COUNT(*),2
) AS default_rate

FROM bank_loans

GROUP BY purpose

ORDER BY default_rate DESC;

-- Query 2:
-- Which Loan Purpose Drives Portfolio Growth with minimal manageable risk?

SELECT
    purpose,
    COUNT(*) AS loan_count,

    ROUND(
        SUM(
            CASE
                WHEN loanStatus = 'Default' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS default_rate

FROM bank_loans

GROUP BY purpose

ORDER BY loan_count DESC;

-- Query 3:
-- Does Employment Stability Reduce Default Risk?
SELECT yearsEmployment,

ROUND(
SUM(
CASE
WHEN loanStatus='Default' THEN 1
ELSE 0
END
)*100.0/COUNT(*),2
) AS default_rate

FROM bank_loans

GROUP BY yearsEmployment

ORDER BY default_rate;

-- Query 4:
-- Does Credit Utilization Predict Default Risk?

SELECT

CASE
WHEN revolvingUtilizationRate <=20 THEN '0-20%'
WHEN revolvingUtilizationRate <=40 THEN '20-40%'
WHEN revolvingUtilizationRate <=60 THEN '40-60%'
WHEN revolvingUtilizationRate <=80 THEN '60-80%'
ELSE '80-100%'
END AS utilization_group,

ROUND(
SUM(
CASE
WHEN loanStatus='Default' THEN 1
ELSE 0
END
)*100.0/COUNT(*),2
) AS default_rate

FROM bank_loans

GROUP BY utilization_group

ORDER BY utilization_group;

-- Query 5:
-- Is The Grading System Identifying Risk Properly?

SELECT grade,

ROUND(
SUM(
CASE
WHEN loanStatus='Default' THEN 1
ELSE 0
END
)*100.0/COUNT(*),2
) AS default_rate

FROM bank_loans

GROUP BY grade

ORDER BY default_rate DESC;


