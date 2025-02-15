class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int t_length = t.length();
        int p_length = p.length();
        Long p_number = Long.valueOf(p);
    
        for(int i = 0; i <= t_length-p_length; i++) {
            String temp = t.substring(i, i+p_length);
            Long number = Long.valueOf(temp);
            
            if(number <= p_number) {
                answer++;
            }
        }
        return answer;
    }
}