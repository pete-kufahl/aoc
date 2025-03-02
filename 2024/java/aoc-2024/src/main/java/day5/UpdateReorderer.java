package day5;
import java.util.*;

public class UpdateReorderer {
    public static List<Integer> reorderUpdate(List<int[]> rules, List<Integer> update) {

        Set<Integer> updateElements = new HashSet<>(update);

        List<int[]> applicableRules = new ArrayList<>();
        for (int[] rule : rules) {
            if (updateElements.contains(rule[0]) && updateElements.contains(rule[1])) {
                applicableRules.add(rule);
            }
        }

        Map<Integer, List<Integer>> graph = new HashMap<>();
        Map<Integer, Integer> incomingEdges = new HashMap<>();

        for (int[] rule : applicableRules) {
            graph.computeIfAbsent(rule[0], k -> new ArrayList<>()).add(rule[1]);
            incomingEdges.put(rule[1], incomingEdges.getOrDefault(rule[1], 0) + 1);
            incomingEdges.putIfAbsent(rule[0], 0);
        }

        Deque<Integer> nodesToVisit = new ArrayDeque<>();
        List<Integer> reordered = new ArrayList<>();

        for (int node : update) {
            if (incomingEdges.getOrDefault(node, 0) == 0) {
                nodesToVisit.add(node);
            }
        }

        while (!nodesToVisit.isEmpty()) {
            int node = nodesToVisit.pollFirst();
            reordered.add(node);

            if (graph.containsKey(node)) {
                for (int dest : graph.get(node)) {
                    incomingEdges.put(dest, incomingEdges.get(dest) - 1);
                    if (incomingEdges.get(dest) == 0) {
                        nodesToVisit.add(dest);
                    }
                }
            }
        }

        return reordered;
    }
}
