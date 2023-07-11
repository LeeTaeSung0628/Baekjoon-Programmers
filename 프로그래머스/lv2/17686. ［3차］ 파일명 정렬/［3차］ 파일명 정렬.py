def solution(files):
    
    tf = []
    number = ['0','1','2','3','4','5','6','7','8','9']
    
    for item in files:
        head = ""
        num = ""
        tale = ""
        size = 0
        headCheck = True
        numberCheck = True
        for cha in item:
            #헤드 잘라내기
            if headCheck:
                if cha not in number:
                    head += cha
                else:
                    headCheck = False #넘버값이 나오는 순간 헤드는 끝!
                    
            #넘버값 잘라내기
            if headCheck == False and numberCheck:
                if cha in number and size <= 5:
                    num += cha
                    size += 1
                else:
                    numberCheck = False #넘버값이 나오는 순간 헤드는 끝!
                        
            #마지막 값들
            if headCheck == False and numberCheck == False:
                tale += cha
            
        tf.append([head,num,tale])
    
    tf = sorted(tf, key = lambda x : (x[0].lower(),int(x[1])))
        
    answer = []
    
    for item in tf:
        answer.append("".join(item))
    
    return answer