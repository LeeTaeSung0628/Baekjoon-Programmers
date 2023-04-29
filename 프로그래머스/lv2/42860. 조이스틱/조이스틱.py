"""
아이디어 : length // 2 < (찾고자하는값) 
         이라면, length - (찾고자하는값)이 해다.
"""
import copy

res = []
def dfs(me,name,cnt):
    check = True
    c_name = copy.deepcopy(name)
    c_name[me] = "A"

    for i in range(len(name)):
        if c_name[i] != "A":
            check = False
            dfs(i,c_name,cnt+min(abs(i-me),len(name)-i+me,abs(len(name)-me+i)))
    
    if check == True: #방문할게 더이상 없다면
        #print(cnt)
        res.append(cnt)
    
def solution(name):
    
    abc = [] #알파뱃의 아스키코드를 저장 (abc[0] : A ... abc[25] : Z)
    a=65
    for i in range(26):
        abc.append(a)
        a+=1
        
    total = 0 #총이동횟수    
    
    #알파뱃을 변경하는 횟수
    for i in range(len(name)):
        if name[i] != "A":
            nal = ord(name[i])-65 #바꿔야 하는 이름에 대한 위치값 (nal=A : 0 / nal=B : 1)
            if len(abc) // 2 < nal: #거꾸로가 빠른경우
                total += len(abc) - nal
            else: #정방향이 빠른경우
                total += nal
                
    
    
    #check = [False] * len(name)
    meplac = 0 #자신의 위치 
    name = list(name)
    cnt=0
    dfs(meplac,name,cnt)
    
    #print("총길이 : ",len(res))
    minv = 99999
    for i in res:
        minv = min(minv,i)
        
    total+=minv
    
    answer = total
    return answer