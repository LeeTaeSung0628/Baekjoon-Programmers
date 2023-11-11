import java.util.*;

class Node implements Comparable<Node>{
    int dist;
    int node;
    
    public Node(int dist, int node){
        this.dist = dist;
        this.node = node;
    }
    
    @Override
    public int compareTo(Node other){
        return Integer.compare(this.dist, other.dist);
    }
}

class Solution {
    public int solution(int N, int[][] road, int K) {
    
    
        /*
            1번 마을에서 다른마을까지의 최단거리 알아내기
        */
        
        //갈 수 있는 마을과, 해당마을까지의 거리 배열 저장
        ArrayList<Node>[] map = new ArrayList[N];
        
        //초기화
        for(int i=0; i<N; i++){
            map[i] = new ArrayList<Node>();
        }
        
        for(int[] line: road){
            int st = line[0];
            int en = line[1];
            int dist = line[2];
            
            map[st-1].add(new Node(dist,en-1));
            map[en-1].add(new Node(dist,st-1));
        }
        
        //각 마을까지의 거리
        int[] distArr = new int[N];
        for(int i=0; i<N; i++){
            distArr[i] = 999999;
        }
        
        //시작지점 삽입
        PriorityQueue<Node> q = new PriorityQueue<Node>();
        q.add(new Node(0,0));
        
        while(q.size()>0){
            
            Node nowNode = q.poll();
            
            //방문후, 거리가 더 짧다면 덮어쓰기
            if(distArr[nowNode.node] > nowNode.dist){
                distArr[nowNode.node] = nowNode.dist;
                
                //다음 방문할 수 있는 점 큐에 삽입
                for(Node nextNode : map[nowNode.node]){
                    q.add(new Node(nowNode.dist + nextNode.dist, nextNode.node));
                }
            }     
        }
        
        int answer = 0;
        
        for(int i=0; i<distArr.length; i++){
            
            if(distArr[i] <= K){
                answer++;
            }
        }
        
        return answer;
    }
}