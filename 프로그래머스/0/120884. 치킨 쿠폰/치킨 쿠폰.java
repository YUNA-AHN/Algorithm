class Solution {
    public int solution(int chicken) {
        int more = 0;
        while (chicken >= 10) {
            more += chicken / 10;
            chicken = chicken / 10 + chicken % 10;
            System.out.println(more);
            System.out.println(chicken);
        }
        return more;
    }
}
/*
1081 / 10 => 108 : more + 108 / coupon 108 + 1
108 / 10 => 10 : more + 10 / coupon 18
18 / 10 => 1 : more + 1 / coupon 9
*/