# Text-Based Tic Tac Toe in Python: Build Guide

A concept-first guide. No code here on purpose. The goal is for you to understand the game well enough to write it yourself, then upgrade it with special features.

---

## 1. What You're Building

A two-player (and later, player vs computer) Tic Tac Toe game that runs in the terminal.

- The board is a 3x3 grid.
- One player is **X**, the other is **O**.
- Players take turns placing their mark on an empty square.
- First player to get **3 in a row** (horizontal, vertical or diagonal) wins.
- If all 9 squares fill up and nobody has won, it's a **draw**.

---

## 2. How the Game Works (The Big Picture)

Every turn-based game runs on the same idea: a **game loop**. The loop keeps repeating until something ends the game.

```
Show board  →  Ask current player for a move  →  Validate the move
     ↑                                                    ↓
Switch player  ←  Check for draw  ←  Check for win  ←  Place the mark
```

Each pass through the loop is one turn. The loop stops when someone wins or the board is full.

### The 6 jobs your program has to do

| # | Job | What it means |
|---|-----|---------------|
| 1 | Store the board | Keep track of what's in each of the 9 squares |
| 2 | Display the board | Print it so players can see the current state |
| 3 | Take input | Ask the current player where they want to play |
| 4 | Validate input | Reject bad moves (wrong number, taken square, not a number) |
| 5 | Check the result | After each move, decide: win, draw, or keep going |
| 6 | Switch turns | Hand control to the other player |

If you build each job as its own function, the whole game becomes easy to read, test and upgrade.

---

## 3. The Logic Behind Each Part

### 3.1 Representing the board

You need a way to remember 9 squares. The simplest idea is a **list of 9 items**, one per square, where each item is either empty, X or O.

Players need a way to point at a square, so number the squares 1 to 9:

| 1 | 2 | 3 |
|---|---|---|
| **4** | **5** | **6** |
| **7** | **8** | **9** |

Think about this: players type 1-9, but a Python list starts counting at 0. You'll need to convert between the two. This off-by-one gap is the most common beginner bug in this project.

### 3.2 Displaying the board

Printing is just formatting. For each row, show the three squares separated by vertical bars, and put horizontal lines between rows. Empty squares can show their number so the player knows what to type, or show a blank space. Showing numbers in empty squares is friendlier.

Clear or separate the screen between turns so the board doesn't scroll away.

### 3.3 Taking and validating input

A move is only valid if **all** of these are true:

1. The input is a number (not letters, not empty)
2. The number is between 1 and 9
3. That square is not already taken

If any check fails, show a clear message and ask again. **Don't switch turns on an invalid move.** The same player tries again. Use a loop that only exits when the move is valid.

### 3.4 Checking for a win

This is the heart of the game. There are only **8 possible winning lines** on a 3x3 board:

| Type | Lines (using square numbers) |
|------|------------------------------|
| Rows | 1-2-3, 4-5-6, 7-8-9 |
| Columns | 1-4-7, 2-5-8, 3-6-9 |
| Diagonals | 1-5-9, 3-5-7 |

Store these 8 combinations once. After every move, check each line: are all three squares in that line the same mark, and not empty? If yes for any line, the current player wins.

**Optimization to understand:** you only need to check after a move, and only for the player who just moved. The other player can't have just won.

### 3.5 Checking for a draw

A draw means: the board is completely full **and** nobody has won. Order matters here. Always check for a win **first**, then check for a draw. Otherwise a player who wins on the 9th move would wrongly be told it's a draw.

### 3.6 Switching turns

Keep a variable that tracks whose turn it is. After a valid move that doesn't end the game, flip it: X becomes O, O becomes X.

### 3.7 Ending the game

When the loop ends, print the result (who won, or draw), then ask if they want to play again. If yes, reset the board and start over.

---

## 4. Special Features to Add

Build the basic game first. Then add these in roughly this order, from easiest to hardest.

### Level 1: Quality of life (easy)

- **Play again option.** After a game ends, ask "Play again? (y/n)" instead of quitting.
- **Player names.** Ask for names at the start and use them in prompts ("Ajay's turn (X)").
- **Choose your symbol.** Let player 1 pick X or O.
- **Randomize who starts.** Don't always give X the first move.
- **Quit anytime.** Let a player type "q" to exit mid-game.
- **Clear error messages.** Tell the player exactly what was wrong with their input.

### Level 2: Game tracking (easy to medium)

- **Scoreboard.** Track wins for each player and draws across multiple rounds. Display it after every game.
- **Best of N.** Play best of 3 or best of 5, with a match winner at the end.
- **Move counter.** Show how many moves each game took.
- **Highlight the winning line.** When someone wins, show which three squares won (for example, by using a different marker or colour).

### Level 3: Presentation (medium)

