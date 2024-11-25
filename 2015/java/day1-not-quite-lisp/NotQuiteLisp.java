/*
 * > javac NotQuiteLisp.java
 * > java NotQuiteLisp
 */

import java.io.FileReader;
import java.io.IOException;
import java.lang.String;

public class NotQuiteLisp {

    private static int process(char c) {
        if (c == '(') {
            return 1;
        } else if (c == ')') {
            return -1;
        } else {
            return 0;
        }
    }

    public static void main(String[] args) throws IOException {
        FileReader inputStream = null;
        int num = 0;
        int ret = 0;
        boolean basement = false;
            
        try {
            inputStream = new FileReader("input.txt");
            int c;
            while ((c = inputStream.read()) != -1) {
                // System.out.println(c);
                ret += process((char) c);
                num += 1;
                if (ret == -1 && !basement) {
                    basement = true;
                    System.out.println(String.format("basement entered at position %d", num+1));
                }
            }
            System.out.println(String.format("final floor after %d characters is %d", num, ret));
        } finally {
            if (inputStream != null) {
                inputStream.close();
            }
        }
    }
}
