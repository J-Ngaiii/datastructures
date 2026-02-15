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

# Window Functions Conceptual

# Window Functions Classics

# Recursive Subqueries Conceptual

# Recursive Subqueries Classics