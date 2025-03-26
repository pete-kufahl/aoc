package common;

import java.nio.file.Files;
import java.nio.file.Paths;
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

    /**
    * Reads the file line by line, converts each character into an integer, and stores
    * the grid as a list of lists.
    */
    public static List<List<Integer>> readIntegerGridFromFile(String filePath) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        List<List<Integer>> intGrid = new ArrayList<>();

        for (String line : lines) {
            List<Integer> row = new ArrayList<>();
            for (char ch : line.trim().toCharArray()) {
                row.add(Character.getNumericValue(ch));
            }
            intGrid.add(row);
        }

        return intGrid;
    }

    /**
     * Iterates through the grid to find all positions where the value matches startDigit
     * and returns a list of coordinate pairs (int[]).
     */
    public static List<int[]> getStartingPoints(List<List<Integer>> grid, int startDigit) {
        List<int[]> startPoints = new ArrayList<>();

        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid.get(r).size(); c++) {
                if (grid.get(r).get(c) == startDigit) {
                    startPoints.add(new int[]{r, c});
                }
            }
        }

        return startPoints;
    }

    public static void printGrid(char[][] grid) {
        for (char[] row : grid) {
            System.out.println(new String(row));
        }
    }
}
