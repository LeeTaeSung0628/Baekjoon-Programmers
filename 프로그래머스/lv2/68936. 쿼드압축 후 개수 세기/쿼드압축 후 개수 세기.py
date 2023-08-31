def solution(arr):
    global answer
    answer = [0, 0]
    quad(arr, answer, len(arr))
    return answer

def quad(arr, s, n):
    x, y, tg = s[0], s[1], arr[s[0]][s[1]]
    for i in range(n):
        for j in range(n):
            if arr[x+i][y+j] != tg:
                quad(arr, [x, y], n//2)
                quad(arr, [x, y+n//2], n//2)
                quad(arr, [x+n//2, y], n//2)
                quad(arr, [x+n//2, y+n//2], n//2)
                return
    answer[tg] += 1