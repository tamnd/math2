---
tag: FB6HBKEGPR
kind: example
name: A nonlinear system with exactly two solutions
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
not_instance_of:
  - target: 0GT4WWGWH2
    note: the second equation xy = 0 is not linear, and the system has exactly two solutions, which no linear system over the reals can have
uses: [0GT4WWGWH2, 0Q3ZT8J05R]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: lead section
---

## Example

Consider the system over $\mathbb{R}$
$$x + y = 1, \qquad xy = 0.$$
We show that it is not linear and that it has exactly two solutions.

1. The equation $xy = 0$ contains a product of two unknowns, so it is not a [[linear equation|0Q3ZT8J05R]]. So the system is not a [[system of linear equations|0GT4WWGWH2]].
2. A product of real numbers is zero only when a factor is zero, so $xy = 0$ gives $x = 0$ or $y = 0$.
3. If $x = 0$, then the first equation gives $y = 1$. If $y = 0$, it gives $x = 1$.
4. So the solutions are exactly $(0, 1)$ and $(1, 0)$. Check: $0 + 1 = 1$ with $0 \cdot 1 = 0$, and $1 + 0 = 1$ with $1 \cdot 0 = 0$.
5. Their midpoint $(\tfrac12, \tfrac12)$ satisfies $x + y = 1$, but it gives $xy = \tfrac14 \ne 0$.

## Remarks

The example shows that the number of solutions can detect a nonlinear system.
A linear system over $\mathbb{R}$ with two solutions $s \ne t$ also has every point $s + c(t - s)$ as a solution, so it has infinitely many.
So no linear system over $\mathbb{R}$ has the solution set $\set{(0, 1), (1, 0)}$.
Over $\mathbb{F}_2$ the situation changes: there a line has only two points, and the single linear equation $x + y = 1$ has exactly the solutions $(0, 1)$ and $(1, 0)$.

## Explanations

### L1 human

The line $x + y = 1$ meets the two axes in two points.
The equation $xy = 0$ describes the two axes, which together are not one straight line.
That is why we get exactly two answers.

### L2 human

To test whether a set of points could be the solution set of a linear system over $\mathbb{R}$, take two of its points $s$ and $t$ and check the midpoint $\tfrac12 (s + t)$.
If the midpoint is missing, the set is not the solution set of any linear system.
Here the midpoint $(\tfrac12, \tfrac12)$ is missing.
Watch out: the converse fails.
A nonlinear system can still have a line of solutions, for example $x^2 = 0$ in the unknowns $x, y$, whose solutions are the whole $y$-axis.
