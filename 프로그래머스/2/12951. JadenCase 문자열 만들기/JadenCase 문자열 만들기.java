
class Solution {
    public String solution(String s) {
        StringBuffer sb = new StringBuffer();
        boolean flag = true;
        s = s.toLowerCase();
        
        for(char c : s.toCharArray()) {
            if(c == ' ') {
                flag = true;
            } else if(flag) {
                c = Character.toUpperCase(c);
                flag = false;
            }
            sb.append(c);
        }
     return sb.toString();   
    }
} 