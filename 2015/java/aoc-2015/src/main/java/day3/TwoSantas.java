package day3;

import java.io.FileReader;
import java.io.IOException;
import java.lang.String;
import java.util.HashSet;
import java.util.Set;

public class TwoSantas {
    public static int[] moveDirection(char direction, int x, int y) {
        switch (direction) {
            case '<': // Move left
                x -= 1;
                break;
            case '>': // Move right
                x += 1;
                break;
            case '^': // Move up
                y += 1;
                break;
            case 'v': // Move down
                y -= 1;
                break;
            default:
                throw new IllegalArgumentException("Invalid direction: " + direction);
        }
        // Return the updated coordinates
        return new int[]{x, y};
    }

    public static String encode(int[] coordinates) {
        return coordinates[0] + "_" + coordinates[1];
    }

    public static void main(String[] args) throws IOException {
        FileReader inputStream = null;
        Set<String> visited = new HashSet<>();
        int moves = 0;
        int[] santa = {0, 0};
        int[] robosanta = {0, 0};
        boolean is_santa;
        visited.add(encode(santa));

        try {
            inputStream = new FileReader("src/main/resources/day3/input.txt");
            int c;
            while ((c = inputStream.read()) != -1) {
                moves += 1;
                is_santa = moves % 2 == 1;
                if (is_santa) {
                    santa = moveDirection((char) c, santa[0], santa[1]);
                    visited.add(encode(santa));
                } else {
                    robosanta = moveDirection((char) c, robosanta[0], robosanta[1]);
                    visited.add(encode(robosanta));
                }
            }
            System.out.printf("houses visited after %d moves is %d%n", moves, visited.size());
        } finally {
            if (inputStream != null) {
                inputStream.close();
            }
        }
    }    
}
