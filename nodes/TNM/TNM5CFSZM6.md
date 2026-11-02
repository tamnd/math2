---
tag: TNM5CFSZM6
kind: statement
role: proposition
name: Roe solver
msc: [65M08, 35L65]
uses: [ZY4GY93C4B, XN081NCPF5, GJWKX22VVE, 07SQCNV233, 0BQAA2BK3Q, JSDMGGTG7G]
about: [ZY4GY93C4B]
sources:
  - url: https://en.wikipedia.org/wiki/Roe_solver
---

## Statement

Let $\Omega \subseteq \R^m$ be open and let $F \colon \Omega \to \R^m$ be the $C^1$ flux of a [[hyperbolic conservation law|XN081NCPF5]] $u_t + F(u)_x = 0$.
A *Roe matrix* is a map $(u_l, u_r) \mapsto A(u_l, u_r)$ from $\Omega \times \Omega$ to the real $m \times m$ matrices with three properties:

1. $F(u_r) - F(u_l) = A(u_l, u_r)(u_r - u_l)$ for all $u_l, u_r \in \Omega$;
2. $A(u_l, u_r)$ is [[diagonalisable|07SQCNV233]] with real [[eigenvalues|0BQAA2BK3Q]];
3. $A(u, u) = F'(u)$ for all $u \in \Omega$.

Write $A = A(u_l, u_r) = R \Lambda R^{-1}$ with $\Lambda$ diagonal, and $\abs{A} = R \abs{\Lambda} R^{-1}$.
The *Roe flux* is
$$H(u_l, u_r) = \tfrac{1}{2} \big( F(u_l) + F(u_r) \big) - \tfrac{1}{2} \abs{A} (u_r - u_l).$$
Then:

1. $H(u_l, u_r) = F(u_l) + A (w_0 - u_l) = F(u_r) - A (u_r - w_0)$, and $H(u, u) = F(u)$. Here $w_0$ is the value on the line $x = 0$ of the solution of the linear [[Riemann problem|GJWKX22VVE]] $w_t + A w_x = 0$ with data $u_l, u_r$. So $H$ is a consistent [[Riemann solver|ZY4GY93C4B]].
2. Let $u_r \ne u_l$ with $F(u_r) - F(u_l) = s (u_r - u_l)$ for a number $s$. Then $u_r - u_l$ is an eigenvector of $A$ for the eigenvalue $s$. The linear Riemann problem is then solved by the single jump from $u_l$ to $u_r$ with speed $s$.

## Remarks

Write $u_r - u_l = \sum_k \alpha_k r_k$ in eigenvectors $r_k$ of $A$ with eigenvalues $\lambda_k$.
The linear Riemann problem moves each component $\alpha_k r_k$ with speed $\lambda_k$, so $w_0 = u_l + \sum_{\lambda_k < 0} \alpha_k r_k$.
Property 1 of the matrix gives $\tfrac12 (F(u_l) + F(u_r)) = F(u_l) + \tfrac12 \sum_k \lambda_k \alpha_k r_k$, and subtracting $\tfrac12 \sum_k \abs{\lambda_k} \alpha_k r_k$ leaves $F(u_l) + \sum_{\lambda_k < 0} \lambda_k \alpha_k r_k = F(u_l) + A(w_0 - u_l)$.
Claim 2 is property 1 of the matrix applied to the jump condition.

In the scalar case $m = 1$ the Roe matrix is the number $A = \dfrac{f(u_r) - f(u_l)}{u_r - u_l}$ for $u_r \ne u_l$, and $A(u, u) = f'(u)$.
For the Euler equations of gas dynamics, Roe found a Roe matrix in closed form.
It is the flux Jacobian at averages weighted by $\sqrt{\rho_l}$ and $\sqrt{\rho_r}$, such as $\tilde v = \dfrac{\sqrt{\rho_l} v_l + \sqrt{\rho_r} v_r}{\sqrt{\rho_l} + \sqrt{\rho_r}}$ for the velocity.

The Roe solver can keep entropy-violating jumps at transonic rarefactions, where an eigenvalue changes sign.
For $f(u) = u^2/2$ with $u_l = -1$ and $u_r = 1$ one gets $A = 0$ and $H = \tfrac12$, so the scheme keeps the initial jump although the entropy solution is a rarefaction fan.
An entropy fix, such as the one of Harten, changes $\abs{\lambda_k}$ near zero to remove this defect.

## Explanations

### L1 human

Solving the true Riemann problem at every cell wall is costly for systems like gas dynamics.
Roe's idea is to replace the nonlinear equation near each wall by a linear one with a well chosen constant matrix.
The linear problem is solved by splitting the jump into eigenvector components that move left or right.
The matrix is chosen so that a single [[shock|JSDMGGTG7G]] is still captured exactly.

### L2 human

The Roe flux is a building block of [[Godunov-type schemes|43HZJ7DRT0]] and of [[MUSCL schemes|W7QH1BPBS8]], where it is evaluated at the reconstructed interface states.
Its upwind part $-\tfrac12 \abs{A}(u_r - u_l)$ acts as numerical viscosity: each wave family is damped in proportion to the size of its speed.
This keeps stationary shocks and contact discontinuities sharp, but makes the fix near sonic points necessary.
Other approximate solvers, such as HLL, trade sharpness for robustness and need only estimates of the wave speeds.
