import java.util.*;
import java.awt.Point;
class Solution {
    public int[] solution(String[] maps) {
        
        /*
            구역별로 나눠서 모든 값 더하기.
            재방문 금지
        */
        
        int[][] map = new int[maps.length][maps[0].length()];
        
        //숫자로 맵핑
        for(int i=0; i<maps.length; i++){
            for(int j=0; j<maps[0].length(); j++){
                if(maps[i].toCharArray()[j] == 'X'){
                    map[i][j] = -1;
                }else{
                    int c_n = maps[i].toCharArray()[j] - '0';
                    map[i][j] = c_n;
                }
                
            }
        }
        
        ArrayList<Integer> numArr = new ArrayList<Integer>();
        
        //재방문 방지
        boolean[][] visit = new boolean[maps.length][maps[0].length()];
        
        for(int i=0; i<maps.length; i++){
            for(int j=0; j<maps[0].length(); j++){
                if(visit[i][j] == false && map[i][j] != -1){ 
                    numArr.add(search(map, new Point(i,j), visit));
                }
            }
            System.out.println();
        }
        
        if(numArr.size() == 0){
            int[] answer = new int[1];
            answer[0] = -1;
            return answer;
        }else{
             
            int[] answer = new int[numArr.size()];

            for(int i=0; i<numArr.size(); i++){
                answer[i] = numArr.get(i);
            }

            Arrays.sort(answer);
            return answer;
        }
        
        
    }
    
    public int search(int[][] map, Point p, boolean[][] visit){
        
        int[] px = {1,-1,0,0};
        int[] py = {0,0,1,-1};
        
        int cnt = 0;
        
        Queue<Point> q = new LinkedList<Point>();
        
        q.add(p);
    
        while(q.size()>0){
            Point now_p = q.poll();
            visit[now_p.x][now_p.y] = true;
            cnt += map[now_p.x][now_p.y];// 값 증가
               
            for(int i=0; i<4; i++){ // 동서남북 체크
                int nx = now_p.x + px[i];
                int ny = now_p.y + py[i];
                
                if(0<=nx&&nx<map.length && 0<=ny&&ny<map[0].length// 벽이 아닌지
                  && map[nx][ny] != -1  // X가 아닌지
                  && visit[nx][ny] == false //다시 방문하는 곳이 아닌자
                  ){ 
                    q.add(new Point(nx,ny));
                    visit[nx][ny] = true; 
                }
            }
        }
        
        return cnt;
    }
}