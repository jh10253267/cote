import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String temp = Integer.toString(n);
        int length = temp.length();
        int [] arr = new int[length];
        
        for(int i=0; i<length; i++) {
            arr[i] = (int)temp.charAt(i) - 48;
        }
        
        for(int j = 0; j<length; j++) {
            answer += arr[j];
        }
        
        
        return answer;
    }
}