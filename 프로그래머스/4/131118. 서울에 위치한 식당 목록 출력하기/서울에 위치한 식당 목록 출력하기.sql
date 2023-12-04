

-- 코드를 입력하세요
SELECT A.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) SCORE 
FROM REST_INFO A RIGHT JOIN REST_REVIEW B
ON A.REST_ID = B.REST_ID
WHERE ADDRESS LIKE '서울%'
GROUP BY A.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC