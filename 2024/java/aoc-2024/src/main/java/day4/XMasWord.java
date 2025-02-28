package day4;

import java.io.*;
import java.util.*;

public class XMasWord {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java XMasWord <filename>");
            return;
        }

        char[][] grid = getGrid(args);

        // part 1
        List<int[]> part1 = findWord(grid, "XMAS");
        System.out.println("Found XMAS " + part1.size() + " times");

        // part 2
        int part2 = findCrosses(grid);
        System.out.println("Found X-MAS cross patterns " + part2 + " times");

    }

    public static List<int[]> findWord(char[][] grid, String word) {
        List<int[]> results = new ArrayList<>();
        int rows = grid.length;
        int cols = grid[0].length;
        char firstChar = word.charAt(0); 
        int[][] directions = {
            {-1, 0}, {1, 0}, {0, -1}, {0, 1},  // up, down, left, right
            {-1, -1}, {-1, 1}, {1, -1}, {1, 1}  // up-left, up-right, down-left, down-right
        };

        // iterate through all rows/cols, match first letter, check all directions
        //  keep going in a direction until bounds check fails or mismatch
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == firstChar) {
                    for (int[] direction : directions) {
                        int deltaR = direction[0];
                        int deltaC = direction[1];
                        boolean found = true;

                        for (int i = 1; i < word.length(); i++) {
                            int newRow = row + deltaR * i;
                            int newCol = col + deltaC * i;

                            if (newRow < 0 || newRow >= rows || newCol < 0 || newCol >= cols) {
                                found = false;
                                break;
                            }
                            
                            if (grid[newRow][newCol] != word.charAt(i)) {
                                found = false;
                                break;
                            }
                        }

                        if (found) {
                            results.add(new int[]{row, col, deltaR, deltaC});
                        }
                    }
                }
            }
        }
        return results;
    }

    public static int findCrosses(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        // store the A-locations as strings of coordinates -> dirty!
        Set<String> forwardCenters = new HashSet<>();
        Set<String> backwardCenters = new HashSet<>();

        // forward diagonals
        for (int row = 0; row < rows - 2; row++) {
            for (int col = 0; col < cols - 2; col++) {
                char c1 = grid[row][col];
                char c2 = grid[row + 1][col + 1];
                char c3 = grid[row + 2][col + 2];
                if ((c1 == 'M' && c2 == 'A' && c3 == 'S') || (c1 == 'S' && c2 == 'A' && c3 == 'M')) {
                    forwardCenters.add((row + 1) + "," + (col + 1));
                }
            }
        }

        // backward diagonals
        for (int row = 0; row < rows - 2; row++) {
            for (int col = 2; col < cols; col++) {
                char c1 = grid[row][col];
                char c2 = grid[row + 1][col - 1];
                char c3 = grid[row + 2][col - 2];
                if ((c1 == 'M' && c2 == 'A' && c3 == 'S') || (c1 == 'S' && c2 == 'A' && c3 == 'M')) {
                    backwardCenters.add((row + 1) + "," + (col - 1));
                }
            }
        }

        // intersections of forward and backward diagonals
        forwardCenters.retainAll(backwardCenters);
        return forwardCenters.size();
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
        return grid.toArray(new char[grid.size()][]);
    }
}
