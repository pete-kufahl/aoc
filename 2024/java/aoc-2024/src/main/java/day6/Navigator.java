package day6;

import java.util.*;

class Navigator {
    public static class Position {
        int r, c;

        public Position(int r, int c) {
            this.r = r;
            this.c = c;
        }

        public Position(Position pos) {
            this.r = pos.r;
            this.c = pos.c;
        }

        @Override
        public String toString() {
            return "(" + this.r + ", " + this.c + ")";
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Position position = (Position) o;
            return r == position.r && c == position.c;
        }

        @Override
        public int hashCode() {
            return Objects.hash(r, c);
        }
    }

    private char[][] maze;
    private int mazeHeight, mazeWidth;
    private char obstacle;
    private List<Direction> directions;
    private int startIndex, currentIndex;
    private Map<String, Set<Position>> pathTraversed;
    public boolean trappedInLoop;
    public boolean escaped;

    public Navigator(char[][] grid, char obstacle, char startDirection) {
        this.maze = grid;
        this.mazeHeight = grid.length;
        this.mazeWidth = grid[0].length;
        this.obstacle = obstacle;

        // directions is a list of method references.
        // these four methods implement a functional interface Direction (custom, defined below)
        // in nextStep(), they are polled and move() is called on them
        //. the modulo operator and class reflection are used to simulate a cyclic queue
        this.directions = Arrays.asList(this::goUp, this::goRight, this::goDown, this::goLeft);
        this.startIndex = getDirectionIndex(startDirection);
        this.currentIndex = this.startIndex;

        this.pathTraversed = new HashMap<>();
        for (Direction dir : directions) {
            pathTraversed.put(dir.getName(), new HashSet<>());
        }

        this.trappedInLoop = false;
        this.escaped = false;
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

    private boolean isEscaping(int r, int c) {
        return r < 0 || r >= mazeHeight || c < 0 || c >= mazeWidth;
    }

    private boolean isValidMove(int r, int c) {
        return maze[r][c] != obstacle;
    }

    private Position goUp(Position pos) {
        return new Position(pos.r - 1, pos.c);
    }

    private Position goRight(Position pos) {
        return new Position(pos.r, pos.c + 1);
    }

    private Position goDown(Position pos) {
        return new Position(pos.r + 1, pos.c);
    }

    private Position goLeft(Position pos) {
        return new Position(pos.r, pos.c - 1);
    }

    public Position nextStep(Position currentPos) {
        for (int i = 0; i < 4; i++) {
            Direction dir = directions.get((currentIndex + i) % 4);
            Position newPos = dir.move(currentPos);

            if (isEscaping(newPos.r, newPos.c)) {
                this.escaped = true;
                return newPos;
            }
            if (isValidMove(newPos.r, newPos.c)) {
                currentIndex = directions.indexOf(dir);
                trappedInLoop = isCycle(dir, newPos);
                this.escaped = false;
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