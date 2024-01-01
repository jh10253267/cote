import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        int count = 0;
        String[] strArr = s.split("");

        for(String str : strArr) {
            if(str.contains(" ")) {
                count = 0;
            } else {
                count++;
            }
            
            answer += count%2 == 0 ? str.toLowerCase() : str.toUpperCase(); 
        }
      return answer;
    }
}