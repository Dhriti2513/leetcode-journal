# Write your MySQL query statement below
WITH FilteredStadium AS (
    SELECT 
        id, 
        visit_date, 
        people,
       
        id - ROW_NUMBER() OVER (ORDER BY id) AS group_id
    FROM 
        Stadium
    WHERE 
        people >= 100
),
StreakCounts AS (
    SELECT 
        id, 
        visit_date, 
        people,
        
        COUNT(*) OVER (PARTITION BY group_id) AS streak_length
    FROM 
        FilteredStadium
)
SELECT 
    id, 
    visit_date, 
    people
FROM 
    StreakCounts
WHERE 
    streak_length >= 3
ORDER BY 
    visit_date ASC;

