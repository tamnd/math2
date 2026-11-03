---
tag: BSRSKXPJPQ
kind: statement
role: theorem
name: Slater's condition
msc: [90C46, 90C25]
uses: [07Q7CNM5WF, QRXXH28W3A, AXBPKPSENT]
about: [QRXXH28W3A]
sources:
  - url: https://en.wikipedia.org/wiki/Slater%27s_condition
same_as:
  wikidata: Q7538885
  wikipedia: Slater's condition
---

## Statement

Let $f_0, f_1, \dots, f_m \colon \R^n \to \R$ be [[convex functions|07Q7CNM5WF]], let $A$ be a real $p \times n$ matrix and let $b \in \R^p$.
Consider the problem of minimizing $f_0(x)$ subject to $f_i(x) \le 0$ for $1 \le i \le m$ and $Ax = b$, with optimal value $p^*$.
Assume Slater's condition: there is $\tilde x \in \R^n$ with $f_i(\tilde x) < 0$ for all $i$ and $A \tilde x = b$.
If $p^* > -\infty$, then strong duality holds: the [[Lagrange dual|QRXXH28W3A]] has optimal value $d^* = p^*$, and some $\lambda \ge 0$, $\nu$ attain $g(\lambda, \nu) = d^*$.

## Remarks

The proof separates two convex sets in $\R^{1 + m + p}$ by a hyperplane.
One is the set of attainable values $(t, u, v)$ with $f_0(x) \le t$, $f_i(x) \le u_i$ and $Ax - b = v$ for some $x$, and the other is the half-line of values below $p^*$ at $(u, v) = 0$.
The Slater point forces the separating hyperplane to be non-vertical, and its normal gives the dual optimal multipliers.
Affine inequality constraints need only hold, not strictly, at $\tilde x$; for linear programs no strict point is needed at all.

Example: minimize $x^2$ subject to $1 - x \le 0$.
The point $\tilde x = 2$ is a Slater point, and indeed $p^* = d^* = 1$, attained at $\lambda = 2$.

Without a Slater point the conclusion can fail.
For minimize $x$ subject to $x^2 \le 0$, the only feasible point is $0$ and $p^* = 0$.
The dual function is $g(\lambda) = -1/(4\lambda)$ for $\lambda > 0$, so $d^* = 0$ but no $\lambda$ attains it.
For minimize $e^{-x}$ subject to $x^2 / y \le 0$ on the domain $y > 0$, one has $p^* = 1$ but $d^* = 0$, a positive [[duality gap|AXBPKPSENT]].

## Explanations

### L1 human

For convex problems, the best lower bound from the dual is usually exactly the optimum.
Slater's condition is a simple test that guarantees this: some point must satisfy all inequality constraints strictly.
It rules out degenerate feasible sets that are squeezed to a thin set.

### L2 human

Slater's condition is the most used constraint qualification in convex optimization.
With strong duality and attained optima, a primal point and a dual point are both optimal exactly when they satisfy the [[Karush–Kuhn–Tucker conditions|HDWEPH4YG4]].
So it is the bridge from duality theory to optimality conditions, and it also justifies primal-dual and interior-point methods.
The same argument works in infinite dimensions when the strict point lies in the interior of the relevant cone.
