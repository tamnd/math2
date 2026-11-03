---
tag: NWBJA4Q208
kind: counterexample
name: Klee–Minty cube
msc: [90C05, 90C60, 52B12]
uses: [MH272QHWPM, VNMXB0J2KA, P9PYM71GMM]
sources:
  - url: https://en.wikipedia.org/wiki/Klee–Minty_cube
same_as:
  wikidata: Q6420102
  wikipedia: Klee–Minty cube
---

## Counterexample

Claim refuted: the [[simplex algorithm|MH272QHWPM]] with Dantzig's largest-coefficient rule needs only polynomially many pivots.

Let $n \ge 1$ and consider the [[linear program|VNMXB0J2KA]] in the variables $x_1, \dots, x_n$:
$$\text{maximize } \sum_{j=1}^{n} 2^{n-j} x_j \quad \text{subject to} \quad \sum_{j=1}^{i-1} 2^{i-j+1} x_j + x_i \le 5^i \ (i = 1, \dots, n), \quad x \ge 0.$$
Its feasible region is a deformed [[cube|P9PYM71GMM]] with $2^n$ vertices, the *Klee–Minty cube*.
Start the simplex algorithm at the vertex $x = 0$, with the slack variables as basis.
Use Dantzig's rule: the entering variable has the largest reduced cost.
Then the algorithm visits all $2^n$ vertices and makes $2^n - 1$ pivots before it reaches the optimum $x = (0, \dots, 0, 5^n)$.

Check for $n = 2$: the program is "maximize $2 x_1 + x_2$ subject to $x_1 \le 5$, $4 x_1 + x_2 \le 25$, $x \ge 0$".
At $(0, 0)$ the reduced costs are $2$ and $1$, so $x_1$ enters, and the ratio test stops at $(5, 0)$, value $10$.
There the objective reads $10 - 2 s_1 + x_2$, so $x_2$ enters, and the ratio test stops at $(5, 5)$, value $15$.
There the objective reads $15 + 2 s_1 - s_2$, so $s_1$ enters, $x_1$ leaves, and the point becomes $(0, 25)$, value $25$.
There the objective reads $25 - 2 x_1 - s_2$, so it is optimal; the run used $3 = 2^2 - 1$ pivots and visited all $4$ vertices.

## Remarks

Victor Klee and George Minty gave this construction in 1972.
It shows that the worst-case running time of the simplex algorithm with Dantzig's rule is exponential in $n$, although the program has only $n$ variables and $n$ constraints.
Variants of the construction defeat many other deterministic pivot rules.
The question whether some pivot rule makes the simplex algorithm polynomial is still open.

## Explanations

### L1 human

The simplex method walks along the edges of a many-sided shape, always uphill, until it reaches the top.
Klee and Minty squashed a cube so cleverly that the steepest uphill choice at each corner leads the method through every single corner before the top.
A cube in $n$ dimensions has $2^n$ corners, so for $n = 50$ the walk would take about $10^{15}$ steps.
In practice the simplex method is fast, and this example shows that the reason is not a worst-case guarantee.
