---
tag: DC2NJW1SRM
kind: definition
name: Linear programming relaxation
msc: [90C10, 90C05, 90C11]
defines: PYMHHM5Z6F
uses: [3PX6EV34QK, VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_programming_relaxation
---

## Definition

Let a [[mixed-integer linear program|3PX6EV34QK]] be given:
$$\text{maximize } c^T x \quad \text{subject to} \quad A x \le b, \quad x_1, \dots, x_p \in \Z,$$
with a real $m \times n$ matrix $A$, $b \in \R^m$, $c \in \R^n$ and $0 \le p \le n$.
Its *linear programming relaxation* is the [[linear program|VNMXB0J2KA]]
$$\text{maximize } c^T x \quad \text{subject to} \quad A x \le b, \quad x \in \R^n,$$
obtained by removing the conditions $x_1, \dots, x_p \in \Z$.

## Remarks

Let $z_{LP}$ be the optimal value of the relaxation and $z_{IP}$ that of the mixed-integer program.
Every feasible solution of the mixed-integer program is feasible for the relaxation, so $z_{LP} \ge z_{IP}$.
If an optimal solution of the relaxation satisfies the integrality conditions, it is optimal for the mixed-integer program.

Example: consider maximizing $x_1 + x_2$ subject to $2 x_1 + 2 x_2 \le 3$, $x \ge 0$, $x \in \Z^2$.
The relaxation has optimal value $3/2$, for instance at $(3/2, 0)$, while the integer program has optimal value $1$.

Non-example: replacing $x \in \Z^n$ by $x \in \set{0, 1}^n$ is a restriction, not a relaxation; and dropping the constraints $A x \le b$ while keeping integrality is a relaxation, but not the linear programming relaxation.

For a $0$-$1$ program, the conditions $x \in \set{0, 1}^n$ are written as $0 \le x \le 1$ and $x \in \Z^n$, so the relaxation keeps the bounds $0 \le x_i \le 1$.
The ratio between $z_{LP}$ and $z_{IP}$, taken in the worst case over a class of instances, is the *integrality gap* of the formulation.
The same integer program can have different formulations whose relaxations differ; a formulation is better when its relaxation is closer to the convex hull of the integer feasible points.
