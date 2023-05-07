import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var numbers:[Int] = numbers
    var maxv:Int = numbers[numbers.count-1] //지정수
    var res:[Int] = Array(repeating : -1,count:numbers.count)
    
    var i:Int = numbers.count-2
    while i >= 0 {
        if numbers[i] >= maxv{
            maxv = numbers[i]
            i-=1
        }
        else{
            for j in stride(from:i+1,to:numbers.count,by:1){
                if numbers[i] < numbers[j]{
                    res[i] = numbers[j]
                    i-=1
                    break
                }
                if numbers[i] <= numbers[j] && numbers[i] < res[j]{
                    res[i] = res[j]
                    i-=1
                    break
                }
            }
        }   
    }
    
    return res
}