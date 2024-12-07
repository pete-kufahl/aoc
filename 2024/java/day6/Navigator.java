import java.util.*;

public class Navigator {
    /**
     * Class for storing and cycling through the navigator of a 2D text maze
     */
    private char[][] maze;
    private int mazeHeight;
    private int mazeWidth;
    private char obstacle;
    private int currentIndex;
    private int startIndex;

    // Directional interfaces
    private List<Runnable> directions;
    private Map<String, Set<String>> pathTraversed;

    // Flag to identify loop
    public boolean trappedInLoop;

    // Constructor
    public Navigator(char[][] grid, char obstacle, char startDirection) {
        this.maze = grid;
        this.mazeHeight = grid.length;
        this.mazeWidth = grid[0].length;
        this.obstacle = obstacle;

        // Initialize directions
        this.directions = Arrays.asList(this::goUp, this::goRight, this::goDown, this::goLeft);

        // Set the initial direction index based on the input character
        this.startIndex = getDirectionIndex(startDirection);
        this.currentIndex = this.startIndex;

        // Initialize path traversed
        this.pathTraversed = new HashMap<>();
        this.pathTraversed.put("go_up", new HashSet<>());
        this.pathTraversed.put("go_right", new HashSet<>());
        this.pathTraversed.put("go_down", new HashSet<>());
        this.pathTraversed.put("go_left", new HashSet<>());

        this.trappedInLoop = false;
    }

    // Method to get the direction index from a character
    private int getDirectionIndex(char direction) {
        switch (direction) {
            case '^': return 0; // Up
            case '>': return 1; // Right
            case 'v': return 2; // Down
            case '<': return 3; // Left
            default: throw new IllegalArgumentException("Invalid start direction: " + direction);
        }
    }

    // Directional movement methods
    private void goUp() {
        // Implement logic for moving up
    }

    private void goRight() {
        // Implement logic for moving right
    }

    private void goDown() {
        // Implement logic for moving down
    }

    private void goLeft() {
        // Implement logic for moving left
    }

    // Getters (if needed)
    public char[][] getMaze() {
        return maze;
    }

    public char getObstacle() {
        return obstacle;
    }

    public int getCurrentIndex() {
        return currentIndex;
    }

    public Map<String, Set<String>> getPathTraversed() {
        return pathTraversed;
    }

    public Object[] nextStep(int[] currentPos) {
        /**
         * Cyclically iterates through the directions to determine the next step.
         * Returns an array: {new position as int[], boolean indicating escape}.
         */
        List<Runnable> directionCycle = new ArrayList<>();
        
        // Prepare the direction cycle (cyclic iterator equivalent)
        for (int i = 0; i < 4; i++) {
            directionCycle.add(directions.get((currentIndex + i) % directions.size()));
        }
    
        for (int i = 0; i < 4; i++) {
            Runnable direction = directionCycle.get(i);
    
            // Use a helper method to compute the new position based on the direction
            int[] newPos = computeNewPosition(currentPos, direction);
            int x = newPos[0], y = newPos[1];
    
            if (isEscaping(x, y)) {
                return new Object[]{newPos, true};
            }
    
            if (isValidMove(x, y)) {
                currentIndex = directions.indexOf(direction); // Update direction index
                trappedInLoop = isCycle(direction, newPos); // Check if trapped in a loop
                return new Object[]{newPos, false};
            }
        }
    
        return new Object[]{null, false};
    }
    
}
