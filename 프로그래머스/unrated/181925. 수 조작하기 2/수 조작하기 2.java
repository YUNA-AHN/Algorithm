class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        int n = numLog.length - 1;
        for (int i = 0; i < n; i++){
            if (numLog[i+1] - numLog[i] == 1){
                answer += "w";
            } else if (numLog[i+1] - numLog[i] == -1){
                answer += "s";
            } else if (numLog[i+1] - numLog[i] == 10){
                answer += "d";
            } else {
                answer += "a";
            }
        }
        return answer;
    }
}