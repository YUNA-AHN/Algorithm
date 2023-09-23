class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;
        // 같읍 "값"인지 판단하기 위해서는 equals를 사용해야 한다!
        // answer 는 0이라고 위에서 입력해두었으니 틀린 경우에는 따로 작성하지 않음
        if (ineq.equals(">")){
            if (eq.equals("=")) {
                if (n >= m) {
                    answer = 1;
                }
            } else {
                if (n > m) {
                    answer = 1;
                }
            }
        } else {
            if (eq.equals("=")){
                if (n <= m){
                    answer = 1;
                }
            } else {
                if (n < m){
                    answer = 1;
                }
            }
        }
        return answer;
    }
}