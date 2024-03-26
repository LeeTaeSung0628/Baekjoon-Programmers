-- 자동차 아이디별 10/16일을 포함하는 히스토리에 대해서만 체크하여
    -- 그때 대여중일 기록이 있다면 대여중으로 아니면 대여가능으로 한다.



-- with i as(
-- select car_id, '대여중' as AVAILABILITY --대여가 불가능한 리스트
-- from CAR_RENTAL_COMPANY_RENTAL_HISTORY
-- where START_DATE <= to_date('2022-10-16','YYYY-MM-DD') and 
--     END_DATE >= to_date('2022-10-16','YYYY-MM-DD')
-- )

-- select a.car_id
-- ,NVL(i.AVAILABILITY,'대여가능') as AVAILABILITY
-- from CAR_RENTAL_COMPANY_RENTAL_HISTORY a 
--     left join i on i.car_id = a.car_id
-- group by a.car_id,AVAILABILITY
-- order by a.car_id DESC

SELECT CARS.CAR_ID, NVL(AVAILABILITY, '대여 가능') AVAILABILITY
FROM (
    SELECT DISTINCT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) CARS
LEFT JOIN (
    SELECT CAR_ID, '대여중' AVAILABILITY
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE TO_DATE('2022-10-16', 'YYYY-MM-DD') BETWEEN START_DATE AND END_DATE
) RENTAL ON CARS.CAR_ID = RENTAL.CAR_ID
ORDER BY CAR_ID DESC