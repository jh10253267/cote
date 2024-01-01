class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int zero_count = 0;
        int one_count = 0;
        int count = 0;
        int d = 0;//차수
        boolean flag = true;
        while(flag) {
            for(int i = 0; i<s.length(); i++) {
                if(s.charAt(i) == '0') {
                    zero_count ++;
                } else if(s.charAt(i) == '1'){
                    one_count++;
                }
            }
            String temp = Integer.toBinaryString(one_count);
            s = temp;
            
            count++;
            if(one_count == 1) {
                flag = false;
            }
            one_count = 0;
            
        }
        answer[0] = count;
        answer[1] = zero_count;
        return answer;
    }
}