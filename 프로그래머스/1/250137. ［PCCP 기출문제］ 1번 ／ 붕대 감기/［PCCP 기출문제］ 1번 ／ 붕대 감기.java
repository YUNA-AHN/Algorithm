class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int t = bandage[0]; // 시전 시간
        int x = bandage[1]; // 초당 회복량
        int y = bandage[2]; // 추가 회복량
        int now = health; // 현재 체력
        int last = 0; // 초기값 0으로 설정
        // 공경을 순회
        for (int[] attack : attacks){
            int time = attack[0]; // 공격 시간
            int d = attack[1]; // 데미지
            int cont = time - last - 1; // 지속 시간
            now += x * cont + y * (cont / t); // 시간 만큼 초당 회복량 + 추가회복량
            now = (now > health) ? health : now; // max 넘으면 max로 맞춰줌
            now -= d; // 데미지만큼 감소시키기
            // 0보다 작으면 죽음, break
            if (now <= 0) {
                answer = -1;
                break;
            // answer를 now로 설정, 마지막 시간을 time으로
            } else {
                answer = now ;
                last = time;
            }
        }
        
        return answer;
    }
}