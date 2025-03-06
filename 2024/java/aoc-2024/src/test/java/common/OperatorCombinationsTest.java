package common;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class OperatorCombinationsTest {

    @Test
    void generate() {
        List<char[]> combinations = OperatorCombinations.generate(2, new char[]{'+', '*', '|'});
        assertEquals(9, combinations.size());
        assertArrayEquals(new char[]{'+', '+'}, combinations.get(0));
        assertArrayEquals(new char[]{'*', '+'}, combinations.get(1));
        assertArrayEquals(new char[]{'|', '+'}, combinations.get(2));
        assertArrayEquals(new char[]{'+', '*'}, combinations.get(3));
        assertArrayEquals(new char[]{'*', '*'}, combinations.get(4));
        assertArrayEquals(new char[]{'|', '*'}, combinations.get(5));
        assertArrayEquals(new char[]{'+', '|'}, combinations.get(6));
        assertArrayEquals(new char[]{'*', '|'}, combinations.get(7));
        assertArrayEquals(new char[]{'|', '|'}, combinations.get(8));
    }
}