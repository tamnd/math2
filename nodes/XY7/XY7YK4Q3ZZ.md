---
tag: XY7YK4Q3ZZ
kind: example
name: The sum of the first n cubes found by heuristics
msc: ["00A35", "11B83"]
topics: [X1NSTVGDNQ]
audience: ug1
instance_of: [6KCEWEP4WA]
uses: [6KCEWEP4WA, 0ASJVEFA9J, WHN4CBYZXD]
sources:
  - url: https://en.wikipedia.org/wiki/Squared_triangular_number
    locator: lead section
---

## Example

Problem: find a closed formula for $C_n = 1^3 + 2^3 + \cdots + n^3$, and prove it.
We first use [[heuristics|6KCEWEP4WA]] to find the formula, and then we prove it.

1. Specialize. We compute the first values: $C_1 = 1$, $C_2 = 9$, $C_3 = 36$, $C_4 = 100$, $C_5 = 225$.
2. Look at the data. Each value is a perfect square: $1 = 1^2$, $9 = 3^2$, $36 = 6^2$, $100 = 10^2$, $225 = 15^2$.
3. Look at the square roots. The numbers $1, 3, 6, 10, 15$ are the [[triangular numbers|WHN4CBYZXD]] $T_n = 1 + 2 + \cdots + n = \frac{n(n+1)}{2}$.
4. Conjecture. $C_n = T_n^2 = \left(\frac{n(n+1)}{2}\right)^2$ for every $n \ge 1$.
5. Test the conjecture on a new case before trying to prove it. $C_6 = 225 + 216 = 441$, and $T_6^2 = 21^2 = 441$. The test passes.
6. Plan a proof. The conjecture is a statement about every $n$, and $C_{n+1} = C_n + (n+1)^3$, so we try [[mathematical induction|0ASJVEFA9J]].
7. Base case. $C_1 = 1 = \left(\frac{1 \cdot 2}{2}\right)^2$.
8. Induction step. Assume $C_n = \frac{n^2(n+1)^2}{4}$. Then $C_{n+1} = \frac{n^2(n+1)^2}{4} + (n+1)^3 = \frac{(n+1)^2 (n^2 + 4n + 4)}{4}$.
9. Since $n^2 + 4n + 4 = (n+2)^2$, we get $C_{n+1} = \left(\frac{(n+1)(n+2)}{2}\right)^2$, which is the formula for $n + 1$.
10. By induction, $C_n = \left(\frac{n(n+1)}{2}\right)^2$ for every $n \ge 1$.

Steps 1 to 5 are heuristic reasoning: they find the formula and make it credible.
Steps 6 to 10 are the proof: they make it certain.

## Remarks

The example shows the usual division of labour: heuristics find the statement, and a proof method checks it.
The induction proof needs the formula as input, and it gives no hint of how the formula was found.

The same heuristic on the sum of squares $1^2 + 2^2 + \cdots + n^2$ gives $1, 5, 14, 30, 55$, which are not squares.
There the ratios to $T_n$ help instead: they are $1, \frac{5}{3}, \frac{7}{3}, 3, \frac{11}{3}$, that is, $\frac{2n + 1}{3}$, which suggests the formula $\frac{n(n+1)(2n+1)}{6}$.
So the heuristic "look for a pattern" works in both cases, but the pattern to look for is different.

## Explanations

### L1 human

Add the cubes $1 + 8 = 9$, then $1 + 8 + 27 = 36$, then $1 + 8 + 27 + 64 = 100$.
The answers $9$, $36$ and $100$ are the squares of $3$, $6$ and $10$.
And $3 = 1 + 2$, $6 = 1 + 2 + 3$, $10 = 1 + 2 + 3 + 4$.
So we guess: the sum of the first cubes is the square of the sum of the first numbers.
A guess like this is a good start, but we still need a proof, and the induction above gives one.

### L2 human

We repeat the method on the sum $D_n = 1 \cdot 2 + 2 \cdot 3 + \cdots + n(n+1)$.

1. Specialize: $D_1 = 2$, $D_2 = 8$, $D_3 = 20$, $D_4 = 40$.
2. Look for factors: $2 = \frac{1 \cdot 2 \cdot 3}{3}$, $8 = \frac{2 \cdot 3 \cdot 4}{3}$, $20 = \frac{3 \cdot 4 \cdot 5}{3}$, $40 = \frac{4 \cdot 5 \cdot 6}{3}$.
3. Conjecture: $D_n = \frac{n(n+1)(n+2)}{3}$.
4. Prove by induction: $\frac{n(n+1)(n+2)}{3} + (n+1)(n+2) = \frac{(n+1)(n+2)(n+3)}{3}$.

The typical use: compute, factor, guess, test one more case, then prove.

A trap: a formula that fits four values is not yet proved.
For example, $\frac{n(n+1)(n+2)}{3} + (n-1)(n-2)(n-3)(n-4)$ also fits the four values, and it gives $94$ instead of $70$ at $n = 5$.
