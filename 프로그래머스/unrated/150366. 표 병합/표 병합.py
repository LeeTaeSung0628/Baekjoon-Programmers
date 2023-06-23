def check_mom(rc,maps): #연결되있는 원본 판의 값을 리턴
    r,c = rc
    if maps[r][c][1] == 1: #부모가 있으면
        return(check_mom([maps[r][c][0][0],maps[r][c][0][1]],maps))
    else: 
        return rc
    
def solution(com):
    
    maps = [ [["",0] for _ in range(50)]  for _ in range(50)]
    
    ans = []
    for item in com:
        c = list(item.split())
        #데이터형태 ( "글자", 0 ) , ( [1,3] , 1 )
        if c[0] == "UPDATE" and len(c) == 4:
            p = check_mom([int(c[1])-1,int(c[2])-1],maps) #최상위노드 찾기
            maps[p[0]][p[1]][0] = c[3]
            
        elif c[0] == "UPDATE" and len(c) == 3:
            for i in range(len(maps)):
                for j in range(len(maps[0])): 
                    if maps[i][j][1] == 0: #원본배열이라면
                        if maps[i][j][0] == c[1]:
                             maps[i][j][0] = c[2]
            
        elif c[0] == "MERGE":
            p = check_mom([int(c[1])-1,int(c[2])-1],maps)#최상위 연결체크
            p2 = check_mom([int(c[3])-1,int(c[4])-1],maps)#최상위 연결체크
            
            if p == p2: continue #같은것을 머지하면 무시
            
            if len(maps[p[0]][p[1]][0]) == 0 : #원본이 비었으면
                maps[p[0]][p[1]][0] = maps[p2[0]][p2[1]][0] # 값 삽입
                
            maps[p2[0]][p2[1]][1] = 1 #연결
            maps[p2[0]][p2[1]][0] = [p[0],p[1]]
            

                
        elif c[0] == "UNMERGE":
            #언 머지할 좌표가 원본인지, 포함인지 체크
            if maps[int(c[1])-1][int(c[2])-1][1] == 0:#원본이면
                #해당 자식들 모두 삭제
                rm_arr = []
                for i in range(len(maps)):
                    for j in range(len(maps[0])):
                        if maps[i][j][1] == 1: #포함배열일때
                            p = check_mom([i,j],maps)#해당칸의 부모배열 찾기
                            if [int(c[1])-1 ,int(c[2])-1] == p: #내부모와 삭제할 부모가 같다면
                                rm_arr.append([i,j]) #해당칸 삭제
                #삭제할 칸들 삭제
                print(rm_arr)
                for r in rm_arr:
                    i,j = r
                    maps[i][j][1] = 0 #해당칸 삭제
                    maps[i][j][0] = ""

            else: # 언 머지 할 좌표가 포함배열이라면
                #1. 원본값 알아내서 저장
                r = check_mom([int(c[1])-1,int(c[2])-1],maps)#삭제할 부모배열
                orgText = maps[r[0]][r[1]][0]
                #2. 원본 삭제
                maps[r[0]][r[1]][0] = ""
                maps[r[0]][r[1]][1] = 0
                #3. 원본을 포함하고있는 배열들 삭제   
                rm_arr = []
                for i in range(len(maps)):
                    for j in range(len(maps[0])):
                        if maps[i][j][1] == 1: #포함배열일때
                            p = check_mom([i,j],maps)#해당칸의 부모배열 찾기
                            if r == p: #내부모와 삭제할 배열이 같다면
                                rm_arr.append([i,j]) #해당칸 삭제
                 #삭제할 칸들 삭제
                print(rm_arr)
                for r in rm_arr:
                    i,j = r
                    maps[i][j][1] = 0 #해당칸 삭제
                    maps[i][j][0] = ""
                    
                maps[int(c[1])-1][int(c[2])-1][0] = orgText
                maps[int(c[1])-1][int(c[2])-1][1] = 0
                
                                
        elif c[0] == "PRINT":
            p = check_mom([int(c[1])-1,int(c[2])-1],maps)#최상위 노드 찾기
            if maps[p[0]][p[1]][0] == "" : a = "EMPTY"
            else: a = maps[p[0]][p[1]][0]
            ans.append(a)
            
        
    answer = ans
    return answer
