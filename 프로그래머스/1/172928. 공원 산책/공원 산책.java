class Solution {
    public int[] solution(String[] park, String[] routes) {
        int r = park.length;
        int c = park[0].length();
        int sr = 0, sc = 0;
        // 시작점 찾기
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                if (park[i].charAt(j) == 'S'){
                    sr = i; sc = j;
                    break;
                }
            }
        }
        String dir = ""; // 방향
        Integer cnt = 0; // 거리
        // 시작점에서 출발
        for (String route:routes){
            dir = route.split(" ")[0];
            cnt = Integer.valueOf(route.split(" ")[1]);
            int nr = sr, nc = sc;
            if (dir.equals("N")){
                nr = sr - cnt;
            } else if (dir.equals("S")){
                nr = sr + cnt;
            } else if (dir.equals("W")){
                nc = sc - cnt;
            } else {
                nc = sc + cnt;
            }
            // 이동 가능한지 체크
            if (check(sr, sc, nr, nc, r, c, park)) {
                sr = nr;
                sc = nc;
            }
        }
        int[] answer = {sr, sc};
        return answer;
    }
    public boolean check(int sr, int sc, int nr, int nc, int r, int c, String[] park) {
        int sa = (sr > nr) ? nr : sr ;
        int sb = (sr > nr) ? sr : nr ;
        int na = (nc > sc) ? sc : nc ;
        int nb = (nc > sc) ? nc : sc ;
        // 범위를 넘어서지 않는가 ?
        if (nr < 0 || nc < 0 || nr >= r || nc >= c) {
            return false;
            }
        for (int k = sa; k <= sb; k++){
            for (int l = na; l <= nb; l++){
                if (park[k].charAt(l) == 'X'){
                    return false;
                }
            }
        }
        return true;
    }
}