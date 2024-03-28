import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        
        Set<String> set = new HashSet<String>();
        String befor = "";
        
        int cnt = 1;
        for(String item : words){
            
            //중복확인
            if(set.contains(item)){
                // System.out.println(cnt);
                break;
            }
            
            //이전값 확인
            if(befor.length() > 0){
                if(befor.charAt(befor.length()-1) != item.charAt(0)){
                    // System.out.println(cnt);
                    break;
                }
            }
            
            befor = item;
            set.add(item);
            
            cnt += 1;
            
        }
        
        int[] answer = {0,0};
        
        System.out.println("카운트 : " + cnt);
    
        if(cnt == words.length + 1){
            System.out.println("없음");
        }
        else{
            if(cnt%n == 0){
                System.out.println(n + " " + (cnt/n) + " 나누어떨어짐");
                answer[0] = n;
                answer[1] = cnt/n;
            }else{
                System.out.println(cnt % n + " " + ((cnt/n) + 1) + " 남음");
                answer[0] = cnt % n;
                answer[1] = (cnt/n) +1;
            }    
        }
        
        
        // 몇번 사람이 걸렸는지

        return answer;
    }
}