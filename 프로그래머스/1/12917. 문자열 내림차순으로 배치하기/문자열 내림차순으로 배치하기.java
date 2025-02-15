import java.util.*;
//각 문자를 char배열로 바꾼다. char배열을 정렬한 후 스트링으로 반환한다.
//문자열을 나누어 문자열 배열로 만들고 내림차순 정렬하고 
//StringBuilder


class Solution {
    public String solution(String s) {
        String answer;
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder(new String(arr));
        //문자열 배열로 바꾸기
        answer = sb.reverse().toString();
        
        return answer;
        
    }
}