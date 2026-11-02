---
tag: 178GG6TXKQ
kind: statement
role: theorem
name: Liénard's theorem
msc: [34C07, 34C25, 34C15]
uses: [0AAQ73WRFB, 0VW90BBSJ4, 0FP31SX5EA, 0EW1X61ZT1]
about: [0AAQ73WRFB]
sources:
  - url: https://en.wikipedia.org/wiki/Li%C3%A9nard_equation
---

## Statement

Let $f, g \colon \R \to \R$ be [[continuously differentiable|0VW90BBSJ4]], and let $F(x) = \int_0^x f(s)\, ds$.
Assume:

1. $f$ is an [[even function|0FP31SX5EA]] and $g$ is an odd function;
2. $g(x) > 0$ for all $x > 0$;
3. $F$ has exactly one positive zero $a$, with $F(x) < 0$ for $0 < x < a$;
4. $F$ is increasing on $(a, \infty)$, and $F(x) \to \infty$ as $x \to \infty$.

Then the system $x' = y - F(x)$, $y' = -g(x)$, equivalent to $x'' + f(x) x' + g(x) = 0$, has exactly one [[limit cycle|0AAQ73WRFB]].
This limit cycle surrounds the origin, and it is stable.

## Remarks

The proof uses the energy $E(x, y) = \frac{1}{2} y^2 + G(x)$, where $G(x) = \int_0^x g(s)\, ds$.
Along solutions, $E' = -g(x) F(x)$.
By the symmetry $(x, y) \mapsto (-x, -y)$, it is enough to follow a solution from a point $(0, y_0)$ with $y_0 > 0$ to its next crossing of the $y$-axis.
Let $\Delta(y_0)$ be the change of $E$ on this half turn.
It is positive when the half turn stays in $0 \le x \le a$.
For the half turns that go beyond $x = a$, it decreases strictly in $y_0$ and tends to $-\infty$.
So $\Delta$ vanishes for exactly one $y_0$, and this gives the unique closed orbit.

For the van der Pol equation $x'' - \mu (1 - x^2) x' + x = 0$ with $\mu > 0$, one has $F(x) = \mu (x^3/3 - x)$ and $g(x) = x$.
Here $a = \sqrt{3}$, $F < 0$ on $(0, \sqrt{3})$, and $F' = \mu (x^2 - 1) > 0$ for $x > \sqrt{3}$.
So the van der Pol oscillator has exactly one limit cycle, and it is stable.

## Explanations

### L1 human

Liénard's theorem gives easy conditions under which an oscillator has one and only one self-sustained oscillation.
The friction must be negative for small motions and positive for large ones, with a single change of sign.
Then every motion except the rest state spirals onto the same closed loop.

### L2 human

Proving that a limit cycle exists is often done with the [[Poincaré–Bendixson theorem|0EW1X61ZT1]], but that theorem says nothing about how many there are.
Liénard's theorem gives existence and uniqueness at once for a whole family of equations.
Its proof is a careful estimate of how the energy changes on a half turn around the origin.
The van der Pol oscillator is the main application.
