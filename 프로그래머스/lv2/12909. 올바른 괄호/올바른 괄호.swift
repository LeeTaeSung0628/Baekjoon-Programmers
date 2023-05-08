import Foundation

func solution(_ s:String) -> Bool
{
    var ans:Bool = false
    var sList:[String] = s.map{String($0)}
    var stack:[String] = [String]()
    
    for item in s{
        if item == "("{
            stack.append("\(item)")
        }
        else{
            if stack.isEmpty{
                return false
            }
            else{
                var save:String = stack[stack.count-1]
                stack.removeLast()
            }
        }
    }
    if stack.isEmpty{return true}
    else{return false}
    
}