def binary_search(target, data): #해당스코어 이상인 지점을 찾는 함수
    start = 0
    end = len(data) - 1
    mid = 0
    while start <= end:
        mid = (start + end) // 2

        #if data[mid] == target:
        #    return mid #중복값이 있을수 있으므로, 해당 수의 개수를 세야한다.
        if data[mid] < target:
            start = mid + 1
        else:
            end = mid -1     

    #찾은값이 타겟보다 크면
    if data[mid] < target:#찾은값이 타겟보다 작으면
        return mid+1# 그이상인 값 출력(만약 arr길이를 넘어가면 없는것)
    else: #찾은값이 타겟 이상이면
        return mid #중간값이 타겟 이상이므로 출력
    

def solution(info, query):
    
    answer = []
    
    #특정한 사람 배열
    person = {}
    
    #사람 생성
    for item in info:
        a,b,c,d,num = list(item.split())
        a = a[0]
        b = b[0]
        c = c[0]
        d = d[0]
        num = int(num)
        sum_string = a+b+c+d
        
        if sum_string in person:
            person[sum_string].append(num)
            
        else: #없으면 새로 생성
            person[sum_string] = [num]
    
    #사람들 점수 정렬하기
    for item in person:
        person[item].sort()
    
    #인재 체크
    for item in query:
        a,b,c,dd = list(item.split(" and "))
        a = a[0]
        b = b[0]
        c = c[0]
        dd = dd
        d, num= list(dd.split())
        d = d[0]    
        num = int(num)
        if a == "-":
            a = ["c","j","p"]
        if b == "-":
            b = ["b","f"]
        if c == "-":
            c = ["j","s"]
        if d == "-":
            d = ["c","p"]
        
        sum_string = []
        for aaa in range(len(a)):
            for bbb in range(len(b)):
                for ccc in range(len(c)):
                    for ddd in range(len(d)):
                        sum_string.append(a[aaa]+b[bbb]+c[ccc]+d[ddd])
        #조건충족하는사람 더하기
        cnt = 0
        
        for i in range(len(sum_string)):
            name = sum_string[i] #각각 모든 구릅이름
            if name in person: #해당하는 구룹이 있다면
                iss = binary_search(num,person[name]) #몇번째 인덱스부터 num이상값이 나오는지

                cnt += len(person[name]) - iss

        answer.append(cnt)
        
    return answer