---
tag: EPE132XYYK
kind: definition
name: Stably free module
msc: [19A13, 13C10]
defines: YMXJ4JTQPF
uses: [0B1261B5ED, 0NZ8JA25WK, 0DZ9DKAKZR]
sources:
  - url: https://en.wikipedia.org/wiki/Stably_free_module
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $P$ be a left [[$R$-module|0NZ8JA25WK]].
The module $P$ is *stably free* if there are integers $m, n \ge 0$ with $P \oplus R^m \cong R^n$.

## Remarks

A stably free module is finitely generated and projective, since it is a direct summand of $R^n$.
Every [[free module|0DZ9DKAKZR]] $R^k$ is stably free, with $m = 0$.

Example: let $A = \R[x, y, z]/(x^2 + y^2 + z^2 - 1)$ and let $P$ be the kernel of the map $A^3 \to A$, $(u, v, w) \mapsto ux + vy + wz$.
The map is onto and has the section $a \mapsto (ax, ay, az)$, because $x^2 + y^2 + z^2 = 1$ in $A$.
So $P \oplus A \cong A^3$, and $P$ is stably free.
It is not free: an isomorphism $P \cong A^2$ would give a nowhere-vanishing tangent vector field on the $2$-sphere, which the hairy ball theorem rules out.

Non-example: over $R = \Z/6\Z$, the projective module $P = \Z/2\Z$ is not stably free.
The module $P \oplus R^m$ has $2 \cdot 6^m$ elements, which is never of the form $6^n$.
