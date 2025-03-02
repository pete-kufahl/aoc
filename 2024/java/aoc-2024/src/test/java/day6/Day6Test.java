package day6;

import common.GridReader;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class Day6Test {

    @Test
    void findStartingPoint() {
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

        char[][] grid = GridReader.readGrid(input);
        List<Character> chars = Arrays.asList('^', 'v', '<', '>');
        Day6.StartingPoint result = Day6.findStartingPoint(grid, chars);

        assertNotNull(result);
        assertEquals(6, result.row);
        assertEquals(4, result.col);
        assertEquals('^', result.orientation);
    }
}