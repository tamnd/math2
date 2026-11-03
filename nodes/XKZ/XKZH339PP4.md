---
tag: XKZH339PP4
kind: definition
name: Mathematical optimization
msc: [90C99, 90C30, 49K99]
defines: W3ZXKT3DS1
uses: [NS0Q42Y3FX, 1TTKMRW8PD, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_optimization
---

## Definition

*Mathematical optimization* (also *mathematical programming*) is the study of [[optimization problems|NS0Q42Y3FX]].
Such a problem asks to minimize or maximize an objective [[function|0EPAT51DXQ]] $f \colon X \to \R$ over a [[feasible region|1TTKMRW8PD]] $F \subseteq X$.
The study covers three questions:

1. whether an optimal solution exists;
2. how optimal solutions are characterized, through necessary and sufficient optimality conditions;
3. how optimal solutions, or good approximations of them, are computed by algorithms.

## Remarks

The field is divided by the type of problem.
In *linear programming*, $f$ is linear and $F$ is given by linear constraints.
In *convex optimization*, $f$ and $F$ are convex.
In *integer* and *combinatorial optimization*, $F$ is a discrete set.
*Continuous optimization* treats $F \subseteq \R^n$.
Problems over spaces of functions belong to the calculus of variations and optimal control.

Example: the problem "maximize $xy$ subject to $2x + 2y = 4$, $x, y \ge 0$" belongs to the field.
Substituting $y = 2 - x$ gives $x(2 - x) = 1 - (x - 1)^2 \le 1$, so the optimum is $x = y = 1$ with value $1$.

Non-example: solving the equation $x^2 = 2$ is not by itself an optimization problem, since there is no objective to minimize or maximize.
It can be recast as one, by minimizing $(x^2 - 2)^2$.
