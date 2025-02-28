package day6;

import java.io.*;
import java.util.*;

public class GuardMaze {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java XMasWord <filename>");
            return;
        }

        char[][] grid = getGrid(args);
    }

    private static char[][] getGrid(String[] args) {
        String filename = args[0];
        List<char[]> grid = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                grid.add(line.toCharArray());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Print the 2D matrix (for demonstration)
        for (char[] row : grid) {
            System.out.println(Arrays.toString(row));
        }

        return grid.toArray(new char[grid.size()][]);
    }
}
