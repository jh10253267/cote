class Solution {
    public boolean solution(String s) {
        int length = s.length();
        int a = 0;
        
        if(length==4 || length==6) {
            
          try {
              a = Integer.parseInt(s);
              return true;
          } catch(Exception e)  {
              return false;
          }
            
        }
        
        return false;
    }
}