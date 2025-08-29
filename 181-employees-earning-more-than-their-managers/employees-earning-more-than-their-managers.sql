# Write your MySQL query statement below
SELECT e.name as Employee
from Employee e,Employee m
where e.salary > m.salary 
and e.managerId = m.id;