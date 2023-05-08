import Foundation

func dfs(_ start:[Int], _ finish:[Int], _ count:Int, _ xlim:Int, _ ylim:Int, _ maps:[[String]]) -> Void {
    
    var copyMap:[[String]] = maps //깊은복사
    copyMap[start[0]][start[1]] = "X" 
    let copyCount:Int = count
    
    if start == finish{ //도착했다면
        res.append(copyCount)
    }
    
    //동서남북으로 체크, 가능한곳으로 이동
    let px:[Int] = [0,1,0,-1]
    let py:[Int] = [1,0,-1,0]
    for i in stride(from:0,to:4,by:1){
        let nx:Int = start[0] + px[i]
        let ny:Int = start[1] + py[i]
        
        if nx < xlim && nx >= 0 && ny < ylim && ny >= 0 && copyMap[nx][ny] != "X"{
            var nextCoor:[Int] = [Int]()
            nextCoor.append(nx)
            nextCoor.append(ny)
            dfs(nextCoor,finish,copyCount+1,xlim,ylim,copyMap)
        }
    }
}

func bfs(_ start:[Int], _ finish:[Int], _ count:Int, _ xlim:Int, _ ylim:Int, _ maps:[[String]]) -> Int {    
    var maps:[[String]] = maps
    var q:[[Int]] = [[Int]]()
    var count:Int = count

    q.append(start)
    maps[start[0]][start[1]] = String(count)
    while q.isEmpty == false{        
        let itemx:Int = q[0][0]
        let itemy:Int = q[0][1]    
        
        if q[0] == finish{ //도착체크
            return Int(maps[itemx][itemy])!
        }
        q.removeFirst()
        
        //동서남북으로 체크, 가능한곳으로 이동
        let px:[Int] = [0,1,0,-1]
        let py:[Int] = [1,0,-1,0]
        for i in stride(from:0,to:4,by:1){
            let nx:Int = itemx + px[i]
            let ny:Int = itemy + py[i]

            if nx < xlim && nx >= 0 && ny < ylim && ny >= 0 && ( maps[nx][ny] == "O"
            || maps[nx][ny] == "S" || maps[nx][ny] == "L" || maps[nx][ny] == "E" ){
                maps[nx][ny] = String(Int(maps[itemx][itemy])!+1)
                var nextCoor:[Int] = [Int]()
                nextCoor.append(nx)
                nextCoor.append(ny)
                q.append(nextCoor)
            }
        }
    }
    return -1
}

var res:[Int] = [Int]()

func solution(_ maps:[String]) -> Int {
    
    var stCoor:[Int] = [Int]() //출발지점 좌표
    var lbCoor:[Int] = [Int]() //레버 좌표
    var fiCoor:[Int] = [Int]() //도착지점 좌표
    
    var newMaps:[[String]] = [[String]]()
    //좌표값 추가
    for i in stride(from:0,to:maps.count,by:1){
        let item:[String] = maps[i].map{String($0)}
        newMaps.append(item)
        //print(item)
        for j in stride(from:0,to:item.count,by:1){
            if item[j] == "S"{ stCoor.append(i); stCoor.append(j) }
            else if item[j] == "L"{ lbCoor.append(i); lbCoor.append(j) }
            else if item[j] == "E"{ fiCoor.append(i); fiCoor.append(j) }      
        }
    }
    
   
    let xlim:Int = maps.count
    let yitem:[String] = maps[0].map{String($0)}
    let ylim:Int = yitem.count
    
    /* dfs부분 ( 시간초과 )
    dfs(stCoor,lbCoor,0,xlim,ylim,newMaps)
    if res.isEmpty {
        return -1
    }
    var minV1:Int = res.min() ?? 0
    res = []
    
    dfs(lbCoor,fiCoor,0,xlim,ylim,newMaps)
    if res.isEmpty {
        return -1
    }
    var minV2:Int = res.min() ?? 0
    
    return minV1 + minV2
    */
    let res1:Int = bfs(stCoor,lbCoor,0,xlim,ylim,newMaps)
    if res1 == -1{
        return -1
    }
    let res2:Int = bfs(lbCoor,fiCoor,0,xlim,ylim,newMaps)
    if res2 == -1{
        return -1
    }
    
    return res1+res2
}