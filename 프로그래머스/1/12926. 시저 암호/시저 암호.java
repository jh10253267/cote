//아스키 코드 개념 사용
import java.util.*;
class Solution {
    public String solution(String s, int n) {
        String answer = "";
        int length = s.length();
        //Z -> A 25차이
        for(int i=0; i<length; i++) {
            char c = s.charAt(i);
            if(Character.isLowerCase(c)) {
                answer += (char)((c - 'a' + n) % 26 + 'a');
            } else if(Character.isUpperCase(c)) {
                answer += (char)((c - 'A' + n) % 26 + 'A');
            } else if(c == ' ') {
                answer += " ";
                continue;
            }
        }
        
        return answer;
    }
}