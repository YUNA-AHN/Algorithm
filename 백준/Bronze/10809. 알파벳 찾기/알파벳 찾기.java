import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st = br.readLine();
        // a-z(97-122) 순환하며 체크 - 아스키코드(형변환)
        for (int i = 97; i < 122; i++) {
            System.out.print(st.indexOf((char) i) + " ");
        }
        System.out.print(st.indexOf((char) 122));
    }
}