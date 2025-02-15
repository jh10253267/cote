import java.util.*;

class Solution {
    public int[] solution(long n) {
        int length = (int)(Math.log10(n) + 1);
        int[] answer = new int[length];
        long b = 0;
        
        
        
        for(int i=0; i<length; i++) {
            answer[i] = (int)(n%10);
            b = n/10;
            n = b;
        }
            
        
        return answer;
    }
}