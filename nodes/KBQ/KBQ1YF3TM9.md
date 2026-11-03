---
tag: KBQ1YF3TM9
kind: definition
name: Dual linear program
msc: [90C05, 90C46]
defines: 14VMJNXMDC
uses: [T7Y2GVS1FQ, VNMXB0J2KA, 09DXWYRD43]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_linear_program
---

## Definition

Let $A$ be a real $m \times n$ matrix, let $b \in \R^m$ and let $c \in \R^n$.
Consider the [[linear program in standard form|T7Y2GVS1FQ]], called the *primal* program:
$$\text{(P)} \quad \text{maximize } c^T x \quad \text{subject to} \quad A x \le b, \quad x \ge 0.$$
Its *dual linear program* is the program over $y \in \R^m$
$$\text{(D)} \quad \text{minimize } b^T y \quad \text{subject to} \quad A^T y \ge c, \quad y \ge 0,$$
where $A^T$ is the [[transpose|09DXWYRD43]] of $A$.

## Remarks

The dual has one variable $y_i$ for each primal constraint and one constraint for each primal variable $x_j$.
Written in standard form as "maximize $-b^T y$ subject to $-A^T y \le -c$, $y \ge 0$", the dual of (D) is again (P).
For other forms of the primal, the rules are: an equality constraint gives a free dual variable, and a free primal variable gives an equality dual constraint.
For example, the dual of "maximize $c^T x$ subject to $A x = b$, $x \ge 0$" is "minimize $b^T y$ subject to $A^T y \ge c$" with $y$ free.

Example: the primal "maximize $x_1 + x_2$ subject to $x_1 + 2 x_2 \le 4$, $3 x_1 + x_2 \le 6$, $x \ge 0$" has the dual "minimize $4 y_1 + 6 y_2$ subject to $y_1 + 3 y_2 \ge 1$, $2 y_1 + y_2 \ge 1$, $y \ge 0$".
The point $y = (2/5, 1/5)$ is dual feasible, since $2/5 + 3/5 = 1$ and $4/5 + 1/5 = 1$, with value $14/5$.

Non-example: "minimize $b^T y$ subject to $A y \ge c$, $y \ge 0$" with $A$ in place of $A^T$ is not the dual; for $m \neq n$ the product $A y$ is not even defined.
