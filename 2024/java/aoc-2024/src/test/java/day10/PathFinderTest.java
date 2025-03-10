package day10;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class PathFinderTest {
    @Test
    void testIsValid() {
        List<List<Integer>> grid = Arrays.asList(
                Arrays.asList(0, 1, 2),
                Arrays.asList(3, 4, 5),
                Arrays.asList(6, 7, 8)
        );

        assertTrue(PathFinder.isValid(0, 1, grid, 0)); // 0 → 1 is valid
        assertFalse(PathFinder.isValid(1, 1, grid, 0)); // 0 → 4 is invalid
        assertFalse(PathFinder.isValid(-1, 0, grid, 0)); // Out of bounds
        assertFalse(PathFinder.isValid(3, 0, grid, 0)); // Out of bounds
    }

    @Test
    void testFindPaths_SimpleGrid() {
        List<List<Integer>> grid = Arrays.asList(
                Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        );

        PathFinder.findPaths(grid, true);
        // Expected output: 1 valid path from 0 → 9 in a straight line
    }

    @Test
    void testFindPaths_NoValidPath() {
        List<List<Integer>> grid = Arrays.asList(
                Arrays.asList(0, 1, 2),
                Arrays.asList(9, 8, 7),
                Arrays.asList(6, 5, 4)
        );

        PathFinder.findPaths(grid, true);
        // No valid path from 0 to 9, expect 0 solutions
    }

}