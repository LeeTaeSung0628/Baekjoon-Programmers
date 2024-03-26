-- 8~10월 사이에 대여되었던 기록이 있는 차
-- with mm as(SELECT            
--     CAR_ID,
--     count(CAR_ID) as cnt
-- from
--     CAR_RENTAL_COMPANY_RENTAL_HISTORY
-- where
--     START_DATE between to_date('2022-09','YYYY-MM') and to_date('2022-10','YYYY-MM')
-- group by CAR_ID
-- order by CAR_ID)

-- select 
--     to_number(to_char(START_DATE,'MM')) as MONTH,
--     h.CAR_ID,
--     count(h.CAR_ID) as RECORDS
-- from
--     CAR_RENTAL_COMPANY_RENTAL_HISTORY h, mm
-- where
--     h.CAR_ID = mm.CAR_ID
--     and mm.cnt >= 5
-- group by to_number(to_char(START_DATE,'MM')), h.CAR_ID
-- order by MONTH

SELECT  TO_NUMBER(TO_CHAR(START_DATE,'MM')) AS MONTH
        ,CAR_ID
        ,COUNT(HISTORY_ID) AS RECORDS
FROM    CAR_RENTAL_COMPANY_RENTAL_HISTORY MM
WHERE   EXISTS (
--     22년 8월부터 22년 10월까지 총 대여횟수 5회 이상인 자동차
            SELECT  1
            FROM    CAR_RENTAL_COMPANY_RENTAL_HISTORY
            WHERE   START_DATE BETWEEN TO_DATE('20220801','YYYY-MM-DD') AND TO_DATE('20221031','YYYY-MM-DD')
            AND     CAR_ID = MM.CAR_ID
            GROUP BY CAR_ID
            HAVING COUNT(HISTORY_ID) >= 5
        )
-- 8월부터 10월 대여된 월별 자동차 그룹
AND     START_DATE BETWEEN TO_DATE('20220801','YYYY-MM-DD') AND TO_DATE('20221101','YYYY-MM-DD')
GROUP BY TO_CHAR(START_DATE,'MM'), CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC