//우선 배열을 스캔할 수 있는 방법 생각하기.
//

class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        //int[][] answer = new int[arr1.length][inA.length];
        int[] inA = arr1[0];
        int[][] answer = new int[arr1.length][inA.length];
        
        for(int i=0; i<arr1.length; i++) {
            
            int[] inArr1 = arr1[i];
            int[] inArr2 = arr2[i];
            
            for(int j=0; j<inArr1.length; j++) {
                answer[i][j] = inArr1[j] + inArr2[j];
                
            }
            
        }
        
        return answer;
    }
}