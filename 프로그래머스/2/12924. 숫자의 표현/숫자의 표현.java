//투포인터.
class Solution {
    public int solution(int n) {
        
        int sum = 1;
        int count = 1;
        int start_index = 1;
        int end_index = 1;
        
      while(end_index != n) {
          if(sum == n) {
              count ++;
              end_index ++;
              sum = sum + end_index;
          } else if(sum < n) {
              end_index++;
              sum = sum + end_index;
          } else if(sum > n) {
              sum = sum - start_index++;
          } 
          
      }
        return count;
        
    }
}