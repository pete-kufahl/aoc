package day7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TestSequencesTest {

    @Test
    void testTestAddMultSingleOperand() {
        assertTrue(TestSequences.testAddMult(5, new int[]{5}));
        assertFalse(TestSequences.testAddMult(10, new int[]{5}));
    }

    @Test
    void testTestAddMultMultipleOperands() {
        assertTrue(TestSequences.testAddMult(9, new int[]{2, 3, 4}));   // 2 * 3 + 4
        assertFalse(TestSequences.testAddMult(14, new int[]{2, 3, 4})); // ops evaluated L->R, not in order of precedence!
        assertTrue(TestSequences.testAddMult(20, new int[]{2, 3, 4}));
    }

    @Test
    void testTestAddMultExample() {
        assertTrue(TestSequences.testAddMult(190, new int[]{10, 19}));
        assertTrue(TestSequences.testAddMult(3267, new int[]{81, 40, 27}));
        assertFalse(TestSequences.testAddMult(83, new int[]{17, 5}));
        assertFalse(TestSequences.testAddMult(156, new int[]{15, 6}));
        assertFalse(TestSequences.testAddMult(7290, new int[]{6, 8, 6, 15}));
        assertFalse(TestSequences.testAddMult(161011, new int[]{16, 10, 13}));
        assertFalse(TestSequences.testAddMult(21037, new int[]{9, 7, 18, 13}));
        assertFalse(TestSequences.testAddMult(192, new int[]{17, 8, 14}));
        assertTrue(TestSequences.testAddMult(292, new int[]{11, 6, 16, 20}));
    }
}