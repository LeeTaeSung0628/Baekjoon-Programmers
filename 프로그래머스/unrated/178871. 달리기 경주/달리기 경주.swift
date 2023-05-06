import Foundation

func solution1(_ pl:[String], _ call:[String]) -> [String] { //리스트를 사용한 방법
    
    var pl:[String] = pl
    let call:[String] = call
    
    for item in call {
        let index:Int? = pl.firstIndex(of:item) as? Int
        var temp:String = ""
        
        temp = pl[index!-1]
        pl[index!-1] = pl[index!]
        pl[index!] = temp
    } 
        
    return pl
}

func solution(_ pl:[String], _ call:[String]) -> [String] { //딕셔너리를 사용한 방법
    
    var pl:[String] = pl
    let call:[String] = call
    
    var plDic:[String:Int] = [:]
    
    for i in stride(from:0, to:pl.count, by:1) {
        plDic.updateValue(i, forKey : pl[i])
    }
    
    for item in call {
        let me:Int = plDic[item]! //내값
        let pre:Int = plDic[item]!-1 //바꿀값
        plDic.updateValue(pre, forKey : pl[me])
        plDic.updateValue(me, forKey : pl[pre])
        
        pl.swapAt(pre,me)
        /* var temp:String = ""
           temp = pl[pre]
           pl[pre] = pl[me]
         pl[me] = temp */
    }
   
        
    return pl
}