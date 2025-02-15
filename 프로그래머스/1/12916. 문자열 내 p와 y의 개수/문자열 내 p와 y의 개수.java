class Solution {
    boolean solution(String s) {
        boolean answer = true;

       String s2 =s.toLowerCase();
       int pCount = 0;
       int yCount = 0;
      for(int i=0; i<s2.length(); i++) {
          
          if(s2.charAt(i) == 'p') {
              pCount++;
          } else if(s2.charAt(i) == 'y') {
              yCount++;
          }
          
      }
        if(pCount != yCount) {
              answer = false;
          }
        return answer;
    }
}