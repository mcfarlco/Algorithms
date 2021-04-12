#3 - Try New Puzzle
$python3 npuzzle.py
$n
$new
$move (tile #)

#4 - Verify Solution
$python3 npuzzle.py
$y
$y
$solution.txt


Solution.txt format -

n # Puzzle size (8, 15, or 24. 8 is standard)
(Tile #) (Tile #) (Tile #) # example show with size n = 8
(Tile #) (Tile #) (Tile #) # if a space is empty, (Tile #) = e
(Tile #) (Tile #) (Tile #)
m # Number of moves to solve
m1 # Tile # of first move
m2 # Tile # of second move
m3 # ...
mm # Tile # of last move


