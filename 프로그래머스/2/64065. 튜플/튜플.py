def solution(s):
    
    
    dic = {}
    ans = []
    ss = s[2:-2].split("},{")
                      
    for item in ss:
        arr = item.split(",")
        
        for i in range(len(arr)):
            if arr[i] in dic:
                dic[arr[i]] += 1
            else:
                dic[arr[i]] = 1
    
    
    for item in dic:
        ans.append([int(item),dic[item]])
        
    ans = sorted(ans, key = lambda x : -x[1])
    
    anss = []
    for item in ans:
        anss.append(item[0])
            
    return anss