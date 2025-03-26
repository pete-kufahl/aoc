package common;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class GridReaderTest {

    @Test
    void readIntegerGridFromFile_valid() throws IOException {
        // Create a temporary test file
        Path tempFile = Files.createTempFile("grid", ".txt");
        Files.write(tempFile, Arrays.asList("012", "345", "678"));

        List<List<Integer>> expected = Arrays.asList(
                Arrays.asList(0, 1, 2),
                Arrays.asList(3, 4, 5),
                Arrays.asList(6, 7, 8)
        );

        List<List<Integer>> result = GridReader.readIntegerGridFromFile(tempFile.toString());
        assertEquals(expected, result);

        Files.delete(tempFile);
    }

    @Test
    void readIntegerGridFromFile_empty() throws IOException {
        Path tempFile = Files.createTempFile("empty_grid", ".txt");
        Files.write(tempFile, new ArrayList<>());

        List<List<Integer>> result = GridReader.readIntegerGridFromFile(tempFile.toString());
        assertTrue(result.isEmpty());

        Files.delete(tempFile);
    }

    @Test
    void getStartingPoints() {
        List<List<Integer>> grid = Arrays.asList(
                Arrays.asList(0, 1, 2),
                Arrays.asList(3, 0, 5),
                Arrays.asList(6, 7, 0)
        );

        List<int[]> expected = Arrays.asList(new int[]{0, 0}, new int[]{1, 1}, new int[]{2, 2});
        List<int[]> result = GridReader.getStartingPoints(grid, 0);

        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertArrayEquals(expected.get(i), result.get(i));
        }
    }

    @Test
    void testGetStartingPoints_NoZeroes() {
        List<List<Integer>> grid = Arrays.asList(
                Arrays.asList(1, 2, 3),
                Arrays.asList(4, 5, 6)
        );

        List<int[]> result = GridReader.getStartingPoints(grid, 0);
        assertTrue(result.isEmpty());
    }
}