package day7;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CircuitEvaluatorTest {

    @Test
    void testDirectAssignment() {
        CircuitEvaluator evaluator = new CircuitEvaluator();

        // Direct assignments
        evaluator.parseLine("123 -> x");
        evaluator.parseLine("456 -> y");

        assertEquals(123, evaluator.evaluateWire("x"));
        assertEquals(456, evaluator.evaluateWire("y"));
    }

    @Test
    void testANDOperation() {
        CircuitEvaluator evaluator = new CircuitEvaluator();

        // Test AND operation
        evaluator.parseLine("123 -> x");
        evaluator.parseLine("456 -> y");
        evaluator.parseLine("x AND y -> z");

        assertEquals(72, evaluator.evaluateWire("z"));  // 123 AND 456 = 72
    }

    @Test
    void testOROperation() {
        CircuitEvaluator evaluator = new CircuitEvaluator();

        evaluator.parseLine("123 -> x");
        evaluator.parseLine("456 -> y");
        evaluator.parseLine("x OR y -> z");

        assertEquals(507, evaluator.evaluateWire("z"));  // 123 OR 456 = 507
    }

    @Test
    void testNOTOperation() {
        CircuitEvaluator evaluator = new CircuitEvaluator();

        evaluator.parseLine("123 -> x");
        evaluator.parseLine("NOT x -> y");

        assertEquals(65412, evaluator.evaluateWire("y"));  // ~123 & 0xFFFF = 65412
    }

    @Test
    void testRSHIFTOperation() {
        CircuitEvaluator evaluator = new CircuitEvaluator();

        evaluator.parseLine("123 -> x");
        evaluator.parseLine("x RSHIFT 2 -> y");

        assertEquals(30, evaluator.evaluateWire("y"));  // 123 >> 2 = 30
    }

    @Test
    void testLSHIFTOperation() {
        CircuitEvaluator evaluator = new CircuitEvaluator();

        evaluator.parseLine("123 -> x");
        evaluator.parseLine("x LSHIFT 2 -> y");

        assertEquals(492, evaluator.evaluateWire("y"));  // 123 << 2 = 492
    }

    @Test
    void testCombinedOperations() {
        CircuitEvaluator evaluator = new CircuitEvaluator();

        evaluator.parseLine("123 -> x");
        evaluator.parseLine("456 -> y");
        evaluator.parseLine("x AND y -> z");        // 123 AND 456 = 72
        evaluator.parseLine("NOT z -> w");          // ~72 & 0xFFFF = 65412
        evaluator.parseLine("w OR y -> result");    // 65412 | 456 = 65535

        assertEquals(65535, evaluator.evaluateWire("result"));
    }

    @Test
    void testChainedOperations() {
        CircuitEvaluator evaluator = new CircuitEvaluator();

        // Test chained operations
        evaluator.parseLine("123 -> x");
        evaluator.parseLine("456 -> y");
        evaluator.parseLine("x AND y -> z");
        evaluator.parseLine("z OR x -> result");

        assertEquals(123, evaluator.evaluateWire("result"));  // 72 OR 123 = 123
    }
}
