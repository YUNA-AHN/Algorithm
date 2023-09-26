class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        // 기존 길이보다 크기가 1 큰 배열 생성
        int[] answer = new int[n+1];
        // 순회하면서 값 입력
        for (int i=0; i < n; i++){
            answer[i] = num_list[i];
        }
        // 마지막 값은 n > n-1 :
        if(answer[n-1] > answer[n-2]){
            answer[n] = answer[n-1] - answer[n-2];
        } else{
            answer[n] = answer[n-1] * 2;
        }
        return answer;
    }
}