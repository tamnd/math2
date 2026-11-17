---
tag: NSCRV68VNS
kind: example
name: Two numbers with sum 10 and product 21, in symmetric notation
msc: ["00A35", "12D10"]
topics: [X1NSTVGDNQ]
audience: school
instance_of: [6CVYB413ER]
uses: [6CVYB413ER, H840D9TM2X, 0M8EWQJ1YV]
sources:
  - url: https://en.wikipedia.org/wiki/Vieta%27s_formulas
    locator: lead section
---

## Example

Problem: find all pairs of real numbers $x$, $y$ with $x + y = 10$ and $xy = 21$.
The two unknowns play the same role: exchanging $x$ and $y$ does not change the conditions.
We [[introduce a notation|6CVYB413ER]] that keeps this [[symmetry|H840D9TM2X]].

1. The mean of the two numbers is $\frac{x + y}{2} = 5$. Each number is the mean plus or minus a distance $d$.
2. Notation: $x = 5 + d$ and $y = 5 - d$. With these names, $x + y = 10$ holds for every $d$, so the first condition is used up.
3. The second condition becomes $(5 + d)(5 - d) = 21$.
4. The left side is a difference of squares: $(5 + d)(5 - d) = 25 - d^2$.
5. So $25 - d^2 = 21$, that is, $d^2 = 4$, and $d = 2$ or $d = -2$.
6. For $d = 2$: $x = 7$, $y = 3$. For $d = -2$: $x = 3$, $y = 7$.
7. Check: $7 + 3 = 10$ and $7 \cdot 3 = 21$.

The solutions are $(x, y) = (7, 3)$ and $(x, y) = (3, 7)$.
The two values of $d$ give the same pair of numbers in the two orders, as the symmetry predicts.

## Remarks

The symmetric names reduce the problem to $d^2 = 4$, an equation without a linear term.
The names $x$ and $10 - x$ lead to $x^2 - 10x + 21 = 0$, which needs the [[quadratic formula|0KYZXYDGQZ]] or a factorization; the result is the same.
For a general sum $s$ and product $p$, the names $\frac{s}{2} + d$ and $\frac{s}{2} - d$ give $d^2 = \frac{s^2}{4} - p$.
So real solutions exist exactly when $s^2 \geq 4p$, and the two numbers are equal exactly when $s^2 = 4p$.
For $s = 10$ and $p = 26$, $d^2 = -1$, and there are no real solutions.
This is the derivation of the quadratic formula for $t^2 - st + p = 0$, whose roots are the two numbers, by [[Vieta's formulas|0M8EWQJ1YV]].

## Explanations

### L1 human

Two numbers add up to $10$, so on average each is $5$.
One is a little more than $5$ and the other is the same amount less.
Call the amount $d$: the numbers are $5 + d$ and $5 - d$.
Their product is $25$ minus $d$ times $d$, and it must be $21$, so $d$ times $d$ is $4$ and $d$ is $2$.
The numbers are $7$ and $3$.

### L2 human

We use the same notation for a system in three steps: $x + y = 6$ and $x^3 + y^3 = 72$.

1. Notation: $x = 3 + d$, $y = 3 - d$.
2. Expand: $(3 + d)^3 + (3 - d)^3 = 2 \cdot 27 + 2 \cdot 3 \cdot 3 d^2 = 54 + 18 d^2$, since the odd powers of $d$ cancel.
3. So $54 + 18 d^2 = 72$, $d^2 = 1$, and $\{x, y\} = \{4, 2\}$. Check: $4^3 + 2^3 = 64 + 8 = 72$.

The typical use: in a symmetric system, the odd powers of $d$ cancel, and the degree of the equation in $d$ halves.

A trap: the method needs the symmetry.
For $x + y = 6$ and $x^3 + 2y^3 = 72$, the odd powers of $d$ do not cancel, and the symmetric names give no gain.
