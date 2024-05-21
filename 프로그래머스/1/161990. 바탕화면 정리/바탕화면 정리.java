class Solution {
    public int[] solution(String[] wallpaper) {
        int r = wallpaper.length;
        int c = wallpaper[0].length();
        int cnt = 0, lux = r, luy = c, rdx = 0, rdy = 0;
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                if (wallpaper[i].charAt(j) == '#'){
                    lux = (lux < i) ? lux : i;
                    luy = (luy < j) ? luy : j;
                    rdx = (rdx > i) ? rdx : i + 1;
                    rdy = (rdy > j) ? rdy : j + 1;
                }
            }
        }
        int[] answer = {lux, luy, rdx, rdy};
        return answer;
    }
}