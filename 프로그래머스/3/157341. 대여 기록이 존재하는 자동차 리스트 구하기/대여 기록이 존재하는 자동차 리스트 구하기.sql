-- 코드를 입력하세요
select 
    h.car_id
from
    CAR_RENTAL_COMPANY_RENTAL_HISTORY h
    ,(SELECT car_id,car_type
    from CAR_RENTAL_COMPANY_CAR
    where car_type = '세단') c

where
    h.CAR_ID = c.CAR_ID
    and (start_date between to_date('2022-10-01','YYYY-MM-DD') and to_date('2022-10-31','YYYY-MM-DD'))
group by
    h.car_id
order by car_id DESC