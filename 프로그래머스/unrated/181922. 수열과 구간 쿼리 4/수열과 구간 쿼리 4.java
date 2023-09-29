class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = arr;
        // 쿼리 길이만큼 순회
        for (int i=0; i < queries.length; i++){
            int s = queries[i][0];
            int e = queries[i][1];
            int k = queries[i][2];
            for (int j=0; j < arr.length; j++){
                if (j >=s && j <= e && j % k == 0){
                    answer[j] += 1;
                }
            }
        }
        return answer;
    }
}