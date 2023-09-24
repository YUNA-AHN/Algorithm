class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        // 배열의 길이를 구하는 메서드 배열.length : 괄호 없음 !
        for (int i = 0; i < included.length; i ++) {
            if (included[i]){
                answer += a + d * i;
            }
        }
        return answer;
    }
}