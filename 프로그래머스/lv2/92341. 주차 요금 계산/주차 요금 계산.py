import math

def solution(fees, recod):
    
    """
    1. 객체 생성
    2. records 배열 순회하면서 시간을 분으로 바꾼 뒤, 생성한 객체에 key로 시간, 차 번호, inout 타입, 마지막으로 들어온 시간을 넣어주며 계속적으로 계산.
    3. 값이 들어간 객체를 순회하며 타입이 IN일때, 누적시간이 기본시간을 넘기지 않았을 때를 각가 구하고 나머지 조건에 대해서는 반올림을 하여 구해준다.
    """
    car_dic = {}
    
    #처음처리
    for item in recod:
        t,num,io = item.split()
        hour,minute = list(map(int,t.split(":")))
        time = (hour * 60) + minute
        
        if io == "IN": 
            if num in car_dic:
                car_dic[num] = [car_dic[num][0],int(num),io,time]
            else:
                car_dic[num] = [0,int(num),io,time]
        else:
            car_dic[num] = [(car_dic[num][0] + (time-car_dic[num][3])),int(num),io,time]
    
    #입차상태인 애들 처리
    for item in car_dic:
        time_sum= car_dic[item][0]#누적합
        num = car_dic[item][1]#번호
        io = car_dic[item][2]#i/o 상태
        time = car_dic[item][3]#입차시간
        
        if io == "IN":
            car_dic[item] = [time_sum + ( (23*60+59) - time), int(num),"oooo",time]
        
    ans = []
    print(car_dic)
    for item in car_dic:
        time_sum = car_dic[item][0]#누적합
        num = car_dic[item][1] #인트형 번호
        ans.append([num,time_sum])
    
    ans = sorted(ans, key = lambda x: x[0])
    
    d_time = fees[0] #기본시간
    d_pay = fees[1] #기본요금
    p_time = fees[2] #단위시간
    p_pay = fees[3] #단위요금
    
    answer = []
    for item in ans:
        if item[1] <= d_time:
            answer.append(d_pay)
        else:
            total = d_pay + ( math.ceil((item[1]-d_time) / p_time) * p_pay)
            answer.append(total)
        
    return answer
