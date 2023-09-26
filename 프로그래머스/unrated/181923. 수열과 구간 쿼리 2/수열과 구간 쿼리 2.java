class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int n = queries.length;
        int[] answer = new int[n];
        // 쿼리를 순회
        for (int i=0; i < n; i ++){
            // arr을 순회
            int mn = 10000000;
            int s = queries[i][0];
            int e = queries[i][1];
            for (int j = s; j <= e; j++){
                int k = queries[i][2];
                if (arr[j] > k && arr[j] < mn){
                    mn = arr[j];
                }
            }
            if (mn == 10000000) {
                answer[i] = -1;
            } else {
                answer[i] = mn;
            }
        }
        return answer;
    }
}