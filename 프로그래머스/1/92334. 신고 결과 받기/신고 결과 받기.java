import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        /*
            1. 인원별 딕셔너리를 2개 생성한다
            2. 1번째 의 딕셔너리에는 신고 당한 횟수를 저장한다.
            3. 2번째 딕셔너리에는 "muzi frodo" (신고자, 당한자)를 저장하여 이미 신고했는지를 판단한다.
            4. id_list와 순서와 크기가 같은 배열을 생성하여, 신고한 명단을 String으로 저장한다.
            5. 1번 딕셔너리에서 k보다 많이 신고당한 사람들이 포함된 배열을 만든 후, 4번 배열과 비교하여 메일 개수를 판단한다.
        */

        Map<String, Integer> dict1 = new HashMap<>();
        Map<String, Integer> dict2 = new HashMap<>();
        ArrayList<String>[] arr = new ArrayList[id_list.length];
        
        //2차원 배열로 생성
         for(int i=0; i<id_list.length;i++) {
             arr[i]=new ArrayList<String>(); //배열 원소를 인스턴스로 지정한다
         } 
        
        //dict1에 신고당한 횟수 초기화
        for(String s : id_list){
            dict1.put(s,0);
        }
        
        //신고처리
        for(String s : report){
            //sr[0] 신고자 / sr[1] 당한자
            String[] sr = s.split(" ");
            
            // 이미 신고했는지 처리
            if(!dict2.containsKey(s)){
                //신고당한 횟수 처리
                dict1.put(sr[1], (dict1.get(sr[1])+1));
                //재신고여부 처리
                dict2.put(s, 1);
                
                //id_list 인덱스
                int index = Arrays.asList(id_list).indexOf(sr[0]);
                
                arr[index].add(sr[1]);
            }
            
        }
        
        //정답
        int[] result = new int[id_list.length];
        
        for(int i=0;i<id_list.length;i++){
            
            for(int j=0;j<arr[i].size();j++){
                if(dict1.get(arr[i].get(j)) >= k){
                    result[i] += 1;
                }
            }
        }
        
        return result;
    }
}