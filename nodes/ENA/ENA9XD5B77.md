---
tag: ENA9XD5B77
kind: definition
name: Hamiltonian of an optimal control problem
msc: [49K15, 93C15]
defines: RACVWG5QTK
uses: [T3V6ZNAMDN, ZPDTVZQN5K]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_(control_theory)
---

## Definition

Let $U \subseteq \R^m$ be a nonempty set and $I \subseteq \R$ an interval.
Consider an [[optimal control|T3V6ZNAMDN]] problem with [[control system|ZPDTVZQN5K]] $x' = f(t, x, u)$ and running cost $\int L(t, x, u) \, dt$, where $f \colon I \times \R^n \times U \to \R^n$ and $L \colon I \times \R^n \times U \to \R$.
The *Hamiltonian* of the problem is the function $H \colon I \times \R^n \times U \times \R^n \times \R \to \R$ given by
$$H(t, x, u, p, \lambda_0) = p \cdot f(t, x, u) - \lambda_0 L(t, x, u).$$
The vector $p \in \R^n$ is the costate, and the number $\lambda_0 \ge 0$ is the cost multiplier.
In the normal case $\lambda_0 = 1$ one writes $H(t, x, u, p) = p \cdot f(t, x, u) - L(t, x, u)$.

## Remarks

Example: for $x' = u$ in $\R$ with running cost $\int \frac12 (x^2 + u^2) \, dt$, the normal Hamiltonian is $H = p u - \frac12 (x^2 + u^2)$.
For fixed $(x, p)$ it is a concave function of $u$ with maximum at $u = p$.
The state equation is recovered as $x' = \partial H / \partial p$.
Many texts use the opposite sign convention $H = L + p \cdot f$, under which optimal controls minimize $H$; this gives the minimum principle.
The two conventions differ by the change $p \mapsto -p$ and an overall sign.
A non-example is the Lagrangian $L(t, x, u)$ alone: it does not involve the costate, so it does not carry the dynamics.
