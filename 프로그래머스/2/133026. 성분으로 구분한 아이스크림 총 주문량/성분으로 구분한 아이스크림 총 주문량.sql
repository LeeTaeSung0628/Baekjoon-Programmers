-- 코드를 입력하세요
SELECT
    i.ingredient_type
    ,sum(h.TOTAL_ORDER) as TOTAL_ORDER
FROM 
    FIRST_HALF h, ICECREAM_INFO i
WHERE 
    h.FLAVOR = i.FLAVOR
GROUP BY
    i.ingredient_type
ORDER BY 
    TOTAL_ORDER