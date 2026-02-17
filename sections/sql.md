---
layout: default
title: "SQL"
date: 2026-02-14
categories: SQL
---
# Special Datatype Handling

## CASE
Def
- Creates a set of values based on some set of conditions
- Great for categorical transformations

Syntax: CASE, WHEN, THEN, ELSE structure
```sql
SELECT 
    col1, 
    col2, 
    CASE 
        WHEN condition1 THEN result1
        WHEN condition2 THEN result2
    ELSE resultN AS col3
FROM tbl;
```

## DISTINCT
- Removes all duplicate rows from the col/set it is applied onto

## Date Handling Methods

### Date Reading/Reformatting
- GETDATE / CURRENT_DATE: Checks system to return current date
- DATEPART / EXTRACT: Pulls a specific part (year, month, day) out
- FORMAT('MM-dd-yyyy'): Allows for custom formatting
    - Especially helpful for aggregation based on date

### Date Difference
- DATEDIFF(unit, start, end): Calculates difference between `start` and `end` date, returning in terms of `unit`
- DATEADD(unit, value, date): Adds an interval of time specified by `value` to `date`, returning in terms of `unit`
    - Helpful for conditionals or numerical transformations

## Text Processing Methods

### Basics
- CONCAT(str1, str2): Concats together `str1` and `str2` with `str1` rendering first
- UPPER() / LOWER(): Modifies ll characters to be upper or lower case
- TRIM(): Removes leading or trailing whitespace

### LIKE keyword
LIKE Def
- We use the `LIKE` keyword when referencing string columns in conditionals:
```sql
SELECT * FROM example
WHERE txt_col LIKE sql_pattern
```

Exact Character Matching
- If you put in raw characters SQL looks for an exact match:
```sql
SELECT * FROM example
WHERE txt_col LIKE 'hello'
-- searches example for rows that exactly equal 'hello' in their txt_col
```
% Operator
- `%` operator matches "any character, any number of times" 
- Great for 'contains XYZ' searches or 'starts with/ends with' searches
```sql
SELECT * FROM example
WHERE txt_col LIKE '%hello%'
-- searches example for rows that contain 'hello' in their txt_col
-- specifically checks for any number of chars, any num of times before 'hello' --> checks for the presence of 'hello' --> theb checks for any number of chars, any num of times after 'hello'
```

_ Operator
- `_` operator matches "any character, one time" 
- Great for a little more precision in 'starts with/ends with' searches
```sql
SELECT * FROM example
WHERE txt_col LIKE 'J_hn'
-- searches example for rows that start with 'J' --> contain any single character --> end with 'hn' in their txt_col
-- so rows with 'John', 'Jehn', 'Juhn' in their txt_col would get returned
```
### SUBSTRING keyword
Forlooping Through Strings
- First usage is basically as a forloop through a string or string col:
```sql
SELECT SUBSTRING(str_or_col FROM start_idx FOR interval_length); 
-- extracts a portion of a string starting from start_idx for interval_length number of characters
```
Regex Searching Through Strings
- Second usage is for applying a regex pattern to a string or string col:
```sql
SELECT SUBSTRING(str_or_col FROM regex_pattern); 
-- extracts a portion of a string starting from start_idx for interval_length number of characters

-- eg, extracting rating from text description
SELECT SUBSTRING('Rated PG-13 for content' FROM 'Rated ([\w-]+)');
```

## Numerical Handling Methods
Operating on numerical cols together
- Helpful for numerical transformation (eg weighted averages)
```sql
SELECT AVERAGE(vals * weights) FROM tbl
GROUP BY col3
```

# Case Statement Classics

## [Evaluate Boolean Expression](https://neetcode.io/problems/sql-evaluate-boolean-expression/history)

### Main Idea
Why it's a classic
- Here the negative cases are way more numerous than the positive cases so we use the `CASE` operator to only define the logic for the less numerous positive cases and leave the rest up to the `ELSE` statement

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

# Aggregations Conceptual
Def
- Aggregations taking multiple rows of data (usually under a specific column) and collapse them into a single value
- Mathematically $\textnormal{agg }: \mathbb{R}^{2} \rightarrow \mathbb{R}^{1}$

Syntax

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

## [1045. Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=study-plan-v2&envId=top-sql-50)

### Main Idea
Intuition
- we need check if a specific customer has bought all items => check if all items under a specific customer fully exhausts all unique items in the product relation
- checking all items/hashset like logic => cue for `DISTINCT` keyword

