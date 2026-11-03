---
tag: ZXBVKC1TF6
kind: definition
name: Cutting-plane method
msc: [90C10, 90C57]
defines: PR7VMJN5BH
uses: [9GX3WH5EQF, PYMHHM5Z6F, 0325SGSJAR, 0FQSDC2EQ2, VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Cutting-plane_method
---

## Definition

Let $P = \set{x \in \R^n : A x \le b}$ be a rational [[polyhedron|0325SGSJAR]] and $c \in \R^n$, and consider the [[integer program|9GX3WH5EQF]] of maximizing $c^T x$ over $P \cap \Z^n$.
An inequality $\alpha^T x \le \beta$ is *valid* if every point of $P \cap \Z^n$ satisfies it.
For a point $x^* \in \R^n$, a *cut* for $x^*$ is a valid inequality with $\alpha^T x^* > \beta$.
A *cutting-plane method* is the following iteration, with a procedure that produces a cut for a given non-integral point.

1. Start with $Q = P$.
2. Solve the [[linear program|VNMXB0J2KA]] of maximizing $c^T x$ over $Q$; if it is infeasible or unbounded, stop.
3. Take an optimal vertex $x^*$; if $x^* \in \Z^n$, stop: $x^*$ is optimal for the integer program.
4. Otherwise find a cut $\alpha^T x \le \beta$ for $x^*$, replace $Q$ by $Q \cap \set{x : \alpha^T x \le \beta}$, and go to step 2.

## Remarks

At step 1, $Q$ is the [[linear programming relaxation|PYMHHM5Z6F]].
Since every cut is valid, $Q$ always contains $P \cap \Z^n$, so the value at each step is an upper bound for the integer optimum.
An integral optimal $x^*$ of a relaxation is therefore optimal for the integer program.
The ideal relaxation is the [[convex hull|0FQSDC2EQ2]] of $P \cap \Z^n$, which is a rational polyhedron.

Example: maximize $x_2$ subject to $2 x_2 \le 2 x_1 + 1$, $2 x_2 \le 3 - 2 x_1$, $0 \le x_1 \le 1$, $x_2 \ge 0$, $x \in \Z^2$.
The relaxation has the optimal vertex $(1/2, 1)$.
The inequality $x_2 \le 0$ is valid: an integer point with $x_2 \ge 1$ would need $x_1 \ge 1/2$ and $x_1 \le 1/2$, which no integer $x_1$ satisfies.
It cuts off $(1/2, 1)$, and the new relaxation is the segment from $(0, 0)$ to $(1, 0)$, whose vertices are integral optimal points with value $0$.

Non-example: the inequality $x_2 \le 1$ is valid in this example but is not a cut for $(1/2, 1)$, since that point satisfies it.

Whether the method terminates depends on the cuts; with [[Gomory's fractional cuts|AZJMC8A93H]] and suitable rules for pure integer programs it terminates after finitely many steps.
In practice cuts are combined with branching in [[branch and cut|AJ786D5KK7]].
