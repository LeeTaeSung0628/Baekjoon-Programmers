import Foundation

func solution(_ storey:Int) -> Int {
    var result = 0
    var storey = "\(storey)".map{Int(String($0))!}
    
    while storey.filter{$0 == 0}.count != storey.count {    // storey가 모두 0일 떄까지
        // storey 맨 오른쪽부터 0이 아닌 위치를 찾는다
        var idx = storey.count - 1
        while storey[idx] == 0 && idx > 0 {
            idx -= 1
        }
        if storey[idx] > 5 {    // 찾은 수가 5보다 크다면
            result += 10-storey[idx]    // (10-찾은 수)를 result에 추가
            storey[idx] = 0 // 해당 위치를 계산하였으므로 0으로 설정
            if idx > 0 {    // 맨 왼쪽 자리가 아닐 경우
                storey[idx-1] += 1  // 찾은 수에서 자릿수가 넘어가서 0이 되었으니 찾은 수의 앞 자리 수 증가 
            }
            else {
                storey.insert(1, at: 0) // 맨 왼쪽 자리인 경우에서 자릿수가 넘어갔으니 1 추가
            }
        }
        else if storey[idx] < 5 {   // 찾은 수가 5보다 작다면
            result += storey[idx]   // result에 추가
            storey[idx] = 0 // 해당 위치를 계산하였으므로 0으로 설정
        }
        else {  // 찾은 수가 5라면 찾은 수의 앞 자리 수를 조건에 따라 비교해야한다
            if idx-1 > 0 {
                if storey[idx-1] >= 5 {
                    result += 10-storey[idx]
                    storey[idx] = 0
                    storey[idx-1] += 1                
                }
                else {
                    result += storey[idx]
                    storey[idx] = 0
                }
            }
            else {
                result += 5
                storey[idx] = 0
            }
        }
    }
    return result
}