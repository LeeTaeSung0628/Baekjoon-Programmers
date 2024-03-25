
select 
    '/home/grep/src/' || f.board_id || '/' || f.FILE_ID || f.FILE_NAME || f.FILE_EXT
    as FILE_PATH
from 
    USED_GOODS_FILE f,
    (
    select * 
    from USED_GOODS_BOARD a
    where a.VIEWS = (select max(VIEWS) from USED_GOODS_BOARD)
    ) m
where
    f.BOARD_ID = m.BOARD_ID
order by
    f.FILE_ID DESC
 

