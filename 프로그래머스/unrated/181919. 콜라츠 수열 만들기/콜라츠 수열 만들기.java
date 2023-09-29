import java.util.ArrayList;

class Solution {
    public ArrayList solution(int n) {
        ArrayList <Integer> answer = new ArrayList<>();
        answer.add(n);
        // n이 1보다 큰 동안에
        while (n > 1) {
            // 짝수면 나누기 2
            if (n % 2 == 0){
                n = n / 2;
                answer.add(n);
            } else {
                // 홀수면 3*n+1
                n = 3*n + 1;
                answer.add(n);
            }
        }
        return answer;
    }
}