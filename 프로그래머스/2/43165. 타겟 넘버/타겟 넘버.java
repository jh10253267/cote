class Solution {
    int answer = 0;
    
    public int solution(int[] numbers, int target) {
        //완전탐색(깊이탐색)을 하고 타겟에 닿았을 때 깊이가 numbers.length와 같으면 카운트 ++
        
        DFS(numbers, 0, 0, target);
        
        return answer;
    }
    public void DFS(int[] numbers, int depth, int sum, int target) {
        if(depth == numbers.length) {
            if(sum == target) {
                answer++;
            }
            
        } else {
            DFS(numbers, depth + 1, sum + numbers[depth], target);
            DFS(numbers, depth + 1, sum - numbers[depth], target);
            
        }
    }
}