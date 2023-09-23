class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        // 숫자의 자릿수를 구하기 위하여 ! (int)(Math.log10(변수)+1)
        int len_a = (int)(Math.log10(a)+1);
        int len_b = (int)(Math.log10(b)+1);
        // 거듭제곱을 위한 함수 (int) Math.pow(밑, 지수)
        // (int) 정수형으로의 자료 변형
        int a_first = a * (int) Math.pow(10, len_b) + b;
        int b_first = b * (int) Math.pow(10, len_a) + a;
        if (a_first >= b_first) {
            answer = a_first;
        } else {
            answer = b_first;
        }
        return answer;
    }
}