---
tag: JPSCHKN0QP
kind: statement
role: theorem
name: Strong duality theorem of linear programming
msc: [90C05, 90C46]
uses: [14VMJNXMDC, 50026WSZNF, FYZC634H2D, T7Y2GVS1FQ]
about: [14VMJNXMDC]
sources:
  - url: https://en.wikipedia.org/wiki/Strong_duality
  - url: https://en.wikipedia.org/wiki/Dual_linear_program
---

## Statement

Let $A$ be a real $m \times n$ matrix, let $b \in \R^m$ and let $c \in \R^n$.
Let (P) be "maximize $c^T x$ subject to $A x \le b$, $x \ge 0$", and let (D) be its [[dual linear program|14VMJNXMDC]] "minimize $b^T y$ subject to $A^T y \ge c$, $y \ge 0$".

1. If (P) or (D) has an optimal solution, then both have optimal solutions $x^*$ and $y^*$, and $c^T x^* = b^T y^*$.
2. If (P) and (D) are both feasible, then both have optimal solutions, with equal optimal values.

## Remarks

Part 2 follows from part 1 and [[weak duality|50026WSZNF]]: a feasible dual point bounds the primal above, so the primal is bounded and has an optimum.
Part 1 is proved with [[Farkas' lemma|FYZC634H2D]].
If $x^*$ is optimal with value $\gamma$, the system $A x \le b$, $x \ge 0$, $c^T x \ge \gamma + \varepsilon$ has no solution for each $\varepsilon > 0$.
A version of Farkas' lemma for inequalities then gives $y \ge 0$ with $A^T y \ge c$ and $b^T y < \gamma + \varepsilon$, so the dual optimum equals $\gamma$.

Example: for "maximize $x_1 + x_2$ subject to $x_1 + 2 x_2 \le 4$, $3 x_1 + x_2 \le 6$, $x \ge 0$", the point $x^* = (8/5, 6/5)$ has value $14/5$.
The dual point $y^* = (2/5, 1/5)$ satisfies $y_1 + 3 y_2 = 1 \ge 1$ and $2 y_1 + y_2 = 1 \ge 1$, and $4 y_1 + 6 y_2 = 14/5$.
By weak duality both are optimal, as the theorem predicts.

The other cases are also possible: (P) infeasible with (D) unbounded, (P) unbounded with (D) infeasible, or both infeasible.
For example, with $A = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$, $b = (-1, -1)^T$ and $c = (1, 1)^T$, both programs are infeasible.

## Explanations

### L1 human

A linear program and its dual look at the same situation from two sides: one pushes a value up, the other pushes a bound down.
The theorem says that they meet: the best value of the primal equals the best bound from the dual.
So an optimal solution can always be proved optimal by exhibiting a dual solution with the same value.

### L2 human

Strong duality is the central theorem of linear programming.
It gives short certificates of optimality, it underlies complementary slackness, and it yields the max-flow min-cut theorem and the minimax theorem for zero-sum matrix games.
The simplex algorithm proves it constructively: at termination, the vector $y^T = c_B^T A_B^{-1}$ is an optimal dual solution.
For general convex programs the analogue needs a constraint qualification such as Slater's condition; for linear programs no such hypothesis is needed.
