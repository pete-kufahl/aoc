package day7;

import java.util.HashMap;
import java.util.Map;

public class CircuitEvaluator {
    // wire names and their expressions
    private final Map<String, String> wireMap = new HashMap<>();
    // computer values
    private final Map<String, Integer> computedValues = new HashMap<>();

    public void parseLine(String line) {
        String[] parts = line.split(" -> ");
        String expression = parts[0].trim();
        String wire = parts[1].trim();
        wireMap.put(wire, expression);
    }

    public int evaluateWire(String wire) {
        // if the wire is a number, return its integer value directly
        if (wire.matches("\\d+")) {
            return Integer.parseInt(wire);
        }

        // cached values
        if (computedValues.containsKey(wire)) {
            return computedValues.get(wire);
        }

        String expression = wireMap.get(wire);
        if (expression == null) {
            throw new IllegalArgumentException("Wire not found: " + wire);
        }

        int result;
        if (expression.contains("AND")) {
            String[] parts = expression.split(" AND ");
            result = evaluateWire(parts[0].trim()) & evaluateWire(parts[1].trim());
        } else if (expression.contains("OR")) {
            String[] parts = expression.split(" OR ");
            result = evaluateWire(parts[0].trim()) | evaluateWire(parts[1].trim());
        } else if (expression.contains("NOT")) {
            String operand = expression.replace("NOT ", "").trim();
            result = ~evaluateWire(operand) & 0xFFFF;  // Bitwise NOT and limit to 16-bits
        } else if (expression.contains("RSHIFT")) {
            String[] parts = expression.split(" RSHIFT ");
            result = evaluateWire(parts[0].trim()) >> Integer.parseInt(parts[1].trim());
        } else if (expression.contains("LSHIFT")) {
            String[] parts = expression.split(" LSHIFT ");
            result = evaluateWire(parts[0].trim()) << Integer.parseInt(parts[1].trim());
        } else {
            result = evaluateWire(expression);  // direct assignment
        }

        computedValues.put(wire, result);   // cache
        return result;
    }
}
