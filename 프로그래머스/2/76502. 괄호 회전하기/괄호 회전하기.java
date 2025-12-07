import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        HashMap<Character, Character> map = new HashMap<>();
        
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');
       
        int length = s.length();
         s += s;
        
        A:for(int i=0; i<length; i++) {
            ArrayDeque<Character> stack = new ArrayDeque<>();
            for(int j = i; j< i+length; j++) {
                char c = s.charAt(j);
                if(!map.containsKey(c)) {
                    stack.push(c);
                } else if(stack.isEmpty() || !stack.pop().equals(map.get(c))){
                    continue A;
                }
            }
            if(stack.isEmpty()) {
                answer += 1;
            }
        }
       
        return answer;
    }
}