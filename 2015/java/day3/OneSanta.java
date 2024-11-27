import java.io.FileReader;
import java.io.IOException;
import java.lang.String;
import java.util.HashSet;
import java.util.Set;

public class OneSanta {
    
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
        int[] coords = {0, 0};
        visited.add(encode(coords));

        try {
            inputStream = new FileReader("input.txt");
            int c;
            while ((c = inputStream.read()) != -1) {
                moves += 1;
                int x = coords[0];
                int y = coords[1]; 
                coords = moveDirection((char) c, x, y);
                visited.add(encode(coords));
            }
            System.out.println(String.format("houses visited after %d moves is %d", moves, visited.size()));
        } finally {
            if (inputStream != null) {
                inputStream.close();
            }
        }
    }
}
