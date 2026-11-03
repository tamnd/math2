---
tag: VDM6VE9X1Q
kind: definition
name: Separation of variables in the Hamilton–Jacobi equation
msc: [70H20, 70H06]
defines: ST45QMRDZ6
uses: [5TRXQKP7DY, JAZWC031S4, D4TRNRC45C, 47NFRVB564]
sources:
  - url: https://en.wikipedia.org/wiki/Hamilton%E2%80%93Jacobi_equation
---

## Definition

Let $H(q, p)$ be a time-independent Hamiltonian of class $C^2$ on an open subset of $\R^{2n}$.
The stationary [[Hamilton–Jacobi equation|5TRXQKP7DY]] for $H$ is
$$H\big(q, \nabla_q W(q)\big) = E,$$
for an unknown function $W$, called Hamilton's characteristic function, and a constant $E$.
A *complete solution* is a family $W(q, \alpha)$ of solutions, $C^2$ in $(q, \alpha)$, with $n$ constants $\alpha = (\alpha_1, \ldots, \alpha_n)$ and $E = E(\alpha)$.
It must make the matrix $\big(\partial^2 W / \partial q_i \partial \alpha_j\big)$ invertible.
The equation is *separable* in $q$ when it has a complete solution
$$W(q, \alpha) = \sum_{i=1}^n W_i(q_i, \alpha),$$
where each $W_i$ depends only on $q_i$ and on $\alpha$.

## Remarks

Then $S(q, t, \alpha) = W(q, \alpha) - E(\alpha) t$ solves the time-dependent equation, and it serves as a type 2 [[generating function|D4TRNRC45C]] with new momenta $\alpha$; this links it to [[Hamilton's principal function|JAZWC031S4]].
The method is an additive analogue of [[separation of variables|47NFRVB564]] for linear partial differential equations, where one uses products instead of sums.
The motion is given by $\partial S / \partial \alpha_j = \beta_j$ with constants $\beta_j$, which can be solved for $q(t)$.

Example: $H = \sum_{i=1}^n \big(\frac{1}{2} p_i^2 + V_i(q_i)\big)$.
Take $W_i(q_i, \alpha) = \int^{q_i} \sqrt{2 (\alpha_i - V_i(x))} \, dx$ on a region where $\alpha_i > V_i$, and $E = \alpha_1 + \cdots + \alpha_n$.
Then $\frac{1}{2} (W_i')^2 + V_i(q_i) = \alpha_i$, the sum gives $E$, and $\partial^2 W / \partial q_i \partial \alpha_j = \delta_{ij} / \sqrt{2(\alpha_i - V_i(q_i))}$ is an invertible diagonal matrix.

Non-example: let $n = 2$ and $H = \frac{1}{2}(p_1^2 + p_2^2)$.
The family $W = \sqrt{\alpha_1}(q_1 + q_2)$ is a sum of one-variable terms that solves the equation with $E = \alpha_1$.
But it depends on one constant only, so $\partial^2 W / \partial q_i \partial \alpha_j$ has a zero column and the solution is not complete.
