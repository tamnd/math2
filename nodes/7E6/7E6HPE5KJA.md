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
After $9$ moves one number is left, and we prove that it cannot be $0$.
The proof is a [[proof of impossibility|6F55216R53]] by an invariant.

1. Let $S$ be the sum of the numbers on the board.
   At the start,
   $$S = 1 + 2 + \cdots + 10 = 55,$$
   which is odd.
2. A move replaces $a + b$ in the sum by $|a - b|$, so it lowers the sum by
   $$(a + b) - |a - b| = 2 \min(a, b),$$
   which is an even number.
3. So each move keeps the parity of $S$, and the parity of $S$ is an invariant.
4. After $9$ moves the board shows one number, and that number is the final value of $S$.
   By step 3 it is odd.
5. The number $0$ is even, so the last number cannot be $0$.

Check of step 2: with $a = 7$ and $b = 3$ the sum drops by $10 - 4 = 6 = 2 \cdot 3$.

## Remarks

The proof never looks at a particular sequence of moves.
There are a great many sequences, and the invariant rules out all of them at once.

The conclusion depends on the starting numbers.
For $1, 2, 3$ the sum is $6$, which is even, and the last number can be $0$ or not, depending on the moves.
Replacing $1$ and $2$ by $1$, then $1$ and $3$ by $2$, leaves $2$.
Replacing $1$ and $3$ by $2$, then $2$ and $2$ by $0$, leaves $0$.
For $1, 2, \ldots, n$ the sum is $\frac{n(n + 1)}{2}$, which is odd exactly when $n$ leaves remainder $1$ or $2$ on division by $4$, and for those $n$ the last number is never $0$.

## Explanations

### L1 human

Start with the numbers $1$ to $10$ and keep replacing two numbers by their difference.
To answer the question you need something that stays the same through all the moves, and here it is "the total is odd".
Taking the difference of two numbers instead of their sum always changes the total by an even amount.
The total starts odd, so it stays odd.
The last number is the total at the end, so it is odd and cannot be $0$.

### L2 human

Here is the same idea in another game.
A box holds $5$ red and $6$ blue balls.
A move takes out two balls: if they have the same color, a blue ball is put in, and if they differ, a red ball is put in.
At the end one ball is left, and we show that it is red.
Two reds out and a blue in lower the reds by $2$.
Two blues out and a blue in leave the reds unchanged.
A red and a blue out and a red in leave the reds unchanged as well.
So the number of reds changes by $0$ or $-2$, and its parity never changes.
It starts at $5$, which is odd, so with one ball left the number of reds is odd, hence $1$, and the last ball is red.
The typical use is to list the moves, compute how each one changes a candidate quantity, and look for a parity or remainder that never changes.
Watch out: the total number of balls is no help here, because every move changes it.
