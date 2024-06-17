//배열을 순회한다
//
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        //n개의 배열 생성
        int[] arr = new int[n];
        int length = arr.length;
        for(int i = 0; i<length; i++) {
            arr[i] = 1;
        }
        for(int i : reserve) {
            arr[i-1] += 1;
        }
        for(int i : lost) {
            arr[i-1] -= 1;
        }
        
        for(int i=0; i<length; i++ ) {
            if(arr[i] > 1) {
                if(i == 0 && arr[i+1] == 0) {
                    arr[i+1] += 1;
                    arr[i] -= 1;
                } else if(i>0 && arr[i-1] == 0) {
                    arr[i-1] += 1;
                    arr[i] -= 1;
                } else if(i < length-1 && arr[i+1] == 0) {
                    arr[i+1] += 1;
                    arr[i] -= 1;
                }
            }
        }
        for(int i : arr) {
        
            if(i > 0) {
                answer ++;
            }
        }
        
        return answer;
    }
}