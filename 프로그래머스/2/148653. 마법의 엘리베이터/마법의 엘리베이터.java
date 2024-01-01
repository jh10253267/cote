//+10이던 +100이던 돌의 수는 하나
//-를 쓰느냐와 +를 쓰느냐는 5를 기준으로 갈린다.
//6이라면 -로 빼고 +4를 하는 것이 최선이다. Math.min으로 판별
class Solution {
    public int solution(int storey) {
        return elevator(storey);
    }
    
    private int elevator(int floor) { 
        if(floor <= 1) return floor;
        int underTen = floor%10; // 6
        int rest = floor/10; // 1
        
        int temp1 = underTen + elevator(rest);
        int temp2 = (10-underTen) + elevator(rest+1);
        
        return Math.min(temp1, temp2);
    }
}