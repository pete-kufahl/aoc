package day4;

import org.junit.jupiter.api.Test;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

public class XMasWordTest {

    @Test
    void testFindWord_Horizontal() {
        char[][] grid = {
                {'X', 'M', 'A', 'S'},
                {'A', 'B', 'C', 'D'},
                {'E', 'F', 'G', 'H'}
        };
        List<int[]> result = XMasWord.findWord(grid, "XMAS");
        assertFalse(result.isEmpty());
        assertArrayEquals(new int[]{0, 0, 0, 1}, result.getFirst());
    }

    @Test
    void testFindWord_Vertical() {
        char[][] grid = {
                {'X', 'A', 'E'},
                {'M', 'B', 'F'},
                {'A', 'C', 'G'},
                {'S', 'D', 'H'}
        };
        List<int[]> result = XMasWord.findWord(grid, "XMAS");
        assertFalse(result.isEmpty());
        assertArrayEquals(new int[]{0, 0, 1, 0}, result.getFirst());
    }

    @Test
    void testFindWord_Diagonal() {
        char[][] grid = {
                {'X', 'O', 'O', 'O'},
                {'O', 'M', 'O', 'O'},
                {'O', 'O', 'A', 'O'},
                {'O', 'O', 'O', 'S'}
        };
        List<int[]> result = XMasWord.findWord(grid, "XMAS");
        assertFalse(result.isEmpty());
        assertArrayEquals(new int[]{0, 0, 1, 1}, result.getFirst());
    }

    @Test
    void testFindWord_NotFound() {
        char[][] grid = {
                {'A', 'B', 'C'},
                {'D', 'E', 'F'},
                {'G', 'H', 'I'}
        };
        List<int[]> result = XMasWord.findWord(grid, "XMAS");
        assertTrue(result.isEmpty());
    }

    @Test
    void testFindCrosses_Found() {
        char[][] grid = {
                {'M', 'A', 'M'},
                {'A', 'A', 'A'},
                {'S', 'A', 'S'}
        };
        assertEquals(1, XMasWord.findCrosses(grid));
    }

    @Test
    void testFindCrosses_NotFound() {
        char[][] grid = {
                {'M', 'A', 'S'},
                {'X', 'A', 'M'},
                {'S', 'A', 'S'}
        };
        assertEquals(0, XMasWord.findCrosses(grid));
    }
}