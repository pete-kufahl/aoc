package day8;

import org.junit.jupiter.api.Test;

import java.util.Set;

import static org.junit.jupiter.api.Assertions.*;

class AntinodesTest {

    @Test
    void inBounds() {
        char[][] grid = {
                {'.', '.', '.'},
                {'.', 'A', '.'},
                {'.', '.', '.'}
        };

        assertTrue(Antinodes.inBounds(new Node(1, 1), grid));
        assertFalse(Antinodes.inBounds(new Node(-1, 1), grid));
        assertFalse(Antinodes.inBounds(new Node(3, 3), grid));
    }

    @Test
    void findAntinodes_2() {
        char[][] grid = {
                {'.', '.', '.', '.'},
                {'.', 'A', '.', '.'},
                {'.', '.', 'A', '.'},
                {'.', '.', '.', '.'}
        };

        Set<Node> network = Set.of(new Node(1, 1), new Node(2, 2));
        Set<Node> result = Antinodes.findAntinodes(network, grid);

        assertEquals(2, result.size()); // Expect two valid antinodes
//        for (Node n : result) {
//            System.out.println("node at: " + n.x() + ", " + n.y());
//        }
        assertTrue(result.contains(new Node(0, 0)));
        assertTrue(result.contains(new Node(3, 3)));
    }

    @Test
    void findAntinodes_3() {
        char[][] grid = {
                {'.', '.', '.', '.'},
                {'.', 'A', '.', '.'},
                {'.', 'A', 'A', '.'},
                {'.', '.', '.', '.'}
        };

        Set<Node> network = Set.of(new Node(1, 1), new Node(2, 2), new Node(1, 2));
        Set<Node> result = Antinodes.findAntinodes(network, grid);

        assertEquals(6, result.size()); // Expect two valid antinodes
//        for (Node n : result) {
//            System.out.println("node at: " + n.x() + ", " + n.y());
//        }
        assertTrue(result.contains(new Node(0, 0)));
        assertTrue(result.contains(new Node(1, 0)));
        assertTrue(result.contains(new Node(1, 3)));
        assertTrue(result.contains(new Node(0, 2)));
        assertTrue(result.contains(new Node(3, 2)));
        assertTrue(result.contains(new Node(3, 3)));
    }

    @Test
    void findAntinodes_2sets() {
        char[][] grid = {
                {'.', '.', '.', '.'},
                {'.', 'A', 'B', '.'},
                {'.', 'B', 'A', '.'},
                {'.', '.', '.', '.'}
        };

        Set<Node> network = Set.of(new Node(1, 1), new Node(2, 2), new Node(1, 2));
        Set<Node> result = Antinodes.findAntinodes(network, grid);

        assertEquals(6, result.size()); // Expect two valid antinodes
//        for (Node n : result) {
//            System.out.println("node at: " + n.x() + ", " + n.y());
//        }
        assertTrue(result.contains(new Node(0, 0)));
        assertTrue(result.contains(new Node(1, 0)));
        assertTrue(result.contains(new Node(1, 3)));
        assertTrue(result.contains(new Node(0, 2)));
        assertTrue(result.contains(new Node(3, 2)));
        assertTrue(result.contains(new Node(3, 3)));
    }

    @Test
    void findCollinearPoints() {
        char[][] grid = {
                {'.', '.', '.', '.'},
                {'.', 'A', '.', '.'},
                {'.', '.', 'A', '.'},
                {'.', '.', '.', '.'}
        };

        Set<Node> network = Set.of(
                new Node(1, 1),
                new Node(2, 2)
        );
        Set<Node> result = Antinodes.findCollinearPoints(network, grid);

        assertTrue(result.contains(new Node(3, 3))); // Collinear point
        assertFalse(result.contains(new Node(4, 4))); // Out of bounds
    }
}