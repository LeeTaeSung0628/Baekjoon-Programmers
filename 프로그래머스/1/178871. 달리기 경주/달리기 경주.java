import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        
        //인원의 순위를 기록하는 해쉬맵 생성
        Map<String, Integer> dic = new HashMap<>();
        
        for(int i=0; i<players.length; i++){
            dic.put(players[i],i);
        }

        
        //순위 변경
        for(String call : callings){
            
            // 지금 불려진 선수의 위치
            int now = dic.get(call);
            
            //내 인덱스 변경
            dic.put(call, now-1);
                
            //추월한 녀석 인덱스 변경
            dic.put(players[now-1], now);
            
            // 자리변경
            String temp = players[now];
            players[now] = players[now-1];
            players[now-1] = temp;
            
        } 
        
        
        return players;
    }
}