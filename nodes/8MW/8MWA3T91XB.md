---
tag: 8MWA3T91XB
kind: definition
name: Sum-of-squares optimization
msc: [90C23, 90C22]
defines: AM0BYNK5YJ
uses: [01MMVW8CKC, 2RTN2X4R2N]
sources:
  - url: https://en.wikipedia.org/wiki/Sum-of-squares_optimization
---

## Definition

Let $\R[x] = \R[x_1, \dots, x_n]$ be the ring of real polynomials in $n$ variables.
A polynomial $p \in \R[x]$ is a *sum of squares* (SOS) if $p = \sum_{i=1}^k q_i^2$ for some $k \ge 1$ and $q_1, \dots, q_k \in \R[x]$.
Let $c \in \R^m$ and let $p_{j,0}, p_{j,1}, \dots, p_{j,m} \in \R[x]$ for $j = 1, \dots, N$.
The *sum-of-squares program* with these data is: minimise $c^T u$ over $u \in \R^m$ subject to
$$p_{j,0} + \sum_{l=1}^m u_l \, p_{j,l} \ \text{ is SOS} \quad (j = 1, \dots, N).$$
*Sum-of-squares optimization* is the study and solution of such programs.

## Remarks

Let $z(x)$ be the vector of all monomials of degree at most $d$.
A polynomial $p$ of degree at most $2d$ is SOS if and only if $p(x) = z(x)^T Q z(x)$ for some [[positive semidefinite|01MMVW8CKC]] matrix $Q$.
Matching coefficients turns each SOS constraint into linear equations on $Q$ and $u$ together with $Q \succeq 0$, so the program is a [[semidefinite program|2RTN2X4R2N]].

Example: maximise $\gamma$ subject to $p - \gamma$ SOS (take $m = 1$, $u = \gamma$, $c = -1$, $p_{1,0} = p$, $p_{1,1} = -1$).
For $p(x) = x^2 - 2x + 3$ one has $p - 2 = (x - 1)^2$, which is SOS, while $p - \gamma$ is negative at $x = 1$ for $\gamma > 2$; so the optimum is $\gamma = 2$, the minimum of $p$.

Non-example: the Motzkin polynomial $x^4 y^2 + x^2 y^4 - 3 x^2 y^2 + 1$ is nonnegative on $\R^2$ by the inequality of arithmetic and geometric means, but it is not a sum of squares of polynomials.
So the constraint "$p - \gamma$ is SOS" fails for $\gamma = 0$, and the SOS program does not certify its minimum $0$.
