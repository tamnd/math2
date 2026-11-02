---
tag: 53K0FDVSHE
kind: definition
name: Inertial manifold
msc: [37L25, 35B42]
defines: W1F5C7RZ0M
uses: [HM2HHE3J51, 0XMEM406JM, 0AW1E6YTJY, 4SH2ZB984E]
sources:
  - url: https://en.wikipedia.org/wiki/Inertial_manifold
---

## Definition

Let $H$ be a real [[Hilbert space|HM2HHE3J51]] and let $(S(t))_{t \ge 0}$ be a [[semigroup|0XMEM406JM]] of continuous maps $S(t) \colon H \to H$ with $S(0) = \id$ and $S(t + s) = S(t) S(s)$.
An *inertial manifold* for $S$ is a subset $\mathcal{M} \subseteq H$ such that:

1. $\mathcal{M}$ is a finite-dimensional Lipschitz manifold: there are an orthogonal projection $P$ of finite rank and a [[Lipschitz|0AW1E6YTJY]] map $\Phi \colon PH \to (I - P)H$ with $\mathcal{M} = \set{p + \Phi(p) : p \in PH}$;
2. $\mathcal{M}$ is positively invariant: $S(t) \mathcal{M} \subseteq \mathcal{M}$ for all $t \ge 0$;
3. $\mathcal{M}$ attracts exponentially: there is $\gamma > 0$ and, for each $u_0 \in H$, a constant $C(u_0)$ with $\operatorname{dist}(S(t) u_0, \mathcal{M}) \le C(u_0) e^{-\gamma t}$ for all $t \ge 0$.

## Remarks

If the semigroup has a [[global attractor|4SH2ZB984E]] $\mathcal{A}$, then $\mathcal{A} \subseteq \mathcal{M}$.
The dynamics on $\mathcal{M}$ are given by an ordinary differential equation for $p = P u$ in the finite-dimensional space $PH$, the inertial form.
Some authors ask in clause 3 for exponential tracking: each solution approaches some solution that lies on $\mathcal{M}$.

Example: let $H = \R^2$ and $S(t)(x, y) = (e^{-t} x, e^{-10 t} y)$.
Take $P(x, y) = (x, 0)$ and $\Phi = 0$, so $\mathcal{M}$ is the $x$-axis.
It is invariant, and $\operatorname{dist}(S(t)(x, y), \mathcal{M}) = e^{-10 t} \abs{y}$, so all clauses hold with $\gamma = 10$.

Non-example: for the same semigroup, the parabola $\set{(x, x^2)}$ is the graph of a function, but it is not invariant.
The point $(1, 1)$ goes to $(e^{-t}, e^{-10 t})$, which is not on the parabola for $t > 0$, so clause 2 fails.

Consider a dissipative equation $u' + A u = F(u)$ with $A$ self-adjoint with compact inverse and $F$ globally Lipschitz.
An inertial manifold exists when the eigenvalues of $A$ have large enough gaps compared with the Lipschitz constant of $F$.
