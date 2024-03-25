-- 코드를 입력하세요
select 
    c.WRITER_ID as USER_ID,
    u.NICKNAME as NICKNAME,
    u.CITY || ' ' || u.STREET_ADDRESS1 || ' ' || u.STREET_ADDRESS2 as 전체주소,
    substr(u.TLNO, 1, 3) || '-' || substr(u.TLNO, 4, 4) || '-' || substr(u.TLNO, 8, 4) as 전화번호
    -- c.cnt
    
from
    USED_GOODS_USER u,
    (
    SELECT 
        WRITER_ID,
        count(WRITER_ID) as cnt
    from
        USED_GOODS_BOARD    
    group by
        WRITER_ID
     ) c
where
    c.WRITER_ID = u.USER_ID 
    and c.cnt >= 3
order by 
    c.WRITER_ID DESC
