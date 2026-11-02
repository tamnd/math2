---
tag: NZTCZQA8KW
kind: definition
name: Symplectic integrator
msc: [65P10, 37J11]
defines: B4C25SXFRE
uses: [0EDKGA2FAK, 0JARTXX4XP]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_integrator
---

## Definition

Let $n \ge 1$ and let $J = \begin{pmatrix} 0 & I_n \\ -I_n & 0 \end{pmatrix}$, where $I_n$ is the $n \times n$ identity matrix.
For a smooth function $H \colon \R^{2n} \to \R$, consider the [[Hamiltonian system|0EDKGA2FAK]] $y' = J \nabla H(y)$ with $y = (q, p)$, that is, $q' = \nabla_p H$ and $p' = -\nabla_q H$.
A one-step method assigns to each such $H$ and each small step size $h > 0$ a map $\Phi_h$, and computes $y_{k+1} = \Phi_h(y_k)$.
The method is a *symplectic integrator* if $\Phi_h$ is a symplectic map whenever $H$ is smooth and $\Phi_h$ is defined and smooth.
This means
$$D\Phi_h(y)^T \, J \, D\Phi_h(y) = J \quad \text{for all } y.$$

## Remarks

For $n = 1$, a map of the plane is symplectic exactly when its Jacobian determinant is $1$, that is, when it preserves area.
Example: for $H = \frac12 (p^2 + q^2)$, the symplectic Euler method $p_{k+1} = p_k - h q_k$, $q_{k+1} = q_k + h p_{k+1}$ gives $q_{k+1} = (1 - h^2) q_k + h p_k$, with Jacobian determinant $(1 - h^2) \cdot 1 - h \cdot (-h) = 1$.
In general the symplectic Euler method is $p_{k+1} = p_k - h \nabla_q H(q_k, p_{k+1})$, $q_{k+1} = q_k + h \nabla_p H(q_k, p_{k+1})$, and it is symplectic for every $H$.
Non-example: the explicit [[Euler method|0JARTXX4XP]] for the same $H$ is $q_{k+1} = q_k + h p_k$, $p_{k+1} = p_k - h q_k$, with Jacobian determinant $1 + h^2 \ne 1$, so it is not symplectic.
A Runge–Kutta method with coefficients $a_{ij}$, $b_i$ is symplectic when $b_i a_{ij} + b_j a_{ji} = b_i b_j$ for all $i, j$; the implicit midpoint rule is an example.
