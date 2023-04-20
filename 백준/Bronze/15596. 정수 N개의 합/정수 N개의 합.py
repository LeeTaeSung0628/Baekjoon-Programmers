def solve(a: list): 
    if 0 <= len(a) <= 3000000:
        ans = 0 
        for i in a: 
            if 1 <= i <= 1000000:
                ans = ans + int(i) 
    return ans 

a = [1,12,23]

solve(a)

