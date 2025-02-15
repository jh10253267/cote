class Solution {
    public String solution(String s) {
        String answer = "";
        int length = s.length();
        char a, a1;
        
        if(length % 2 !=0) {
            a = s.charAt(length/2);    
            answer = Character.toString(a);
        } else {
            a = s.charAt(length/2-1);
            a1 = s.charAt(length/2);
            answer = Character.toString(a) + Character.toString(a1);
        }        
        return answer;
    }
}