Why it's classic
- usage of aggregation and `DISTINCT` keyword in conjunction

### Implementation
```sql
SELECT c.customer_id FROM Customer as c
GROUP BY c.customer_id
HAVING COUNT(DISTINCT(c.product_key)) = (SELECT COUNT(DISTINCT(p.product_key)) FROM Product AS p)
```

# Subqueries Conceptual

## Background: EXISTS and NOT EXISTS Keyword
Def
- EXISTS and NOT EXISTS check if at least one row exists as output from some SQL query

Syntax: EXISTS
- The query below checks the relation `shirts` for rows with `color` being `'blue'`. 
    - If no rows in `shirts` have `color` = `'blue'` then the whole query returns `FALSE`
    - If at least one row in `shirts` has `color` = `'blue'` then the whole query returns `TRUE`
```sql
EXISTS (SELECT * FROM shirts WHERE color = 'blue')
```

Syntax: NOT EXISTS
- The query below checks the relation `houses` for rows with `size_sqft` being at least `1000`. 
    - If no rows in `houses` have `size_sqft` >= `1000` then the whole query returns `TRUE`
    - If at least one row in `houses` satisfies `size_sqft` >= `1000` then the whole query returns `FALSE`
```sql
NOT EXISTS (SELECT * FROM houses WHERE size_sqft >= 1000)
```

## Subqueries Definition and Use Cases
Def
- Subqueries are when we nest a whole new `SELECT-FROM-WHERE` query inside an existing `SELECT-FROM-WHERE` SQL query to execute some logic.
- With a subquery we can support creating more complex sets via complex subqueries to do condition checks

Use Cases
- Usually happn in the `WHERE` or `HAVING` clauses, useful for defining more complex conditions
- 'At least one of A' or 'none of B' for some set of values A/B --> `EXISTS` and `NOT EXISTS` strapped onto a subqeury that outputs the set A/B we're interested in
    - A/B can be an individual col, untransformed or a set of really complex values that comes about from multiple joins
- Also pairs well with `SUM` or `COUNT` 

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
# Views

## Definition and Syntax
Def
- Effectively creates a table but does that by basically wrapping an SQL query in a variable assignment
- Outputs are not stored, everytime a view is called the SQL query that defines it is reran
- Exists in the **kernel session** and is accessible as long as the database connection is open after it's been defined
- Best used as variable assignment for certain commonly referenced but non-complex queries
    - Cuz you don't want to be rerunning complex and costly joins and aggregations via a View, at that point use CTE (if it's a throwaway calculation) or a Mat View (if it needs to persist on disk)

Syntax
- Write `CREATE VIEW` then the view_name (in this case `citation_stops`)
- Must have semi-colon at the end of the view definition
- Then you write a whole new query to select from it
```sql
CREATE VIEW citation_stops AS (
    SELECT gender, citation
    FROM stops
    WHERE citation = True
);
-- write new select statement to query on the view
SELECT * FROM citation_stops;
```

