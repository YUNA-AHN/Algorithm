class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = arr;
        for (int i=0; i < queries.length; i++){
            int a = arr[queries[i][0]];
            int b = arr[queries[i][1]];
            answer[queries[i][1]] = a;
            answer[queries[i][0]] = b;
        }
        return answer;
    }
}