package day8;

import java.util.HashSet;
import java.util.Set;

public class Antinodes {

    public static boolean inBounds(Node node, char[][] grid) {
        // Check x against columns, y against rows
        return (node.x() >= 0 && node.x() < grid[0].length) &&
                (node.y() >= 0 && node.y() < grid.length);
    }

    public static Set<Node> findAntinodes(Set<Node> network, char[][] grid) {
        Set<Node> antinodes = new HashSet<>();

        for (Node loc1 : network) {
            for (Node loc2 : network) {
                if (loc1.equals(loc2)) continue;

                int diffX = loc1.x() - loc2.x();
                int diffY = loc1.y() - loc2.y();

                Node node1 = new Node(loc1.x() + diffX, loc1.y() + diffY);
                Node node2 = new Node(loc1.x() - diffX, loc1.y() - diffY);

                if (inBounds(node1, grid)) { antinodes.add(node1); }
                if (inBounds(node2, grid)) { antinodes.add(node2); }
            }
        }
        Set<Node> ans = new HashSet<>(antinodes);
        ans.removeAll(network);
        if (ans.size() < antinodes.size()) {
            System.out.println("Removed " + (antinodes.size() - ans.size()) + " from antinodes ....");
        }
        return ans;
    }

    public static Set<Node> findCollinearPoints(Set<Node> network, char[][] grid) {
        Set<Node> antinodes = new HashSet<>();

        for (Node loc1 : network) {
            for (Node loc2 : network) {
                if (loc1.equals(loc2)) continue;

                int diffX = loc1.x() - loc2.x();
                int diffY = loc1.y() - loc2.y();
                int i = 1;
                boolean goPlus = true, goMinus = true;

                while (goPlus && i < 48) {
                    Node node1 = new Node(loc1.x() + i * diffX, loc1.y() + i * diffY);
                    if (inBounds(node1, grid)) {
                        antinodes.add(node1);
                        i++;
                    } else {
                        goPlus = false;
                    }
                }

                i = 1;
                while (goMinus && i < 48) {
                    Node node2 = new Node(loc1.x() - i * diffX, loc1.y() - i * diffY);
                    if (inBounds(node2, grid)) {
                        antinodes.add(node2);
                        i++;
                    } else {
                        goMinus = false;
                    }
                }
            }
        }

        // In Part 2, antenna network locations are considered possible antinodes
        return antinodes;
    }
}
