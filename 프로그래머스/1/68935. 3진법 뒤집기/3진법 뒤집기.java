class Solution {
    public int solution(int n) {
        int answer = 0;
        String nxt = "";
        // 3진법 반전으로 변환
        while (n / 3 != 0 || n % 3 != 0) {
            nxt += n % 3;
            n /= 3;
        }
        System.out.println(nxt.length());
        // 10진법으로 표현
        for (int i = 0; i < nxt.length(); i++) {
            int num = Integer.valueOf(Character.toString(nxt.charAt(i)));
            answer += Math.pow(3, nxt.length() - i - 1) * num;
        }
        return answer;
    }
}