class Solution {
    public int solution(String number) {
        int answer = 0;
        for (int i = 0; i < number.length(); i++){
            int n = Integer.parseInt(number.substring(i,i+1));
            answer += n;
        }
        answer %= 9;
        return answer;
    }
}