---
tag: 77RJZCZR8P
kind: definition
name: Nonlinear programming
msc: [90C30]
defines: RAQB00X634
uses: [NS0Q42Y3FX, VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_programming
---

## Definition

Let $f, g_1, \dots, g_m, h_1, \dots, h_p \colon \R^n \to \R$ be functions.
The *nonlinear program* with these data is an [[optimization problem|NS0Q42Y3FX]].
It asks to minimise $f(x)$ over $x \in \R^n$ subject to
$$g_i(x) \le 0 \quad (i = 1, \dots, m) \quad \text{and} \quad h_j(x) = 0 \quad (j = 1, \dots, p),$$
where at least one of the functions $f, g_i, h_j$ is not affine.
*Nonlinear programming* is the study and solution of such problems.

## Remarks

Maximising $f$ is the same as minimising $-f$, and a constraint $g(x) \ge 0$ can be written as $-g(x) \le 0$.
Often the functions are assumed continuously differentiable, so that optimality conditions apply.

Example: maximise $x y$ subject to $2x + 2y = 4$, $x \ge 0$, $y \ge 0$.
As a minimisation, $f(x, y) = -x y$ is not affine, $h_1(x, y) = 2x + 2y - 4$, $g_1 = -x$, $g_2 = -y$.
Substituting $y = 2 - x$ gives $-x(2 - x)$, minimal at $x = 1$, so the optimum is $(1, 1)$.

Non-example: minimise $x + y$ subject to $x - y \le 1$, $x \ge 0$, $y \ge 0$ is a [[linear program|VNMXB0J2KA]], not a nonlinear program, since all functions are affine.
