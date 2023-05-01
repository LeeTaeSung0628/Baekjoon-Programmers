"""
아이디어 : 크루스칼 알고리즘 사용 ( 최소신장트리 )
        1. 가장짧은 간선들을 차례대로 구한다 
        2. ex) c[i][j] 라면 i,j를 합집합 리스트에 추가한다.
        3. 간선을 추가할때, i,j가 리스트에 모두 포함되어있으면(사이클이 형성되면) 추가x
        4. 모든 간선을 체크하면 완료
"""

def find(x):
    global root
    
    if root[x] == x: #부모값이 자기자신이면 최상위 노드
        return x
    else:
        return(find(root[x])) #아니라면 부모의 부모 다시 찾기

def union(x, y): # y의 부모값으로 x값(x의 최상위 노드) 삽입 
    global root
    
    x = find(x)
    y = find(y)
    
    if y > x:
        root[y] = x
    else:
        root[x] = y
    
    
root = []
def solution(n, cos):
    global root
    
    cos = sorted(cos, key = lambda x: x[2])
    
    #루트노드를 저장하는 리스트 생성
    for i in range(n):
        root.append(i) #각 요소의 인덱스값은 최상위 루트를 가리킨다.

    
    cnt = 0
    #링크 연결
    for x,y,z in cos:
        fx = find(x) #각각 최상위 부모 탐색
        fy = find(y)
        
        if fx != fy: #부모가 같을경우 합쳐버리면 사이클 발생
            union(x,y)
            cnt+=z
    
        
    print(root)
    
    answer = cnt
    return answer