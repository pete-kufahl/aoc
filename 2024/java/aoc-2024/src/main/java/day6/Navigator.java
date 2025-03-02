package day6;

import java.util.*;

class Navigator {
    public static class Position {
        int x, y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private char[][] maze;
    private int mazeHeight, mazeWidth;
    private char obstacle;
    private List<Direction> directions;
    private int startIndex, currentIndex;
    private Map<String, Set<Position>> pathTraversed;
    public boolean trappedInLoop;

    public Navigator(char[][] grid, char obstacle, char startDirection) {
        this.maze = grid;
        this.mazeHeight = grid.length;
        this.mazeWidth = grid[0].length;
        this.obstacle = obstacle;

        this.directions = Arrays.asList(this::goUp, this::goRight, this::goDown, this::goLeft);
        this.startIndex = getDirectionIndex(startDirection);
        this.currentIndex = this.startIndex;

        this.pathTraversed = new HashMap<>();
        for (Direction dir : directions) {
            pathTraversed.put(dir.getName(), new HashSet<>());
        }

        this.trappedInLoop = false;
    }

    private int getDirectionIndex(char direction) {
        return "^>v<".indexOf(direction);
    }

    private boolean isCycle(Direction dir, Position pos) {
        Set<Position> visited = pathTraversed.get(dir.getName());
        if (visited.contains(pos)) {
            return true;
        } else {
            visited.add(pos);
            return false;
        }
    }

    private boolean isEscaping(int x, int y) {
        return x < 0 || x >= mazeHeight || y < 0 || y >= mazeWidth;
    }

    private boolean isValidMove(int x, int y) {
        return maze[x][y] != obstacle;
    }

    private Position goUp(Position pos) {
        return new Position(pos.x - 1, pos.y);
    }

    private Position goRight(Position pos) {
        return new Position(pos.x, pos.y + 1);
    }

    private Position goDown(Position pos) {
        return new Position(pos.x + 1, pos.y);
    }

    private Position goLeft(Position pos) {
        return new Position(pos.x, pos.y - 1);
    }

    public Position nextStep(Position currentPos) {
        for (int i = 0; i < 4; i++) {
            Direction dir = directions.get((currentIndex + i) % 4);
            Position newPos = dir.move(currentPos);

            if (isEscaping(newPos.x, newPos.y)) {
                return newPos;
            }
            if (isValidMove(newPos.x, newPos.y)) {
                currentIndex = directions.indexOf(dir);
                trappedInLoop = isCycle(dir, newPos);
                return newPos;
            }
        }
        return null;
    }

    private interface Direction {
        Position move(Position pos);
        default String getName() { return getClass().getSimpleName(); }
    }
}