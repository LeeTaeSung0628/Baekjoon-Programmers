import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Arrays;
import java.awt.Point;
import java.util.Queue;

class Solution{
    
    //해당 인덱스와 연결되어있는 노드번호를 저장하는 배열
    public ArrayList<Integer>[] arr;
    //깊이와 노드를 저장하는 배열
    public ArrayList<int[]> ans = new ArrayList<int[]>();
    
    public int bfs(int deps, boolean[] visit){
        
        Queue<Point> q = new LinkedList<>(); //int형
        q.offer(new Point(0,0));
        //방문처리
        visit[0] = true;
        
        while(!q.isEmpty()){
            Point nodeInfo = q.poll();
            int now = nodeInfo.x;
            int now_deps = nodeInfo.y;
            
            
            // System.out.println(now+1+","+now_deps);
            int[] temp = {now+1,now_deps};
            ans.add(temp);
            
            for(int i=0; i<arr[now].size(); i++){
                int next = arr[now].get(i);
                //아직 방문하지 않은 녀석만 삽입
                if(visit[next-1] == false){
                    q.offer(new Point(next-1,now_deps+1));
                    visit[next-1] = true;
                }
            }
        }

        return arr.length;
    }
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        arr = new ArrayList[n];
        
        //2차원 배열로 생성
         for(int i=0; i<n;i++) {
             arr[i]=new ArrayList<Integer>(); //배열 원소를 인스턴스로 지정한다
         } 
        //노드 맵핑
        for(int[] i : edge){
            arr[i[0]-1].add(i[1]);
            arr[i[1]-1].add(i[0]);
        }
        
        // 방문확인
        boolean[] visit = new boolean[n];
        Arrays.fill(visit,false);
        bfs(0,visit);
        
        
        //개수 세기
        int maxv = 0;
        int cnt = 0;
        for(int[] i : ans){
            cnt += 1;
            if(maxv < i[1]){
                cnt = 1;
                maxv = i[1];
            }
        }
        // System.out.println(cnt);

        return cnt;
    }
    
}