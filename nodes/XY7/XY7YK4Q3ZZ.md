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

We want a closed formula for $C_n = 1^3 + 2^3 + \dots + n^3$, with a proof.
We use [[heuristics|6KCEWEP4WA]] to find the formula, and then induction to prove it.

1. We compute small cases: $C_1 = 1$, $C_2 = 9$, $C_3 = 36$, $C_4 = 100$, $C_5 = 225$.
2. We look at the data, and each value is a perfect square: $1 = 1^2$, $9 = 3^2$, $36 = 6^2$, $100 = 10^2$, $225 = 15^2$.
3. The square roots $1, 3, 6, 10, 15$ are the [[triangular numbers|WHN4CBYZXD]]
   $$T_n = 1 + 2 + \dots + n = \frac{n(n+1)}{2}.$$
4. So we conjecture that $C_n = T_n^2$ for every $n \ge 1$.
5. We test the conjecture on a case that we did not use to form it: $C_6 = 225 + 216 = 441$ and $T_6^2 = 21^2 = 441$.
6. The conjecture is about every $n$, and $C_{n+1} = C_n + (n+1)^3$, so we try [[mathematical induction|0ASJVEFA9J]].
7. The base case holds: $C_1 = 1 = \left( \frac{1 \cdot 2}{2} \right)^2$.
8. For the step, we assume $C_n = \frac{n^2 (n+1)^2}{4}$ and add the next cube:
   $$C_{n+1} = \frac{n^2 (n+1)^2}{4} + (n+1)^3 = \frac{(n+1)^2 (n^2 + 4n + 4)}{4}.$$
9. Since $n^2 + 4n + 4 = (n+2)^2$, this is $\left( \frac{(n+1)(n+2)}{2} \right)^2$, the formula for $n + 1$.
10. By induction, $C_n = \left( \frac{n(n+1)}{2} \right)^2$ for every $n \ge 1$.

Steps 1 to 5 are heuristic reasoning, which finds the formula and makes it credible.
Steps 6 to 10 are the proof, which makes it certain.

## Remarks

The example shows the usual division of labor: heuristics find the statement, and a proof method checks it.
The induction needs the formula as input, and it gives no hint of how anyone found the formula.

The same heuristic on the sum of squares $1^2 + 2^2 + \dots + n^2$ gives $1, 5, 14, 30, 55$, and these are not squares.
Here the ratios to $T_n$ help instead:
$$\frac{1}{1}, \ \frac{5}{3}, \ \frac{14}{6} = \frac{7}{3}, \ \frac{30}{10} = 3, \ \frac{55}{15} = \frac{11}{3},$$
which are the values of $\frac{2n+1}{3}$, and they suggest the formula $\frac{n(n+1)(2n+1)}{6}$.
So the advice "look for a pattern" works in both cases, but the pattern to look for is different, and no rule tells you in advance which one to try.

## Explanations

### L1 human

Add cubes: $1 + 8 = 9$, then $1 + 8 + 27 = 36$, then $1 + 8 + 27 + 64 = 100$.
The answers $9$, $36$ and $100$ are the squares of $3$, $6$ and $10$.
And $3 = 1 + 2$, $6 = 1 + 2 + 3$ and $10 = 1 + 2 + 3 + 4$.
So we guess that the sum of the first cubes is the square of the sum of the first numbers.
A guess like this is a good start, and the induction above turns it into a fact.

### L2 human

We repeat the method on $D_n = 1 \cdot 2 + 2 \cdot 3 + \dots + n(n+1)$.
Small cases give $D_1 = 2$, $D_2 = 8$, $D_3 = 20$ and $D_4 = 40$.
These are not squares, so we look for factors instead:
$$2 = \frac{1 \cdot 2 \cdot 3}{3}, \quad 8 = \frac{2 \cdot 3 \cdot 4}{3}, \quad 20 = \frac{3 \cdot 4 \cdot 5}{3}, \quad 40 = \frac{4 \cdot 5 \cdot 6}{3}.$$
So we conjecture $D_n = \frac{n(n+1)(n+2)}{3}$, and the induction step is one line:
$$\frac{n(n+1)(n+2)}{3} + (n+1)(n+2) = \frac{(n+1)(n+2)(n+3)}{3}.$$
Watch out: a formula that fits four values is not yet proved.
The formula $\frac{n(n+1)(n+2)}{3} + (n-1)(n-2)(n-3)(n-4)$ fits the same four values, and at $n = 5$ it gives $94$ instead of the true $70$.
