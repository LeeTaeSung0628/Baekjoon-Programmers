import java.util.*;

class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        
        /*
            t초간 감으면서 1초마다 x만큼 회복
            t초간 붕대를 멈추지 않고 붕대를 감으면 y만큼 추가로 회복한다
            
            시전시간 / 초당회복령 / 추가회복량
            
            최대체력 / [공격시간/피해량]
            
        */
         
        //마지막 공격
        int last_time = attacks[attacks.length-1][0];
        //현재시간 저장
        int nowtime = 0;
        int maxh = health;
        for(int[] a : attacks){
            int atime = a[0]; //공격하는 현재 시간
            int adamege = a[1]; //현재 공격하는 데미지
            
            //공격당할때 까지의 체력회복량을 더해준다.
            int t = (atime - nowtime)-1;//회복한 시간
            health += (bandage[1] * (t)) + (bandage[2] * (t / bandage[0]));
            
            //최대체력보다 크다면 고정
            if(maxh < health){
                health = maxh;
            }
            
            health -= adamege;//공격당함
            nowtime = atime;//시간 갱신
            
            if(health <= 0){
                return -1;
            }
            
        }        
        
        if(health > 0){
            return health;
        }
        else{
            return -1;    
        }
    }
}