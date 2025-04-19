import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 숫자의 개수
        String sNum = sc.next(); // 숫자들을 문자열로 입력받음
        char[] cNum = sNum.toCharArray(); // 문자열을 문자 배열로 변환

        int sum = 0;
        for (int i = 0; i < cNum.length; i++) {
            sum += cNum[i] - '0'; // 문자를 숫자로 변환해 더함
        }
        System.out.println(sum); // 세미콜론 추가됨
    }
}
