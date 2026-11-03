---
tag: 6GP3GW2RHR
kind: definition
name: Akivis algebra
msc: [17D99, 17A40]
defines: T0RB145TH2
uses: [60W3THKGA7, RT4YV20367, T2HH02QC2M, 5JJYBJ6A8K]
sources:
  - url: https://en.wikipedia.org/wiki/Akivis_algebra
---

## Definition

Let $k$ be a field.
An *Akivis algebra* over $k$ is a vector space $A$ over $k$ with a bilinear map $[\cdot, \cdot] \colon A \times A \to A$ and a trilinear map $\langle \cdot, \cdot, \cdot \rangle \colon A \times A \times A \to A$ such that:

1. $[x, y] = -[y, x]$ for all $x, y \in A$;
2. for all $x, y, z \in A$ (Akivis identity),
$$[[x, y], z] + [[y, z], x] + [[z, x], y] = \sum_{\sigma} \sgn(\sigma)\, \langle \sigma(x, y, z) \rangle,$$
where $\sigma$ runs over the six permutations of the three arguments $(x, y, z)$ and $\sgn(\sigma)$ is the sign of $\sigma$.

## Remarks

Written out, the right side of the Akivis identity is $\langle x, y, z \rangle + \langle y, z, x \rangle + \langle z, x, y \rangle - \langle x, z, y \rangle - \langle y, x, z \rangle - \langle z, y, x \rangle$.

Example: let $B$ be a [[nonassociative algebra|60W3THKGA7]].
With the [[commutator|T2HH02QC2M]] $[x, y] = xy - yx$ and the [[associator|RT4YV20367]] $\langle x, y, z \rangle = (xy)z - x(yz)$, the space $B$ is an Akivis algebra.
Check: both sides of the identity expand into the twelve products $(uv)w$ and $u(vw)$ with $u, v, w$ a permutation of $x, y, z$, and they carry the same signs.
Every [[Lie algebra|5JJYBJ6A8K]] is an Akivis algebra with $\langle x, y, z \rangle = 0$.

Non-example: let $A = k^3$ with $\operatorname{char} k \notin \set{2, 3}$, the zero bracket, and $\langle u, v, w \rangle = \det(u, v, w)\, e_1$, where $e_1$ is the first standard basis vector.
The determinant is alternating, so the right side equals $6 \det(x, y, z)\, e_1$, which is nonzero for $x, y, z$ the standard basis.
The left side is $0$, so the Akivis identity fails.
