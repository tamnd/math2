---
tag: 9XJ5FBQD7M
kind: statement
role: theorem
name: Maximum principle for subharmonic functions
msc: [31B05, 31A05]
uses: [Z1MHMGFNFW, RN4G8SGP6P, 02BH3MCBQB, 05D5EGMFYV, 0T3RZQXDYD, 8D56GQ4AG8]
about: [Z1MHMGFNFW]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
---

## Statement

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be a connected [[open set|02BH3MCBQB]], and let $u$ be [[subharmonic|Z1MHMGFNFW]] on $\Omega$.

1. If there is a point $a \in \Omega$ with $u(a) = \sup_{\Omega} u$, then $u$ is constant on $\Omega$.
2. If $\Omega$ is bounded and $\limsup_{x \to \zeta,\, x \in \Omega} u(x) \le 0$ for every $\zeta$ in the [[boundary|05D5EGMFYV]] $\partial\Omega$, then $u \le 0$ on $\Omega$.

## Remarks

Proof idea for part 1: let $M = \sup_\Omega u$ and $A = \set{x \in \Omega : u(x) = M}$.
The set $A = \set{u \ge M}$ is closed in $\Omega$ because $u$ is [[upper semicontinuous|RN4G8SGP6P]].
Let $b \in A$.
The sub-mean inequality on small spheres about $b$ and $u \le M$ force $u = M$ almost everywhere on a small ball about $b$.
Since $A$ is closed, $u = M$ on that whole ball, so $A$ is open.
Connectedness gives $A = \Omega$ when $A$ is nonempty.
For part 2, extend $u$ to $\overline{\Omega}$ by its [[limit superior|0T3RZQXDYD]] at boundary points.
The extension is upper semicontinuous on a compact set, so it attains its maximum, and part 1 rules out a positive maximum inside.

Boundedness of $\Omega$ is needed in part 2.
On the half-space $\set{x \in \R^n : x_1 > 0}$, the function $u(x) = x_1$ is harmonic, hence subharmonic, and tends to $0$ at every boundary point, but it is positive everywhere.
Connectedness is needed in part 1.
On two disjoint discs, the function equal to $0$ on one disc and $1$ on the other is subharmonic and attains its supremum, but it is not constant.
Applied to $u$ and $-u$ for a harmonic $u$, it gives the maximum and minimum principles for harmonic functions.

## Explanations

### L1 human

A subharmonic function cannot have a peak inside its domain unless it is flat.
So on a bounded region its largest values are found at the edge.
If it is at most $0$ near the edge, it is at most $0$ everywhere.

### L2 human

This is the tool behind uniqueness for the [[Dirichlet problem|8D56GQ4AG8]] and behind the Perron method, where subharmonic functions are compared with harmonic ones.
It also gives the comparison principle: if $u$ is subharmonic, $v$ is superharmonic, and $\limsup (u - v) \le 0$ at the boundary of a bounded domain, then $u \le v$ inside.
Unbounded domains need extra growth conditions, which is the subject of Phragmén–Lindelöf type results.
