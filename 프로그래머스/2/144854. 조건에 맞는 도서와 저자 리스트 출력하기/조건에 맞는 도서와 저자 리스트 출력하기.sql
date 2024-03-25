-- 코드를 입력하세요
SELECT
    b.book_id,
    a.AUTHOR_NAME,
date_format(b.PUBLISHED_DATE,'%Y-%m-%d')
from
    book b,
    AUTHOR a
where
    b.AUTHOR_ID = a.AUTHOR_ID
    and b.category = '경제'
order by PUBLISHED_DATE
