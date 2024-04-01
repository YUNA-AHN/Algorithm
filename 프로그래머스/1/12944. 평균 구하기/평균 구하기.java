class Solution {
    public double solution(int[] arr) {
        double ans = 0;
        double cnt = arr.length;
        double total = 0;
        for (double num : arr) {
            total += num;
        }
        return total / cnt ;
    }
}