## Properties
- Automatically cascades updates from dependent table (cuz updates are not stored --> it's just a query wrapper and reruns the query at each call) => write advantages
- No actual performance upside since outputs are not stored
- Helpful for convenience/query clarity

# Common Table Expressions (CTEs)

## Definition and Syntax
Def
- Temporary table that's created to segment up complex SQL query
- CTE outputs are stored in **working environment** and can be acessed at anytime **during the execution of a SQL query**
    - So in a jupyter notebook if you write a CTE in cell 1 it is gone by cell 2
- Best used as a 'throwaway' table

Syntax
- You start with a `WITH` statement defining and naming the CTE
- Enclose the SQL query defining the body of the CTE with parentheses
- Then you write a `SELECT` statement after the `WITH(<query>)` statement to select the rows you want from your CTE
```sql
WITH temp_table_name AS (
    SELECT col1, col2, FROM another_relation
    WHERE condition
    -- continue writing out any subqeury
)
SELECT col1, col2 FROM temp_table_name;
-- make sure you're not referencing cols not explicitly named in the query that defines the CTE
```

## Properties
- Outputs aere stored and can be accessed at anytime =>  read-advantaged
- If a dependant table is updated --> those updates don't automatically propgate to the CTE => write-disadvantaged, takes greater time and cost to maintain
- Also takes time and resources to create

# Materialized Views
## Definition and Syntax
Def
- Table where outputs are stored and updating happens. semi-automatically
    - In PostgreSQL you a manual refresh mechanism is built in 
    - In MySQL Mat Views implement polling to cascade updates from dependent relations
- Mat View outputs are stored in **on disk** and can be **retrieved during any session after it has been created** (it's a powered up CTE)
- Best for caching 'snapshots' of data outputted by complex aggregations or joins

Syntax
- Write `CREATE VIEW` then the view_name (in this case `citation_stops`)
- Must have semi-colon at the end of the view definition
- Then you write a whole new query to select from it
```sql
CREATE MATERIALIZED VIEW citation_stops AS (
    SELECT gender, citation
    FROM stops
    WHERE citation = True
);
-- write new select statement to query on the view
SELECT * FROM citation_stops;
```

## Properties
- Persists data onto cache
- Most Read-advanatged performance upside cuz it caches outputs. Great for complex joins and aggregations.
- Highest cost when it comes to maintanence and guarding against stale data
    - With a CTE your only risk is if the dependent table updates during the execution of the se SQL query in which the CTE is defined in
    - With a Mat View SQL needs to update it during the kernel session AND write the updated session to disk before the next relevant read/write request
- Only table creation method (compared with View and CTE) that actively consumes cache/disk memory (the other two only exist in session)

# Data Definitional Language (DDL) Conceptual

## Definition and Syntax
Def
- DDL refers to a set of keywords we use to manipulate the **schema** of a relation
- Used to create new tables, delete old tables and alter existing tables
- Also what we use to specify things like primary keys, cols with unique values only, cols that can have `NULL` values, etc
- Why not use `CAST`? Because with DDL we can change the base relation schema directly to avoid having recall `CAST` if we expect to be treating certain values a certain way repeatedly. 

Syntax: Creating Tables
```sql
CREATE TABLE cars (
    id VARCHAR(20) PRIMARY KEY,  --VARCHAR(n) means we allow alphanumeric characters making a string of length n
    carName VARCHAR(100) NOT NULL, 
    factoryId VARCHAR(14) UNIQUE,  --UNIQUE means each row in this table has a unique val under this col
    price DECIMAL(10, 2),  --DECIMAL(k, m) means this col can hold k digits with 2 of them being right of the decimal point
    inStock BOOLEAN, 
    numSold INT, 
    popular BIT -- values are either 1 or 0, conversion to BIT means all non-zero values are converted to 1
);
```

Syntax: Dropping Tables
```sql
DROP TABLE erase_tbl; -- drops erase_tbl entirely from the database
```

```sql
DROP TABLE IF EXISTS erase_tbl; -- same as above but with error handling
```

Syntax: Dropping, Adding and Altering Columns
```sql
ALTER TABLE cars
    ADD saleDate DATE, 
    DROP factoryId;
```

- For PostgreSQL
```sql
ALTER TABLE cars
    ALTER COLUMN numSold TYPE FLOAT;
```
- For MySQL
```sql
ALTER TABLE cars
    MODIFY numSold FLOAT;
```

# Data Manipulation Language (DML) Conceptual

## Definition and Syntax
Def
- DML refers to a set of keywords we use to manipulate the **data** of a relation **given its schema**

Syntax: Adding Rows
```sql
CREATE TABLE cars (
    id VARCHAR(20) PRIMARY KEY,  
    carName VARCHAR(100) NOT NULL, 
    factoryId VARCHAR(14) UNIQUE,  
    price DECIMAL(10, 2),  
    inStock BOOLEAN, 
    numSold INT, 
    popular BIT
);

INSERT INTO target_relation
VALUES
    ('AAa19AYha7', '2025 Honda Accord', 'io7186BH', 22925.60, TRUE, 190, 1), 
    ('AAa18BHoau8s', '2026 Toyota Corolla Cross', 'jk71bah1s', 30952.57, TRUE, 171, 0);
    -- we insert tuples where each value must correspond with the schema for the given target_relation or else we error
```

Syntax: Manipulating Rows
- Delete all rows 
```sql
DELETE FROM target_relation;
```
- Delete rows that satisfy some condition
```sql
DELETE FROM target_relation
WHERE <condition>;
```

- Update rows
```sql
UPDATE target_relation
    SET col1 = col2
    WHERE <condition>;
```

# Window Functions Conceptual

# Window Functions Classics

# Recursive Subqueries Conceptual

# Recursive Subqueries Classics