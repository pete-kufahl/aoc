package common;

import java.util.*;
import java.io.*;

public class GridReader {
    public static void main(String[] args) {
        String input = "....#.....\n"
                + ".........#\n"
                + "..........\n"
                + "..#.......\n"
                + ".......#..\n"
                + "..........\n"
                + ".#..^.....\n"
                + "........#.\n"
                + "#.........\n"
                + "......#...";

        char[][] grid = readGrid(input);
        printGrid(grid);
    }

    public static char[][] readGrid(String input) {
        String[] lines = input.split("\\n");
        int rows = lines.length;
        int cols = lines[0].length();
        char[][] grid = new char[rows][cols];

        for (int i = 0; i < rows; i++) {
            grid[i] = lines[i].toCharArray();
        }
        return grid;
    }

    public static char[][] readGridFromFile(String filename) throws IOException {
        List<String> lines = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                lines.add(line);
            }
        }
        int rows = lines.size();
        int cols = rows > 0 ? lines.getFirst().length() : 0;
        char[][] grid = new char[rows][cols];

        for (int i = 0; i < rows; i++) {
            grid[i] = lines.get(i).toCharArray();
        }
        return grid;
    }

    public static void printGrid(char[][] grid) {
        for (char[] row : grid) {
            System.out.println(new String(row));
        }
    }
}
