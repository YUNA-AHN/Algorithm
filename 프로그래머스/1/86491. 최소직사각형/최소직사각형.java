class Solution {
    // 각 명함의 긴 쪽과 짧은 쪽을 나누어 긴 쪽의 최대, 짧은 쪽의 최대를 구하는 문제
    public int solution(int[][] sizes) {
        System.out.println();
        int wid = 0; // 긴 쪽 비교
        int len = 0; // 짧은 쪽 비교
        // length : 배열의 크기, 문자열 길이는 () 추가
        for(int i = 0; i < sizes.length; i++){
            // 긴 쪽과 짧은 쪽 구분
            int lng = (sizes[i][0] < sizes[i][1]) ? sizes[i][1] : sizes[i][0];
            int srt = (sizes[i][0] > sizes[i][1]) ? sizes[i][1] : sizes[i][0];
            
            // 비교
            wid = (wid > lng) ? wid : lng;
            len = (len > srt) ? len : srt;
            
        }
        
        return wid*len;
    }
}