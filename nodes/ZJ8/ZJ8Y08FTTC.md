---
tag: ZJ8Y08FTTC
kind: statement
role: theorem
name: Hex theorem that the first player wins
msc: [91A46, 05C57]
uses: [SHQ800E0J4, D01Y6FHTZF, N7AAJ2MW5T]
about: [SHQ800E0J4]
sources:
  - url: https://en.wikipedia.org/wiki/Hex_(board_game)
---

## Statement

Let $n \ge 1$ and consider the game of Hex on an $n \times n$ rhombic board of hexagonal cells.
Two players alternately place a stone of their own colour on an empty cell.
Each player owns two opposite sides of the board.
A player wins when her stones contain a chain of adjacent cells joining her two sides.
Then the first player has a winning strategy.

## Remarks

The proof has two steps.
First, a game of Hex cannot end in a draw: when the board is full, exactly one of the two players has a connecting chain.
So Hex is a finite game of perfect information without draws, and one of the two players has a winning strategy.
Second, a [[strategy-stealing argument|D01Y6FHTZF]] rules out the second player.
An extra stone of one's own colour never hurts in Hex.
So the first player could play an arbitrary first move and then follow the second player's supposed winning strategy, and both players would win, which is absurd.
The argument is due to John Nash, and it shows that a winning strategy exists without describing it.
David Gale showed that the no-draw property of Hex is equivalent to the two-dimensional case of the [[Brouwer fixed-point theorem|N7AAJ2MW5T]].
For $n = 1$ the first player wins with her first stone, and for $n = 2$ she wins by playing in one of the two cells of the short diagonal.

## Explanations

### L1 human

Hex is a board game in which each player tries to connect two opposite sides of a diamond-shaped board.
The board can never fill up without one of the players having a connection, so someone always wins.
The theorem says that the player who moves first can always force a win, if she plays perfectly.
Strangely, the proof does not tell her how to do it.

### L2 human

The result is the classic application of the strategy-stealing argument in [[combinatorial game theory|SHQ800E0J4]].
Its two ingredients appear often: a finite game of perfect information without draws is determined, and a symmetric game where extra moves never hurt cannot be a second-player win.
The no-draw property is a discrete topological fact, which is why it is linked to the Brouwer fixed-point theorem.
Finding explicit winning strategies is hard, and it has been done by computer only for small boards.
