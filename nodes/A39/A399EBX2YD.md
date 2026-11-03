---
tag: A399EBX2YD
kind: definition
name: Real form of a Lie group
msc: ["22E15", "22E10"]
defines: SADNTQAY3G
uses: [7JBRGCVJRB, NM8XCPS1Q3]
sources:
  - url: https://en.wikipedia.org/wiki/Real_form_(Lie_theory)
---

## Definition

Let $G_\C$ be a complex [[Lie group|7JBRGCVJRB]] with complex [[Lie algebra|WKVBS76432]] $\mathfrak{g}_\C$.
A *[[real form|59DHW3BZTW]]* of $G_\C$ is a closed real [[Lie subgroup|NM8XCPS1Q3]] $G$ of $G_\C$ whose Lie algebra $\mathfrak{g} \subseteq \mathfrak{g}_\C$ is a real form of $\mathfrak{g}_\C$.
That is, $\mathfrak{g}_\C = \mathfrak{g} \oplus i \mathfrak{g}$ as real vector spaces.

## Remarks

Example: $G = \mathrm{SU}(n)$ in $G_\C = \mathrm{SL}_n(\C)$.
Here $\mathfrak{g} = \mathfrak{su}(n)$ is the space of skew-Hermitian matrices of trace $0$, and $i \mathfrak{g}$ is the space of Hermitian matrices of trace $0$.
Each traceless complex matrix $Z$ is uniquely $\frac{1}{2}(Z - Z^*) + \frac{1}{2}(Z + Z^*)$, a skew-Hermitian plus a Hermitian traceless matrix, so $\mathfrak{sl}_n(\C) = \mathfrak{g} \oplus i\mathfrak{g}$.

Non-example: $G = \mathrm{SO}(n)$ in $\mathrm{SL}_n(\C)$ for $n \ge 2$.
Its Lie algebra $\mathfrak{so}(n)$ of real antisymmetric matrices satisfies $\mathfrak{so}(n) \cap i\,\mathfrak{so}(n) = 0$, but $\mathfrak{so}(n) \oplus i\,\mathfrak{so}(n)$ is the space of complex antisymmetric matrices, which misses the diagonal matrices of trace $0$.

Often a real form is given as the fixed point group of an antiholomorphic involution $\sigma$ of $G_\C$, or as an open subgroup of it.
For $\sigma(g) = \bar g$ on $\mathrm{SL}_n(\C)$, the fixed points form $\mathrm{SL}_n(\R)$; for $\sigma(g) = (g^*)^{-1}$, they form $\mathrm{SU}(n)$.
A real form that is compact is a compact real form; for a connected complex semisimple group it exists and is unique up to conjugation.
