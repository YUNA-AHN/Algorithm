import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String res = "";
        for (char text : a.toCharArray()){
            if (Character.isLowerCase(text)) {
                res += Character.toUpperCase(text);
            } else {
                res += Character.toLowerCase(text);
            }
        }
        System.out.println(res);
    }
}