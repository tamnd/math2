---
tag: AQK50V3NGJ
kind: definition
name: Peak function
msc: ["32E35", 32T15]
defines: SKE8QTW3YM
uses: [507C34W0ZT, Z7RVXBA2KB]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
---

## Definition

Let $\Omega \subseteq \C^n$ be a bounded domain and let $p \in \partial\Omega$.
A *peak function* for $\Omega$ at $p$ is a function $f \colon \overline{\Omega} \to \C$ such that:

1. $f$ is continuous on $\overline{\Omega}$ and [[holomorphic|507C34W0ZT]] on $\Omega$.
2. $f(p) = 1$.
3. $\abs{f(z)} < 1$ for every $z \in \overline{\Omega} \setminus \set{p}$.

The point $p$ is a *peak point* of $\Omega$ if a peak function at $p$ exists.

## Remarks

Example: on the unit ball $B \subseteq \C^n$, let $e_1 = (1, 0, \dots, 0)$ and $f(z) = (1 + z_1)/2$.
Then $f(e_1) = 1$, and $\abs{f(z)} \le (1 + \abs{z_1})/2 \le 1$ on $\overline{B}$, with equality only if $z_1 = 1$, which forces $z = e_1$.
Non-example: on the bidisc $\Delta^2$, the point $p = (1, 0)$ is not a peak point.
Suppose $f$ satisfies the three clauses.
The function $w \mapsto f(1, w)$ is holomorphic on the open unit disc, as a locally uniform limit of the functions $w \mapsto f(r, w)$ for $r \to 1$.
It has modulus at most $1$ and reaches the modulus $1$ at the interior point $w = 0$, so it is the constant $1$ by the maximum modulus principle, against clause 3.
Every boundary point of a bounded [[strongly pseudoconvex domain|Z7RVXBA2KB]] with smooth boundary is a peak point.
