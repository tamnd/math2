---
tag: 7NERHHWBWR
kind: definition
name: Integer programming
msc: [90C10]
defines: 9GX3WH5EQF
uses: [VNMXB0J2KA, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Integer_programming
---

## Definition

Let $A$ be a real $m \times n$ [[matrix|0VD9ZSWWJG]], let $b \in \R^m$ and let $c \in \R^n$; usually all entries are rational.
The *integer (linear) program* given by $(A, b, c)$ is the problem
$$\text{maximize } c^T x \quad \text{subject to} \quad A x \le b, \quad x \in \Z^n.$$
A vector $x \in \Z^n$ with $A x \le b$ is a *feasible solution*, and a feasible solution of largest objective value is *optimal*.
When in addition $x \in \set{0, 1}^n$ is required, the program is a *$0$-$1$ integer program* or *binary integer program*.
*Integer programming* is the study and solution of integer programs.

## Remarks

Example: maximize $x_1 + x_2$ subject to $2 x_1 + 2 x_2 \le 3$, $x_1 \ge 0$, $x_2 \ge 0$, $x \in \Z^2$.
The feasible solutions are $(0, 0)$, $(1, 0)$ and $(0, 1)$, so the optimal value is $1$.
The same problem without integrality, a [[linear program|VNMXB0J2KA]], has optimal value $3/2$.

Non-example: maximize $x_1 x_2$ subject to $x \in \set{0, 1, 2}^2$ is a problem in integers, but not an integer linear program, because the objective is not linear.

Many authors use "integer programming" more broadly, for any optimization problem with integer variables, and say "integer linear programming" for the problem above.
Unlike a linear program, a feasible integer program with irrational data can have a bounded objective without attaining a maximum.
With rational data, a feasible integer program is either unbounded or has an optimal solution.
