# Write your MySQL query statement below
select w.id from Weather w, Weather t where DATEDIFF(w.recordDate, t.recordDate) = 1 and w.temperature > t.temperature