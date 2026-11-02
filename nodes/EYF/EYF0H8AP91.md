---
tag: EYF0H8AP91
kind: statement
role: theorem
name: Comparison principle
msc: [35B51, 35B50, 35J15]
uses: [B4TTNHSTRX, D2JF19HF91]
about: [B4TTNHSTRX]
sources:
  - url: https://en.wikipedia.org/wiki/Comparison_theorem
---

## Statement

Let $\Omega \subseteq \R^n$ be a bounded domain, that is, a bounded connected open set.
Let
$$L u = \sum_{i,j=1}^n a^{ij}(x) \, \partial_i \partial_j u + \sum_{i=1}^n b^i(x) \, \partial_i u + c(x) \, u$$
be a uniformly [[elliptic|B4TTNHSTRX]] operator in $\Omega$ with bounded coefficients, $a^{ij} = a^{ji}$, and $c \le 0$ in $\Omega$.
Let $u, v \in C^2(\Omega) \cap C^0(\overline{\Omega})$ satisfy $L u \ge L v$ in $\Omega$ and $u \le v$ on $\partial\Omega$.
Then $u \le v$ in $\Omega$.

## Remarks

Proof idea: the function $w = u - v$ satisfies $L w \ge 0$ in $\Omega$ and $w \le 0$ on $\partial\Omega$.
The weak [[maximum principle|D2JF19HF91]] for operators with $c \le 0$ gives $\sup_\Omega w \le \sup_{\partial\Omega} w^+ = 0$.

Example: if $\Delta u \ge 0$ in the unit ball $B$ and $u \le 1$ on $\partial B$, comparing with $v = 1$ gives $u \le 1$ in $B$.
If $-\Delta u = 1$ in $B \subseteq \R^n$ with $u = 0$ on $\partial B$, comparison with $0$ and with $(1 - \abs{x}^2)/(2n)$ shows $0 \le u \le (1 - \abs{x}^2)/(2n)$; in fact $u$ equals this function.

The sign condition on $c$ is needed: for $L u = u'' + u$ on $(0, \pi)$, the functions $u = \sin x$ and $v = 0$ satisfy $L u = L v = 0$ and $u = v$ at the endpoints, but $u > v$ inside.

Uniqueness for the Dirichlet problem $L u = f$ in $\Omega$, $u = g$ on $\partial\Omega$, follows by applying the theorem twice.

## Explanations

### L1 human

If two solutions of the same kind of equation are ordered on the boundary, they stay ordered inside.
So to bound an unknown solution, it is enough to find an explicit function that dominates it on the boundary and satisfies the right inequality inside.
Such functions are called barriers, or super- and subsolutions.

### L2 human

The comparison principle is the main use of the maximum principle.
It gives uniqueness for boundary value problems, a priori bounds by explicit barriers, and monotone iteration schemes between a subsolution and a supersolution.
Versions exist for parabolic equations, through the [[parabolic maximum principle|EMDVD4E83K]], and for fully nonlinear equations, where comparison for [[viscosity solutions|H1ERJ3T75T]] is the key uniqueness tool.
It is the PDE analogue of the [[comparison theorem|7XTBR347P5]] for ordinary differential equations.
