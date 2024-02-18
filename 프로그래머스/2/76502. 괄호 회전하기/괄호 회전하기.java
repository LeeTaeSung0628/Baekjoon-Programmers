import java.util.Stack;

class Solution {
    
    public boolean isCorect(String s){
        
            //괄호를 열을때 스텍에 추가, 닫으면 닫는 괄호와 일치하는지 체크 후 삭제. 
            //1. 최종으로 스텍에 값이 남아있으면 오류
            //2. 스텍에 값이 없는데 닫으면 오류
            //3. 일치하지않는 값이 닫히면 오류
        
        boolean check = true;
        
        //길이가 1인경우 예외처리
        if(s.length() == 1){
            return false;
        }
        
        Stack<Character> stackStr = new Stack<>();
        
        for(int i=0;i<s.length();i++){
            
            char now = s.charAt(i);
            
            // 여는 괄호면 스텍에 추가
            if(now == '[' || now == '{' || now == '('){
                stackStr.push(now);
                continue;
            }
            //아니라면 스텍이 비어있는지 확인(예외처리)
            else{
                if(stackStr.isEmpty()){
                    return false;
                }
            }
            
            //비교할 괄호 꺼내기
            char next = stackStr.pop();
                
            if(now == ']' && next != '['){
                return false;
            }
            else if(now == '}' && next != '{'){
                return false;
            }
            else if(now == ')' && next != '('){
                return false;
            }
            
        }
        
        //최종 스텍에 값이 남아있는경우 예외처리
        if(stackStr.size() > 0){
            return false;
        }
        
        return check;
    }
    
    public int solution(String s) {
        
        int cnt = 0;
        
        //회전시킨 모든 경우의 수를 대입후 올바른 경우 cnt
        for(int i=0;i<s.length();i++){
            s = s.substring(1) + s.substring(0,1);
            if(isCorect(s)){
                cnt += 1;
            }
        }
        
        // isCorect(s);
        
        return cnt;
    }
}