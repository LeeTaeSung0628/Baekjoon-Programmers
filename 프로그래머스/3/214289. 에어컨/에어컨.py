def solution(temperature, t1, t2, a, b, onboard):
    mintemp, maxtemp = t1, t2
    
    # dp[temp][t] = 시간 t에 실내온도가 (temp+10)도인 
    # 상황을 만드는 최소 소비 전력
    dp = [[1e9] * 51 for _ in range(1001)]
    
    # 초기화 (t=0)
    dp[0][temperature+10] = 0
    
    for t, is_onboard in enumerate(onboard[1:], 1):
        # 승객이 탑승한 상황에서는 오직 mintemp <= temp <= maxtemp
        # 인 경우만 고려하면 된다.
        if is_onboard:
            mintemp_to_consider = mintemp
            maxtemp_to_consider = maxtemp + 1
        else:
            mintemp_to_consider = -10
            maxtemp_to_consider = 40 + 1
            
        for temp in range(mintemp_to_consider, maxtemp_to_consider):
            if temp == temperature:
                candidates = [dp[t-1][temp+10]]
                if temp + 10 != 0:
                    candidates.append(dp[t-1][temp-1+10])
                if temp + 10 != 50:
                    candidates.append(dp[t-1][temp+1+10])
                    
                dp[t][temp+10] = min(candidates)
                
            elif temp > temperature:
                candidates = [dp[t-1][temp+10] + b]
                if temp + 10 != 0:
                    candidates.append(dp[t-1][temp-1+10] + a)
                if temp + 10 != 50:
                    candidates.append(dp[t-1][temp+1+10])
                    
                dp[t][temp+10] = min(candidates)
            else:
                candidates = [dp[t-1][temp+10] + b]
                if temp + 10 != 0:
                    candidates.append(dp[t-1][temp-1+10])
                if temp + 10 != 50:
                    candidates.append(dp[t-1][temp+1+10] + a)
                    
                dp[t][temp+10] = min(candidates)

    answer = min(dp[len(onboard) - 1])
    return answer