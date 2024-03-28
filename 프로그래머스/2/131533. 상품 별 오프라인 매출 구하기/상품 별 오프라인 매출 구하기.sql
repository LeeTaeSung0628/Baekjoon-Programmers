-- 코드를 입력하세요
SELECT 
    p.PRODUCT_CODE,
    sum(o.SALES_AMOUNT) * p.PRICE as SALES
    
from PRODUCT p, OFFLINE_SALE o
where o.PRODUCT_ID = p.PRODUCT_ID
group by p.PRODUCT_CODE
order by SALES DESC, p.PRODUCT_CODE
