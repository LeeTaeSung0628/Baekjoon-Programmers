import Foundation

var lRes:[[Int]] = [[Int]]() //부분배열의 배열
func permutation(_ disArr:[Int], _ chk:[Bool], _ sRes:[Int], _ cnt:Int) -> Void {
    var chkCopy:[Bool] = chk
    var sResCopy:[Int] = sRes //부분배열
    if sResCopy.count >= cnt{ //전부 방문했으면
        lRes.append(sResCopy)
    }
    else{
        for i in 0..<disArr.count{
            sResCopy.append(disArr[i])
            permutation(disArr,chkCopy,sResCopy,cnt)
            sResCopy.removeLast()
        }
    }
}

func solution(_ user:[[Int]], _ emot:[Int]) -> [Int] {
    
    let disArr:[Int] = [10,20,30,40]
    var chk:[Bool] = Array(repeating:false , count:disArr.count)
    var sRes:[Int] = [Int]() //부분배열
    var cnt:Int = emot.count
    permutation(disArr,chk,sRes,cnt)
    
    
    var res:[[Int]] = [[Int]]() // 플러스맵버쉽 구입한 사람 수/구입한 금액의 배열
    for item in lRes{ // 모든할인율 경우의수 
        var emList:[[Int]] = [[Int]]() //각 할인율의 배열
        for i in 0..<item.count{  //각 할인율의 (할인율/가격/할인된가격) 배열 생성
            emList.append([item[i],emot[i],emot[i] - Int(Float(emot[i])*(Float(item[i])/100))])
        }
        
        var pSum:Int = 0 // 플러스 사용자
        var mSum:Int = 0 // 총금액
        for us in 0..<user.count{ //사람마다 , 해당이모티콘(em)이 사용가능한지 체크
            var mo:Int = user[us][1] //개인별 금액마지노선
            var ex_su:Int = 0 //중간집계가격
            
            for em in 0..<emList.count{ 
                //user[us][0] : 할인율 마지노선
                //mo : 갖고있는 금액 마지노선
                //ex_su : 중간집계
                //emList[em][0] : 할인율
                //emList[em][2] : 할인된가격
                if user[us][0] <= emList[em][0]{ //구입할 수 있다.
                    mo-=emList[em][2] // 할인된 가격만큼 금액 마지노선에서 빼준다.
                    ex_su+=emList[em][2]
                }
            } //이모티콘 전부 탐색 후,
            if mo <= 0{ pSum+=1 } //금액의 마지노선을 넘었다면 (플러스가입자)
            else{ mSum+=ex_su } //넘지 못했따면 ( 현금사용자 )
        }
        //하나의 경우의 수를 탐색했다면
        res.append([pSum,mSum])
    }
    res = res.sorted(by: { ($0[0],$0[1]) > ($1[0],$1[1]) })
    print(res[0])
    
    return res[0]
}