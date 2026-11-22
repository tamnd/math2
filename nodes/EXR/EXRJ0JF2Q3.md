---
tag: EXRJ0JF2Q3
kind: example
name: Tiling a 2^n by 2^n board with one square removed by L-trominoes
msc: ["05B50", "00A35"]
topics: [EEH2F76CYQ]
audience: school
instance_of: [0ASJVEFA9J]
uses: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Tromino
    locator: Rep-tiling and Golomb's tromino theorem
---

## Example

An *L-tromino* is the shape of three unit squares that form an L, that is, a $2 \times 2$ square with one unit square removed.
A *deficient board* is a square board of unit squares with one square removed.
Take an $8 \times 8$ chessboard and remove any one square: can L-trominoes cover the other $63$ squares with no overlap?
The count allows it, since $63 = 3 \cdot 21$, and induction shows that it is always possible.

Claim: for every integer $n \ge 1$ and every square $s$ of the $2^n \times 2^n$ board, the board with $s$ removed can be tiled by L-trominoes.
We prove the claim by [[mathematical induction|0ASJVEFA9J]] on $n$.

1. Let $P(n)$ be the statement "for every square $s$ of the $2^n \times 2^n$ board, the board with $s$ removed can be tiled by L-trominoes".
   The words "for every square" are part of $P(n)$, and the step needs them.
2. Base case $n = 1$.
   A $2 \times 2$ board with one square removed is itself an L-tromino, whichever square is removed, so $P(1)$ holds.
3. Induction step.
   Let $n \ge 1$, and assume $P(n)$.
   Take the $2^{n+1} \times 2^{n+1}$ board and any square $s$ of it.
4. Cut the board along its two middle lines into four quarters.
   Each quarter is a $2^n \times 2^n$ board.
5. The square $s$ lies in exactly one quarter, and which one depends on $s$.
   Each of the other three quarters has one corner square at the center of the big board.
6. Those three corner squares form an L-tromino, because they are three of the four squares around the center point.
   Place one tromino on them.
7. Now each quarter has exactly one square that is removed or already covered.
   In the quarter of $s$ it is $s$, and it can be any square of that quarter; in each other quarter it is the corner square at the center.
8. The hypothesis $P(n)$ holds for every position of the missing square, so it applies to each of the four quarters.
   Each quarter, with its one square taken, can be tiled by L-trominoes.
9. The four tilings and the center tromino together tile the big board with $s$ removed.
   Since $s$ was any square, $P(n + 1)$ holds.
10. By induction, $P(n)$ holds for every $n \ge 1$.

Check the count: a deficient $2^n \times 2^n$ board has $4^n - 1$ squares, and $3$ divides $4^n - 1$ because $4 \equiv 1 \pmod 3$.
So a tiling uses $(4^n - 1)/3$ trominoes: $1$ for $n = 1$, $5$ for $n = 2$ and $21$ for $n = 3$.

## Remarks

The example shows why the induction hypothesis must allow the missing square to be anywhere.
In step 8 the four quarters have their missing squares at four different places, and the quarter of $s$ has it wherever $s$ happens to be.
A weaker claim, such as "the board with a corner square removed can be tiled", cannot carry the step, because the quarter of $s$ need not have $s$ at a corner.
The stronger claim is easier to prove, which is the idea of [[strengthening the induction hypothesis|F94KJC2RXP]].

The case $n = 0$ also holds, since a $1 \times 1$ board with its one square removed is empty and is tiled by no trominoes.
So the induction could start at $n = 0$, and the step from $0$ to $1$ places exactly the center tromino.

The proof is also a recursive algorithm.
It places one tromino at the center, and then tiles the four quarters in the same way, down to $2 \times 2$ boards.

Solomon W. Golomb introduced polyominoes in a 1954 article in the American Mathematical Monthly, and this tiling result is known as Golomb's tromino theorem.

## Explanations

### L1 human

Take a $4 \times 4$ board and cover one square with a coin.
We want to cover the other $15$ squares with L-shaped pieces of three squares, with no overlap.
Cut the board into four $2 \times 2$ corners, and note which corner holds the coin.
Put one L-piece in the middle so that it covers one square of each of the other three corners.
Now each $2 \times 2$ corner has one square taken, and its three free squares form an L.
So $5$ pieces cover the board, wherever the coin is.
For an $8 \times 8$ board, the same cut gives four $4 \times 4$ boards, and we already know how to do those.

### L2 human

We run the proof for $n = 2$, with the removed square in the top left corner.
Number the rows $1$ to $4$ from the top and the columns $1$ to $4$ from the left, and write $(r, c)$ for a square.
The removed square is $s = (1, 1)$, in the top left quarter.
The center squares of the other three quarters are $(2, 3)$, $(3, 2)$ and $(3, 3)$, and the center tromino covers them.
Then each quarter has three free squares that form an L:
$$\{(1, 2), (2, 1), (2, 2)\}, \quad \{(1, 3), (1, 4), (2, 4)\}, \quad \{(3, 1), (4, 1), (4, 2)\}, \quad \{(3, 4), (4, 3), (4, 4)\}.$$
With the center tromino this gives $5$ trominoes, and $(4^2 - 1)/3 = 5$.

Now move $s$ to $(2, 3)$, a center square of the top right quarter.
The center tromino moves to the other three center squares $(2, 2)$, $(3, 2)$ and $(3, 3)$, and each quarter again has one square taken.
The same recipe works for all $16$ positions of $s$.

This is the standard picture of an induction whose step splits an object of size $n + 1$ into several objects of size $n$.
Watch out: if $P(n)$ names one fixed position of the removed square, the hypothesis does not apply to the quarters in step 8, and the proof breaks.
