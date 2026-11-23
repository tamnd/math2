---
tag: 6RA1FTFWYR
kind: example
name: A Chvátal-Gomory cut for three pairwise exclusions
msc: ["03F20", "90C10"]
topics: [CBAF7J051K]
audience: research
instance_of: [KKCX2HQP2K]
uses: [KKCX2HQP2K, AZJMC8A93H]
sources:
  - url: https://en.wikipedia.org/wiki/Cutting-plane_method
    locator: Gomory's cut
---

## Example

Take the three lines $x + y \leq 1$, $y + z \leq 1$ and $x + z \leq 1$ in the variables $x, y, z$.
They are the lines of the clauses $\neg x \vee \neg y$, $\neg y \vee \neg z$ and $\neg x \vee \neg z$, which say that no two of $x, y, z$ are true.
In the pigeonhole formulas they are the hole clauses of one hole and three pigeons.
We derive $x + y + z \leq 1$ in [[cutting planes|KKCX2HQP2K]] with two additions and one division.

1. In the $\geq$ form the three lines are $-x - y \geq -1$, $-y - z \geq -1$ and $-x - z \geq -1$.
2. Linear combination of the first two with weights $1$ and $1$ gives $-x - 2y - z \geq -2$.
3. Linear combination of this line with the third gives $-2x - 2y - 2z \geq -3$.
4. Every coefficient is $-2$, so the division rule applies with $c = 2$.
   It gives the following line:
   $$-x - y - z \geq \lceil -3/2 \rceil = -1.$$
5. The least integer that is at least $-1.5$ is $-1$, so the rounding is correct.
   In the $\leq$ form the result reads $x + y + z \leq \lfloor 3/2 \rfloor = 1$.

The derivation has length $6$: three axioms and three derived lines.
The derived line is a Chvátal-Gomory cut.

## Remarks

The cut removes the point $(1/2, 1/2, 1/2)$.
At this point $x + y = y + z = x + z = 1$, so the point satisfies the three lines, and it satisfies the Boolean axioms since each coordinate lies in $[0, 1]$.
But $x + y + z = 3/2 > 1$, so it violates the cut.
Every linear combination of the axioms with non-negative weights holds at $(1/2, 1/2, 1/2)$, so no derivation without division reaches $x + y + z \leq 1$.

The cut keeps every $0$-$1$ solution.
A $0$-$1$ point that satisfies the three lines has at most one coordinate equal to $1$, so it satisfies $x + y + z \leq 1$.

What changes with more variables?
For $m$ variables with all pairwise lines $x_i + x_j \leq 1$, each variable occurs in $m - 1$ lines.
The sum of all the lines is therefore
$$(m - 1) \sum_i x_i \leq \binom{m}{2},$$
and division by $m - 1$ gives $\sum_i x_i \leq \lfloor m/2 \rfloor$.
For $m = 3$ this is the cut above, but for $m \geq 4$ it is too weak.
The [[pigeonhole refutation|13Y3JADJ8G]] reaches $\sum_i x_i \leq 1$ by adding one variable at a time, with one division for each new variable.
In integer programming the cut is the clique inequality of a triangle, a cut of the same kind as the [[Gomory fractional cut|AZJMC8A93H]].

## Explanations

### L1 human

Three lamps are given, and no two of them may be on at the same time.
Then at most one lamp is on.
If lamps could be half on, all three could be half on, since each pair would give $1/2 + 1/2 = 1$.
Adding the three rules gives "two times the total is at most $3$", so the total is at most $1.5$.
The total is a whole number, so it is at most $1$, and this removes the half-on point.

### L2 human

A Chvátal-Gomory cut has three steps.

1. Choose non-negative weights for the lines, here $1, 1, 1$.
2. Add the weighted lines, here $2x + 2y + 2z \leq 3$.
3. Divide by a common factor of the coefficients and round the right side, here $3/2$ down to $1$.

The typical use is to remove a fractional vertex of the linear relaxation.
Watch out: the factor must divide every coefficient on the left side.
From $2x + 2y + z \leq 3$ one may not divide by $2$, as [[rounding without divisibility|3619VP5J7J]] shows.
