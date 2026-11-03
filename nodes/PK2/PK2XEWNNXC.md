---
tag: PK2XEWNNXC
kind: definition
name: Riemann invariants
msc: [35L65, 76N15, 35L60]
defines: GB7R2ERCTA
uses: [92C3S03AQZ, P3VXR8FW17]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_invariant
---

## Definition

Let $U \subseteq \R^m$ be open and let $A \colon U \to \R^{m \times m}$ be a smooth matrix function.
Assume that the system $u_t + A(u) u_x = 0$ is [[strictly hyperbolic|P3VXR8FW17]] on $U$.
So $A(u)$ has real eigenvalues $\lambda_1(u) < \cdots < \lambda_m(u)$, with smooth right eigenvectors $r_1(u), \ldots, r_m(u)$.
Let $k \in \set{1, \ldots, m}$.
A *$k$-Riemann invariant* is a $C^1$ function $w \colon U \to \R$ such that
$$\nabla w(u) \cdot r_k(u) = 0 \qquad \text{for all } u \in U.$$

## Remarks

Near each point of $U$ there are $m - 1$ functionally independent $k$-Riemann invariants, since they are the first integrals of the vector field $r_k$.
For $m = 2$, a $1$-Riemann invariant $w$ satisfies $w_t + \lambda_2(u) w_x = 0$ along every $C^1$ solution, so it is constant along the curves $dx/dt = \lambda_2$.
Indeed, write $u_x = a r_1 + b r_2$; then $w_t + \lambda_2 w_x = \nabla w \cdot (\lambda_2 I - A) u_x = a (\lambda_2 - \lambda_1) \nabla w \cdot r_1 = 0$.
Some authors label the invariants by the family of curves along which they are constant, which swaps the indices when $m = 2$.

Example: isentropic gas dynamics in the variables $(\rho, u)$ has $A = \begin{pmatrix} u & \rho \\ c^2/\rho & u \end{pmatrix}$, with $c = c(\rho) > 0$ the sound speed.
The eigenvalues are $u - c$ and $u + c$, with eigenvectors $r_1 = (\rho, -c)$ and $r_2 = (\rho, c)$.
Let $h$ be a function with $h'(\rho) = c(\rho)/\rho$, and let $w = u + h(\rho)$.
Then $\nabla w = (c/\rho, 1)$ and $\nabla w \cdot r_1 = c - c = 0$, so $w$ is a $1$-Riemann invariant.
For a polytropic gas, $p = K\rho^\gamma$ with $\gamma > 1$, one may take $h = 2c/(\gamma - 1)$.

Non-example: the density $w(\rho, u) = \rho$ is not a Riemann invariant of this system, because $\nabla w = (1, 0)$ gives $\nabla w \cdot r_1 = \nabla w \cdot r_2 = \rho \ne 0$.
