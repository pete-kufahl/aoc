package day6;

import common.GridReader;

import java.io.IOException;
import java.util.List;

public class Day6 {
    public static void main(String[] args) throws IOException {
        var grid = GridReader.readGridFromFile("src/main/resources/day6/example.txt");
        GridReader.printGrid(grid);
    }

    public static class StartingPoint {
        int row;
        int col;
        char orientation;

        public StartingPoint(int row, int col, char orientation) {
            this.row = row;
            this.col = col;
            this.orientation = orientation;
        }
    }

    public static StartingPoint findStartingPoint(char[][] grid, List<Character> chars) {
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
