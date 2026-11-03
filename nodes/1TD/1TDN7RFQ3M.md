---
tag: 1TDN7RFQ3M
kind: definition
name: Alternating direction method of multipliers
msc: [90C25, 65K05, 49M29]
defines: 7571B52BKD
uses: [AX0NJ6NK81, 07Q7CNM5WF]
sources:
  - url: https://en.wikipedia.org/wiki/Augmented_Lagrangian_method
    locator: Alternating direction method of multipliers
---

## Definition

Let $f \colon \R^n \to (-\infty, \infty]$ and $g \colon \R^m \to (-\infty, \infty]$ be [[convex functions|07Q7CNM5WF]].
Let $A$ be a $p \times n$ matrix, $B$ a $p \times m$ matrix and $c \in \R^p$.
Consider the problem of minimizing $f(x) + g(z)$ subject to $Ax + Bz = c$.
For $\rho > 0$ its augmented Lagrangian is
$$L_\rho(x, z, y) = f(x) + g(z) + y^T (Ax + Bz - c) + \frac{\rho}{2} \norm{Ax + Bz - c}^2.$$
The *alternating direction method of multipliers* starts from $z^0 \in \R^m$ and $y^0 \in \R^p$, and for $k \ge 0$:

1. $x^{k+1} \in \arg\min_x L_\rho(x, z^k, y^k)$;
2. $z^{k+1} \in \arg\min_z L_\rho(x^{k+1}, z, y^k)$;
3. $y^{k+1} = y^k + \rho \, (A x^{k+1} + B z^{k+1} - c)$.

## Remarks

Assume $f$ and $g$ are closed and proper, and the Lagrangian $L_0$ has a saddle point.
Then the residual $A x^k + B z^k - c$ tends to $0$, the objective values tend to the optimal value, and $y^k$ tends to a dual optimal point.

Example: for $a \in \R$ and $\lambda > 0$, minimize $\frac12 (x - a)^2 + \lambda \abs{z}$ subject to $x - z = 0$.
Clause 1 gives $x^{k+1} = (a - y^k + \rho z^k) / (1 + \rho)$, by setting the derivative in $x$ to zero.
Clause 2 gives $z^{k+1} = S_{\lambda/\rho}(x^{k+1} + y^k / \rho)$, where $S_t(v) = \sgn(v) \max(\abs{v} - t, 0)$ is soft thresholding.

Non-example: minimizing $L_\rho$ jointly over $(x, z)$ before the update of $y$ is not ADMM.
It replaces clauses 1 and 2 by one joint step, and it is the plain [[augmented Lagrangian method|AX0NJ6NK81]].
