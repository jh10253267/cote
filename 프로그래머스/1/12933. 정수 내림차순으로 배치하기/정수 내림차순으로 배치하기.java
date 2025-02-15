import java.util.*;

class Solution {
    public long solution(long n) {
        
        String[] list = String.valueOf(n).split("");
        Arrays.sort(list, Collections.reverseOrder());
        String str = "";
        
        for(int i=0; i<list.length; i++) {
            str += list[i];
        }
        Long answer = Long.parseLong(str);
        return answer;
    }
}