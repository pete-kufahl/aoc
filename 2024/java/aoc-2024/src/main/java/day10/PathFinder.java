package day10;

import common.GridReader;

import java.util.ArrayList;
import java.util.List;

public class PathFinder {
    // down, right, up, left
    private static final int[][] DIRECTIONS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    /**
     * Checks if a given cell is valid based on the grid size and previous value
     */
    public static boolean isValid(int x, int y, List<List<Integer>> grid, int prev) {
        return (x >= 0 && x < grid.size()) &&
                (y >= 0 && y < grid.get(0).size()) &&
                (grid.get(x).get(y) == prev + 1);
    }

    /**
     * iterates through all 0 start points and calls dfs
     */
    public static void findPaths(List<List<Integer>> grid, boolean debug) {
        System.out.println("Input grid is " + grid.size() + " rows and " + grid.get(0).size() + " columns");
        List<int[]> starts = GridReader.getStartingPoints(grid, 0);
        int[] rating = {0}; // mutable reference to track rating across recursive calls

        int totalScore = 0;
        int totalRating = 0;

        for (int[] start : starts) {
            List<List<int[]>> currentSolutions = new ArrayList<>();
            rating[0] = 0;
            dfs(start[0], start[1], grid, new ArrayList<>(), new ArrayList<>(), currentSolutions, rating);

            System.out.println("Starting point (" + start[0] + ", " + start[1] + ") has score " +
                    currentSolutions.size() + " and rating " + rating[0]);

            totalScore += currentSolutions.size();
            totalRating += rating[0];

            if (debug) {
                System.out.println("Solutions: " + formatSolutions(currentSolutions));
            }
        }

        System.out.println("Total score for grid is " + totalScore);
        System.out.println("Total rating for the grid is " + totalRating);
    }

    /**
     * Depth-first search - recursive
     * finds 0-9 paths and tracks visited summits
     */
    private static void dfs(int x, int y,
                            List<List<Integer>> grid,
                            List<int[]> path,
                            List<int[]> summits,
                            List<List<int[]>> solutions,
                            int[] rating) {
        path.add(new int[]{x, y});

        if (grid.get(x).get(y) == 9) {
            rating[0]++;
            if (!containsPoint(summits, x, y)) {
                summits.add(new int[]{x, y});
                solutions.add(new ArrayList<>(path));
            }
        } else {
            for (int[] dir : DIRECTIONS) {
                int newX = x + dir[0], newY = y + dir[1];
                if (isValid(newX, newY, grid, grid.get(x).get(y))) {
                    dfs(newX, newY, grid, path, summits, solutions, rating);
                }
            }
        }
        path.remove(path.size() - 1); // backtrack
    }

    /**
     * check if a point exists in the summits list
     */
    private static boolean containsPoint(List<int[]> list, int x, int y) {
        for (int[] point : list) {
            if (point[0] == x && point[1] == y) {
                return true;
            }
        }
        return false;
    }

    /**
     * convert paths to a readable format
     */
    private static String formatSolutions(List<List<int[]>> solutions) {
        StringBuilder sb = new StringBuilder();
        for (List<int[]> path : solutions) {
            sb.append("[");
            for (int[] point : path) {
                sb.append("(").append(point[0]).append(", ").append(point[1]).append("), ");
            }
            sb.setLength(sb.length() - 2); // Remove trailing comma and space
            sb.append("] ");
        }
        return sb.toString();
    }
}