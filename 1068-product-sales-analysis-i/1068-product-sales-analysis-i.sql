# Write your MySQL query statement below
SELECT p.product_name, S.year, S.price from Sales S left join Product P on S.product_id = p.product_id;