import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String arr = br.readLine();

        if (arr.equals("1 2 3 4 5 6 7 8")) {
            System.out.println("ascending");
        } else if (arr.equals("8 7 6 5 4 3 2 1")) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }

    }
}
