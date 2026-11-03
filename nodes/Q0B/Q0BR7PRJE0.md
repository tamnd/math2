---
tag: Q0BR7PRJE0
kind: definition
name: Angular momentum operator
msc: [81R05, 81Q10, "22E70"]
defines: VKWHPCHH6K
uses: [7XAKGQQWTP, 5WG6YTAA6J, 0NEGN5CRSC, 7147M98XNR, 3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Angular_momentum_operator
---

## Definition

Let $\hbar > 0$, and on $L^2(\R^3)$ let $x = (x_1, x_2, x_3)$ be the [[position operator|7XAKGQQWTP]] and $p = -i\hbar\nabla$ the [[momentum operator|5WG6YTAA6J]].
The *orbital angular momentum operator* is $L = x \times p$, that is,
$$L_1 = -i\hbar \left( x_2 \partial_3 - x_3 \partial_2 \right), \quad L_2 = -i\hbar \left( x_3 \partial_1 - x_1 \partial_3 \right), \quad L_3 = -i\hbar \left( x_1 \partial_2 - x_2 \partial_1 \right).$$
Each $L_k$ is the closure of its action on smooth compactly supported functions, and it is [[self-adjoint|0NEGN5CRSC]].
More generally, an *angular momentum operator* on a Hilbert space is a triple $J = (J_1, J_2, J_3)$ of self-adjoint operators satisfying, on a common invariant dense domain,
$$[J_1, J_2] = i\hbar J_3, \qquad [J_2, J_3] = i\hbar J_1, \qquad [J_3, J_1] = i\hbar J_2.$$
Its square is $J^2 = J_1^2 + J_2^2 + J_3^2$.

## Remarks

$J^2$ commutes with each $J_k$.
On an irreducible finite-dimensional invariant subspace, $J^2 = \hbar^2 j(j+1)$ for some $j \in \set{0, \frac12, 1, \frac32, \ldots}$, and $J_3$ has the eigenvalues $\hbar m$, $m = -j, -j+1, \ldots, j$, each once.
For orbital angular momentum only integer $j = \ell$ occur, with the [[spherical harmonics|3F32Y21HP4]] $Y_\ell^m$ as eigenfunctions.

Example: in spherical coordinates $L_3 = -i\hbar \frac{\partial}{\partial \varphi}$, so $\psi = f(r, \theta) e^{im\varphi}$ with $m \in \Z$ satisfies $L_3\psi = \hbar m\psi$.

Non-example: the Pauli matrices satisfy $[\sigma_1, \sigma_2] = 2i\sigma_3$, not $i\hbar\sigma_3$, so $(\sigma_1, \sigma_2, \sigma_3)$ is not an angular momentum operator; the rescaled triple $S = \frac{\hbar}{2}\sigma$ is one, the [[spin|YBS1CHXFTW]] one-half operator, with $j = \frac12$.
