package day6;

import common.GridReader;

import java.io.IOException;
import java.util.*;

public class Day6 {

    private char[][] grid;

    public Day6(char[][] grid) {
        this.grid = grid;
    }

    public static void main(String[] args) throws IOException {
        // String filepath = "src/main/resources/day6/example.txt";
        String filepath = "src/main/resources/day6/input.txt";
        var grid = GridReader.readGridFromFile(filepath);
        // GridReader.printGrid(grid);
        Day6 day6 = new Day6(grid);
        day6.countPositionsVisitedInMaze(false);

        // reset
        day6.grid = GridReader.readGridFromFile(filepath);
        day6.trapNavigatorInCycle(false);
    }



    // part 1
    private void countPositionsVisitedInMaze(boolean debug) {
        StartingPoint start = findStartingPoint(this.grid, Arrays.asList('^', 'v', '<', '>'));
        System.out.println("starting at " + start.position + " pointing: " + start.orientation);

        Navigator navigator = new Navigator(this.grid, '#', start.orientation);
        Navigator.Position curr = new Navigator.Position(start.position);
        long count = 1L;
        Set<Navigator.Position> visited = new HashSet<>();

        while (!navigator.escaped) {
            count++;
            visited.add(curr);
            if (debug) { this.grid[curr.r][curr.c] = 'X'; }

            curr = navigator.nextStep(curr);
            if (debug) { System.out.println("move " + count + ", position " + curr); }

            if (curr == null) {
                System.out.println("Trapped!");
                break;
            }
        }
        // example: 41
        // input: 4665
        System.out.println("Traversed " + visited.size() + " locations in " + count + " steps");

        if (debug) {
            int xes = 0;
            for (char[] row : grid) {
                for (char c : row) {
                    if (c == 'X') {
                        xes++;
                    }
                }
            }
            System.out.println(xes + " X's in maze");
        }
    }

    // part 2
    private void trapNavigatorInCycle(boolean debug) {
        StartingPoint start = findStartingPoint(grid, Arrays.asList('^', 'v', '<', '>'));
        List<Navigator.Position> spaces = new ArrayList<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '.') {
                    spaces.add(new Navigator.Position(i, j));
                }
            }
        }
        int success = 0;
        while (!spaces.isEmpty()) {
            var pos = spaces.removeLast();
            if (debug) { System.out.println("trying obstacle at " + pos); }
            grid[pos.r][pos.c] = '#';
            Navigator navigator = new Navigator(grid, '#', start.orientation);
            Navigator.Position curr = new Navigator.Position(start.position);
            var prev = new Navigator.Position(curr);
            long steps = 1L;
            while(!navigator.escaped) {
                steps++;
                curr = navigator.nextStep(curr);
                if (curr == null) {
                    System.out.println("Trapped!");
                    break;
                }
                if (navigator.trappedInLoop) {
                    if (debug) { System.out.println("guard trapped at " + prev); }
                    success++;
                    break;
                }
                prev = curr;
            }
            if (navigator.escaped && debug) { System.out.println("guard escaped after " + steps + " steps"); }
            grid[pos.r][pos.c] = '.';
        }
        // example: 6
        // input: 1688
        System.out.println("trapped the guard in " + success + " different arrangements");
    }

    public static class StartingPoint {
        Navigator.Position position;
        char orientation;

        public StartingPoint(int row, int col, char orientation) {
            this.position = new Navigator.Position(row, col);
            this.orientation = orientation;
        }
    }

    public StartingPoint findStartingPoint(char[][] grid, List<Character> chars) {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (chars.contains(grid[i][j])) {
                    return new StartingPoint(i, j, grid[i][j]);
                }
            }
        }
        return null;
    }
}
