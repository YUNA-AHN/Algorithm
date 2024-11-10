class Solution {
    static int answer = 0;
    
    public int solution(int[] numbers, int target) {
        recur(numbers, target, 0, 0);
        return answer;
    }
    
    // 재귀함수 작성
    public void recur(int[] numbers, int target, int now, int total){
        // 멈춤 조건 : 길이에 도달하는 경우
        if (now == numbers.length) {
            // 카운트 조건 : 길이에 도달했을 때
            if (total == target) {
                answer++;
            }
        } else {
            // 더하고 빼서 dfs 진행
            recur(numbers, target, now + 1, total + numbers[now]);
            recur(numbers, target, now + 1, total - numbers[now]);
        }
    }
}