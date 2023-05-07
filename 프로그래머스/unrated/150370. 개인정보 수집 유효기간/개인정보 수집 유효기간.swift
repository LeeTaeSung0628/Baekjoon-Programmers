import Foundation

func solution(_ today:String, _ terms:[String], _ privacies:[String]) -> [Int] {
    
    var termDic: [String:Int] = [:]
    var res:[Int] = [Int]()
    
    // terms 배열 잘라서 딕셔너리로 저장하기
    for i in stride(from:0,to:terms.count,by:1){
        var oIndex = terms[i].index(terms[i].startIndex, offsetBy : 1)
        var tIndex = terms[i].index(terms[i].startIndex, offsetBy : 2)
        var oVal = terms[i][..<oIndex] // 첫 번째 문자를 추출
        var tVal = terms[i][tIndex...] // 두 번째 문자부터 뒤 부터 마지막 문자까지 추출
        termDic.updateValue(Int(tVal) ?? 0,forKey:String(oVal))  // ?? 0 => 값이 nil 이면 0 반환
    }
    print("약관별 유효기간 : ",termDic)
    
    // today 잘라서 배열로 저장
    var sliceToday:[Substring] = today.split(separator:".")
    print("현제 날짜 : ",sliceToday)
    
    //privacies 잘라서 배열로 저장
    var priList:[[String]] = [[String]]() // privacies를 저장할 리스트
    var i:Int = 0 // 인덱스
    for p in privacies {
        i+=1
        var sliceP:[Substring] = p.split(separator:" ") // 스플릿 연산은 subString형태로 반환한다.
        var dayP:String = String(sliceP[0])
        var kindP:String = String(sliceP[1])
        priList.append([String(i),dayP,kindP])
    }
    
    print("개인정보 리스트 - ")
    for item in priList {
        var limit:Int = termDic[item[2]] ?? 0
        var sliceDayP:[Substring] = item[1].split(separator:".")
        var dayList:[Int] = [Int]()
        dayList.append(Int(sliceDayP[0]) ?? 0)
        dayList.append(Int(sliceDayP[1]) ?? 0)
        dayList.append(Int(sliceDayP[2]) ?? 0)
        
        let sumMon:Int = dayList[1] + limit
        let yea:Int = Int(sumMon / 12) //초과된 수(년도)
        var mon:Int = sumMon % 12 //버리고 나머지 달
        dayList[0] += yea
        dayList[1] = mon
        dayList[2] -= 1
        
        if dayList[1] == 0 { //2002년 0월 일경우 2001년 12월
            dayList[1] = 12
            dayList[0] -= 1
        }
        if dayList[2] == 0 { //12월 0일 일경우  11월 28일로
            dayList[2] = 28
            dayList[1] -= 1
        }

        print("변경후",dayList)
        
        var toDayList:[Int] = [Int]()
        toDayList.append(Int(sliceToday[0]) ?? 0)
        toDayList.append(Int(sliceToday[1]) ?? 0)
        toDayList.append(Int(sliceToday[2]) ?? 0)
        
        if dayList[0] < toDayList[0] {
            res.append(Int(item[0]) ?? 0)
        }
        else if dayList[0] == toDayList[0] {
            if dayList[1] < toDayList[1] {
                res.append(Int(item[0]) ?? 0)
            }
            else if dayList[1] == toDayList[1] {
                if dayList[2] < toDayList[2] {
                    res.append(Int(item[0]) ?? 0)
                }
            }
        }
        
    }
    
    return res
}