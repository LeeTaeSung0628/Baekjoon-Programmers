import java.util.*;

class Solution {
    
    ArrayList<ArrayList<Integer>> gock = new ArrayList<ArrayList<Integer>>(); 
    
    public int solution(int[] picks, String[] minerals) {
        
        /*
            어떠한 곡괭이를 사용할 것인지 모든 조합을 만든다.
        */
        
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        //어레이 초기화
        ArrayList<Integer> ta = new ArrayList<Integer>();
        permu(picks, ta);
        
        //한개의 순열씩 가졍기
        for( ArrayList<Integer> nowPermu : gock){

            int temp = 0;
            
            //현재 곡괭이 순번
            int nowGockNum = 0;
            //남은횟수
            int count = 0;
            
            //순열(곡괭이 종류) 별로 광석 캐기
            for(String nowMine : minerals){
                
                // 현재 곡괭이
                int nowGock = nowPermu.get(nowGockNum);
                if(nowMine.equals("diamond")){
                    if(nowGock == 1) {
                        temp += 1;
                        count += 1;
                    }
                    else if(nowGock == 2) {
                        temp += 5;
                        count += 1;
                    }
                    else if(nowGock == 3) {
                        temp += 25;
                        count += 1;
                    }
                }
                else if(nowMine.equals("iron")){
                    if(nowGock == 1) {
                        temp += 1;
                        count += 1;
                    }
                    else if(nowGock == 2) {
                        temp += 1;
                        count += 1;
                    }
                    else if(nowGock == 3) {
                        temp += 5;
                        count += 1;
                    }
                }
                else if(nowMine.equals("stone")){
                    if(nowGock == 1) {
                        temp += 1;
                        count += 1;
                    }
                    else if(nowGock == 2) {
                        temp += 1;
                        count += 1;
                    }
                    else if(nowGock == 3) {
                        temp += 1;
                        count += 1;
                    } 
                }
                
                //5번 사용했으면 다음꺼
                if(count == 5){
                    nowGockNum += 1;
                    count = 0;
                }
                
                if (nowGockNum >= nowPermu.size()){
                    break;
                }
            }
            
            answer.add(temp);
        }
        
        
        return Collections.min(answer);
    }
    
    public void permu(int[] arro, ArrayList<Integer> res) {
        //깊은복사
        int[] arr = arro.clone();
        
        if (arr[0] != 0){
            ArrayList<Integer> c_res = new ArrayList<Integer>(res);
            //한값 빼준 후에 재호출
            arr[0] -= 1;
            c_res.add(1);
            permu(arr, c_res);
            
            if(arr[0] == 0 && arr[1] == 0 && arr[2] == 0){
                gock.add(c_res);
            }
            
            arr[0] += 1;
        }
        
        if (arr[1] != 0){
            ArrayList<Integer> c_res = new ArrayList<Integer>(res);
            //한값 빼준 후에 재호출
            arr[1] -= 1;
            c_res.add(2);
            permu(arr, c_res);
            
            if(arr[0] == 0 && arr[1] == 0 && arr[2] == 0){
                gock.add(c_res);
            }
            
            arr[1] += 1;
        }
        
        if (arr[2] != 0){
            ArrayList<Integer> c_res = new ArrayList<Integer>(res);
            //한값 빼준 후에 재호출
            arr[2] -= 1;
            c_res.add(3);
            permu(arr, c_res);
            
            if(arr[0] == 0 && arr[1] == 0 && arr[2] == 0){
                gock.add(c_res);
            }
            
            arr[2] += 1;
        }

    }
}