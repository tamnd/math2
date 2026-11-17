---
tag: 7E6HPE5KJA
kind: example
name: The last number on the board cannot be 0
msc: ["00A35", "05A99"]
topics: [958EF46EYJ]
audience: school
instance_of: [6F55216R53]
uses: [6F55216R53]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_(mathematics)
    locator: lead section
---

## Example

The numbers $1, 2, \ldots, 10$ are written on a board.
A move erases two numbers $a$ and $b$ and writes $|a - b|$ in their place.
After $9$ moves one number is left.
Statement: that number cannot be $0$.
We give a [[proof of impossibility|6F55216R53]] by an invariant.

1. Let $S$ be the sum of the numbers on the board. At the start, $S = 1 + 2 + \cdots + 10 = 55$, which is odd.
2. A move replaces $a + b$ in the sum by $|a - b|$. The change is $(a + b) - |a - b| = 2\min(a, b)$, an even number.
3. So each move keeps the parity of $S$: the parity is an invariant.
4. After $9$ moves the board shows one number, equal to the final $S$. By step 3, it is odd.
5. The number $0$ is even, so the last number cannot be $0$.

## Remarks

The proof does not look at any particular sequence of moves.
There are very many sequences, and the invariant rules all of them out at once.

The parity argument depends on the starting numbers.
For $1, 2, 3$, the sum is $6$, and the last number can be $0$ or not, depending on the moves.
Replacing $1$ and $2$ by $1$, then $1$ and $3$ by $2$, leaves $2$.
Replacing $1$ and $3$ by $2$, then $2$ and $2$ by $0$, leaves $0$.
For $1, 2, \ldots, n$ the sum is $\frac{n(n + 1)}{2}$, which is odd exactly when $n$ leaves remainder $1$ or $2$ on division by $4$.

## Explanations

### L1 human

Start with the numbers $1$ to $10$ and keep replacing two numbers by their difference.
Some quantity must stay the same through all the moves, or the question would be hopeless to answer.
Here it is "the total is odd".
Adding two numbers and taking their difference instead always changes the total by an even amount.
The total starts odd, so it stays odd, and the last number, which is the total at the end, is odd and cannot be $0$.

### L2 human

We use an invariant in another game.
A box holds $5$ red and $6$ blue balls.
A move takes out two balls; if they have the same colour, a blue ball is put in, and if they differ, a red ball is put in.
At the end one ball is left, and we show that it is red.

1. A move with two reds removes $2$ reds. A move with two blues removes one blue and keeps the reds. A move with one red and one blue removes one blue and keeps the reds.
2. In each case the number of red balls changes by $0$ or $-2$, so its parity is an invariant.
3. At the start there are $5$ reds, an odd number. So at the end the number of reds is odd.
4. With one ball left, the number of reds is $0$ or $1$; it is odd, so it is $1$, and the last ball is red.

The typical use: list the moves, compute how each one changes a candidate quantity, and look for a parity or remainder that never changes.

A trap: the invariant must be checked for every kind of move.
The total number of balls is not a useful invariant here, since it changes at each move.
