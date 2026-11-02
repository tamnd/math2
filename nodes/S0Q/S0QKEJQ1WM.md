---
tag: S0QKEJQ1WM
kind: definition
name: Mean-field game
msc: [91A16, 35Q89, 49N80]
defines: WS9A6N2Y0F
uses: [SJP9HW82VX, FVQWR7NS00, 0E0B6RA8K0, 0ABK9V9Y64, 0MWV6ZTK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Mean-field_game_theory
---

## Definition

Let $\mathbb{T}^d = \R^d / \Z^d$ be the torus, let $T > 0$, and let $\nu > 0$ be a constant.
Let $\mathcal{P}$ be the set of probability densities on $\mathbb{T}^d$.
Let $H \colon \mathbb{T}^d \times \R^d \to \R$ be a smooth function, convex in its second variable, the Hamiltonian.
Let $F, G \colon \mathbb{T}^d \times \mathcal{P} \to \R$ be given coupling functions, and let $m_0 \in \mathcal{P}$ be the initial distribution.
The *mean-field game system* is the system
$$\begin{aligned} -\partial_t u - \nu \Delta u + H(x, \nabla u) &= F(x, m(t)), \\ \partial_t m - \nu \Delta m - \nabla \cdot \big( m \, \partial_p H(x, \nabla u) \big) &= 0, \\ m(0, x) = m_0(x), \qquad u(T, x) &= G(x, m(T)), \end{aligned}$$
for unknown functions $u, m \colon [0, T] \times \mathbb{T}^d \to \R$.
Here $\Delta$ is the [[Laplacian|0E0B6RA8K0]], $\nabla$ the [[gradient|0ABK9V9Y64]] and $\nabla \cdot$ the [[divergence|0MWV6ZTK6S]] in $x$, and $\partial_p H$ is the gradient of $H$ in its second variable.
A solution $(u, m)$ is a *mean-field game equilibrium*.
In it, $u$ is the value function of a typical player and $m(t)$ is the distribution of the players at time $t$.

## Remarks

The first equation is a [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]] solved backward from time $T$.
The second is a [[Fokker–Planck equation|FVQWR7NS00]] solved forward from time $0$, for players who use the optimal feedback $-\partial_p H(x, \nabla u)$ with noise of intensity $\nu$.

Example: let $H(x, p) = \tfrac{1}{2} \abs{p}^2$ and $F = G = 0$.
Then $u = 0$ and $m$ equal to the solution of the heat equation $\partial_t m = \nu \Delta m$ with $m(0) = m_0$ form a solution.
The first equation and the terminal condition hold since $u = 0$.
The second equation reduces to the heat equation because $\partial_p H(x, 0) = 0$.

Non-example: in the same setting, if $m_0$ is not constant, then $u = 0$ and $m(t, x) = m_0(x)$ for all $t$ is not a solution, because $\partial_t m - \nu \Delta m = -\nu \Delta m_0 \ne 0$.

Lasry and Lions proved existence of solutions under regularity assumptions, and uniqueness when $F$ and $G$ are monotone.
