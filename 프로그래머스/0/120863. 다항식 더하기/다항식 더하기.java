class Solution {
    public String solution(String polynomial) {
        String answer = "";
        int firstNum = 0;
        int cofNum = 0;
        String [] arr = polynomial.split(" "); // split하여 배열에 담기
        for (int i = 0; i < arr.length; i++) {
            // x항인 경우
            if (arr[i].charAt(arr[i].length() - 1) == 'x') {
                // 1인 경우
                if (arr[i].equals("x")) {
                    firstNum += 1;
                }
                // 1이 아닌 경우
                else {
                    String [] num = arr[i].split("x");
                    firstNum += Integer.parseInt(num[0]);
                }
            } // 상수항의 경우
            else if (!arr[i].equals("+")) {
                cofNum += Integer.parseInt(arr[i]);
            }
        }
        // x항과 상수항이 0인지 체크 후 answer 만들어주기
        if (firstNum > 0 && cofNum > 0) {
            if (firstNum == 1) {
                answer = "x + " + cofNum;
            } else {
                answer = firstNum + "x + " + cofNum;
            }
        } else if (firstNum > 0 ) {
            if (firstNum == 1) {
                answer = "x";
            } else {
                answer = firstNum + "x";
            }
        } else {
            answer = Integer.toString(cofNum);
        }
        
        return answer;
    }
}