-- -- 코드를 입력하세요
select 
u.user_id,
u.NICKNAME,
b.sp as TOTAL_SALES
from
USED_GOODS_USER u,
(
SELECT
    WRITER_ID,
    sum(PRICE) as sp
from
    USED_GOODS_BOARD
where
    STATUS = 'DONE'
group by
    WRITER_ID
) b
where
u.USER_ID = b.WRITER_ID
and b.sp >= 700000
order by
b.sp ASC

-- -- 코드를 입력하세요
-- SELECT A.USER_ID,A.NICKNAME,B.TOTAL_SALES
--   FROM USED_GOODS_USER A
--  INNER JOIN (SELECT WRITER_ID, SUM(PRICE) AS TOTAL_SALES 
--                FROM USED_GOODS_BOARD 
--               WHERE STATUS = 'DONE'
--               GROUP BY WRITER_ID) B
--     ON A.USER_ID = B.WRITER_ID
--  WHERE B.TOTAL_SALES >= 700000
--  ORDER BY B.TOTAL_SALES
