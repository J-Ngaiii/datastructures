---
layout: default
title: "SQL"
date: 2026-02-14
categories: DSQLA
---

# Subqueries Conceptual

IMAGE HERE

# Subqueries Classics

## [Customers Who Bought A and B but Not C](https://neetcode.io/problems/sql-customers-bought-a-b-not-c/question)

### Main Idea
Intuition
- We want to check if a given user as bought at least one of a certain set of item => we check for at least one row satisfying certain conditions => `EXISTS` or `NOT EXISTS`

Why it's classic
- At least one / none of conditions are a classic cue for using `EXISTS` / `NOT EXISTS`

### Implementation
```sql
SELECT c.customer_id, c.customer_name FROM customers AS c 
WHERE 
    EXISTS (
        SELECT * FROM orders AS o
        WHERE o.customer_id = c.customer_id AND product_name = 'A'
    )
    AND
    EXISTS (
        SELECT * FROM orders AS o
        WHERE o.customer_id = c.customer_id AND product_name = 'B'
    )
    AND
    NOT EXISTS (
        SELECT * FROM orders AS o
        WHERE o.customer_id = c.customer_id AND product_name = 'C'
    )
ORDER BY c.customer_name
```

## [570. Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50)

### Main Idea
Why it's a classic
- Using a subqeury to do some aggregation then comparing with a where clause

### Implementation
```sql
SELECT e1.name FROM Employee AS e1
WHERE (
    SELECT COUNT(*) FROM Employee AS e2
    WHERE e2.managerId = e1.id
    ) >= 5
```

# Case Statement Conceptual

# Case Statement Classics

## [Evaluate Boolean Expression](https://neetcode.io/problems/sql-evaluate-boolean-expression/history)

### Main Idea

### Implementation
```sql
SELECT 
    e.left_operand, 
    e.operator, 
    e.right_operand,
    CASE -- use `CASE` keyword 
        WHEN e.operator = '>' AND v1.value > v2.value THEN 'true' -- don't try to directly pull operator 
        WHEN e.operator = '<' AND v1.value < v2.value THEN 'true' -- translate what it means in SQL
        WHEN e.operator = '=' AND v1.value = v2.value THEN 'true' -- set the true conditions and else false all else
        ELSE 'false' -- else false cuz there's more false cases than true ones
    END AS value
FROM expressions e -- double join so we have
JOIN variables v1 ON e.left_operand = v1.name -- one col w/ left translated into nums
JOIN variables v2 ON e.right_operand = v2.name; -- one col w/ right translated into nums
```

# Data Manipulation Language (DML) Conceptual

# Data Manipulation Language (DML) Classics

# Data Definitional Language (DDL) Conceptual

# Data Definition Language (DDL) Classics

# Aggregations Conceptual

# Aggregations Classics

## [1193. Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/description/?envType=study-plan-v2&envId=top-sql-50)

### Main Idea
Why it's classic
- Avoiding "gotcha" of just extracting the month via `MONTH(trans_date)` since we ned to group by every month in every year
- Date formating methods
- Conditional aggregation using CASE statements. Specifically conditonal counting via SUM 1 ELSE 0. 

### Implementation
```sql
SELECT 
    -- we format YYYY-MM to avoid counting Jan 2024 and Jan 2025 as the same
    DATE_FORMAT(trans_date, '%Y-%m') AS month, 
    country,
    COUNT(*) AS trans_count,
    -- using case statements wrapped in for conditional aggregation
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY YEAR(trans_date), MONTH(trans_date), country;
```

# Window Functions Conceptual

# Window Functions Classics

# Recursive Subqueries Conceptual

# Recursive Subqueries Classics