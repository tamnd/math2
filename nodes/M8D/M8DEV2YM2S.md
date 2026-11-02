---
tag: M8DEV2YM2S
kind: definition
name: Energy drift
msc: [65P10, 65L20]
defines: BDVF3BPJEB
uses: [0EDKGA2FAK, B4C25SXFRE]
sources:
  - url: https://en.wikipedia.org/wiki/Energy_drift
---

## Definition

Let $H \colon \R^{2d} \to \R$ be smooth, and consider the [[Hamiltonian system|0EDKGA2FAK]] $y' = J \nabla H(y)$, where $J = \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}$; its exact solutions satisfy $H(y(t)) = H(y(0))$.
Let a numerical method with fixed step size $h > 0$ produce the sequence $y_0, y_1, y_2, \ldots$ from $y_0$.
The energy error at step $n$ is $e_n = H(y_n) - H(y_0)$.
The method shows *energy drift* on this problem if the energy error has a systematic trend in time.
This means that $\abs{e_n}$ is not bounded uniformly in $n$ but grows with the time $t_n = n h$.

## Remarks

Example: for $H(q, p) = \frac12 (q^2 + p^2)$, the explicit Euler method $q_{n+1} = q_n + h p_n$, $p_{n+1} = p_n - h q_n$ gives $q_{n+1}^2 + p_{n+1}^2 = (1 + h^2)(q_n^2 + p_n^2)$.
So $H(y_n) = (1 + h^2)^n H(y_0)$, and the energy error grows exponentially in $n$: the method has energy drift.
Non-example: the symplectic Euler method $p_{n+1} = p_n - h q_n$, $q_{n+1} = q_n + h p_{n+1}$ is a linear map of determinant $1$ and trace $2 - h^2$.
For $0 < h < 2$ its eigenvalues are distinct and of modulus $1$, so the sequence $y_n$ is bounded and so is $e_n$.
There is no drift, only a bounded oscillation of size $O(h)$.
More generally, let $H$ be analytic and use a [[symplectic integrator|B4C25SXFRE]] of order $p$.
If the numerical solution stays in a compact set, backward error analysis gives $e_n = O(h^p)$ over times exponentially long in $1/h$.
In floating-point arithmetic, round-off adds a slow random-walk drift even to such methods.

## Explanations

### L1 human

Energy drift means that the computed energy wanders away from its true constant value with a trend over time, not just with small bounded wiggles.
It is the usual way to judge whether an integrator is fit for long simulations of conservative systems.
