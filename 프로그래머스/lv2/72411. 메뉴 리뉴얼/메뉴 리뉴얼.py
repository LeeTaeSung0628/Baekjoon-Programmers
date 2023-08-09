"""
 1. 오름차 순으로 정렬한다
 2. 각 메뉴 별 조합을 만든다
 3. 각각 조합이 자신을 제외한 다른 메뉴 조합에 포함되는지 확인한다
"""
from itertools import combinations, permutations


def solution(orders, course):
    
    N = len(orders)
    answer = []
    for item in course:

        #메뉴별 조합 만들기
        menu_com = [[] for _ in range(N)]
        for i in range(len(orders)):

            now_menu = list(orders[i])
            now_menu.sort()
            menu_com[i] = list(combinations(now_menu,item))

        #각 조합을 합친후, 배열에 2개 이상 존재하면 append
        check_dic = {} 
        for i in range(N):
            for item in menu_com[i]:
                now_menu = "".join(item)
                #이미 존재하면
                if now_menu in check_dic:
                    check_dic[now_menu] += 1
                else:
                    check_dic[now_menu] = 1

        #배열로 만들어 준 후 정렬
        temp = []
        for item in check_dic:
            temp.append([check_dic[item], item])
        temp = sorted(temp, key = lambda x:-x[0])

        ans = []
        maxv = 0
        for i in range(len(temp)):
            if i == 0:
                if temp[i][0] > 1:
                    maxv = temp[i][0]
                    ans.append(temp[i][1])
                continue
            else:
                #최대값이 아니면
                if maxv == temp[i][0]:
                    ans.append(temp[i][1])
                else:
                    break

        answer += ans
    answer.sort()
    return answer