- **Colored output.** X in one colour, O in another, using a terminal colour library.
- **Nicer board design.** Use box-drawing characters for a cleaner grid.
- **Welcome screen and instructions.** A short intro that shows the numbered grid.

### Level 4: Playing against the computer (medium to hard)

This is the feature that turns a toy into something worth putting on LinkedIn. Build it in **three difficulty levels**:

**Easy mode: random.**
The computer picks any empty square at random. Simple, beatable, a good first version.

**Medium mode: rule-based.**
The computer follows a priority list on each turn:
1. If I can win this move, take the winning square.
2. If the opponent could win next move, block that square.
3. Otherwise take the centre if it's free.
4. Otherwise take a corner.
5. Otherwise take any free square.

This feels surprisingly smart and is very beatable only by tricks.

**Hard mode: unbeatable (Minimax).**
The computer simulates every possible future game from the current board, assuming both sides play perfectly, and picks the move with the best guaranteed outcome. The result is a computer that **never loses**. The best you can do against it is draw.

Concept to learn for this one:
- A finished game scores **+1** if the computer wins, **-1** if it loses, **0** for a draw.
- The computer tries every empty square, imagines the opponent's best reply, imagines its own best reply to that, and so on until the game ends.
- It picks the move that leads to the highest score assuming the opponent also plays their best.
- This idea is called **recursion**, and it's a major step up in your Python skills.

### Level 5: Advanced extras (hard)

- **Bigger boards.** Support 4x4 or 5x5 with a configurable "how many in a row to win". This forces you to generate winning lines with logic instead of hardcoding 8 of them.
- **Undo move.** Keep a history of moves so a player can take back their last move.
- **Game replay.** After the game, replay the whole thing move by move.
- **Save stats to a file.** Store total wins, losses and draws so they persist after closing the program.
- **Leaderboard.** Track top players across sessions.
- **Move timer.** Give each player a time limit, and skip or forfeit if they run out.
- **Simple AI vs AI mode.** Watch two computer players battle it out.

---

## 5. Suggested Project Structure

Keep it modular like your Morse code project. Separate files, separate responsibilities:

| File | Responsibility |
|------|----------------|
| `board` | Stores the board, places marks, checks win and draw |
| `player` | Handles player names, symbols and input |
| `computer` | The AI logic for easy, medium and hard modes |
| `game` | The main loop that connects everything |
| `main` | Entry point: menu, play again, scoreboard |

Using classes here makes sense: a `Board` class, a `Player` class and a `Game` class map naturally onto the real-world pieces.

---

## 6. Recommended Build Order

Don't try to build everything at once. Follow these stages and make sure each one works before moving on.

1. **Board only.** Store it and print it. Hardcode a few marks to test the display.
2. **Place a mark.** Let the code put an X or O on a chosen square.
3. **Take input.** Ask for a move and validate it fully.
4. **Add turns.** Alternate X and O in a loop.
5. **Win detection.** Check the 8 lines after each move.
6. **Draw detection.** Handle a full board with no winner.
7. **Play again.** Reset and restart.
8. **Scoreboard and names.**
9. **Easy computer, then medium, then minimax.**
10. **Polish.** Colours, nicer board, saving stats.

---

## 7. Common Bugs to Watch For

| Bug | Cause |
|-----|-------|
| Wrong square gets marked | Forgot to convert the player's 1-9 into the list's 0-8 |
| Crash when typing letters | Didn't check that the input is a number before converting |
| Players can overwrite each other | Didn't check that the square is empty |
| Draw announced when someone won | Checked for draw before checking for win |
| Turn switches after a bad move | Switched players outside the "valid move" branch |
| Game never ends | Loop exit condition never becomes true |
| Computer plays on a full square | AI picks from all squares instead of only empty ones |

---

## 8. Testing Checklist

Before you call it done, try to break it:

- [ ] Win with every one of the 8 lines, as both X and O
- [ ] Fill the board with no winner to confirm the draw message
- [ ] Win on the 9th move to confirm it counts as a win, not a draw
- [ ] Type letters, symbols, empty input, 0, 10 and negative numbers
- [ ] Pick an already-taken square
- [ ] Play multiple rounds and confirm the board fully resets
- [ ] Confirm the scoreboard adds up correctly
- [ ] Play against hard mode and confirm you can never beat it

---

## 9. Turning It Into a LinkedIn Post

What makes this project stand out is the story, not the game. Good angles:

- "I built an AI you can't beat" (Minimax)
- "Same game, three difficulty levels, three different kinds of logic"
- "Everything I learned about recursion from a 3x3 grid"

Show a short screen recording of you losing to hard mode. People love that.

---

## 10. Key Concepts You'll Practise

- Lists and indexing
- Functions and modular code
- Loops and loop control
- Input validation and error handling
- Classes and OOP
- Game state management
- Recursion (Minimax)
- File handling (saving stats)

Build it step by step, and by the end you'll have a project that touches almost every core Python concept.
