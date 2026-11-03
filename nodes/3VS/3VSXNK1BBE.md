---
tag: 3VSXNK1BBE
kind: definition
name: Compact real form
msc: ["17B20", "22E60", "22E46"]
defines: 6QQF55DQ6K
uses: [59DHW3BZTW, EY9DN7QAX1, TWVQT18JXE]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_Lie_algebra
---

## Definition

Let $\mathfrak{g}$ be a finite-dimensional [[semisimple Lie algebra|EY9DN7QAX1]] over $\C$.
A *compact real form* of $\mathfrak{g}$ is a [[real form|59DHW3BZTW]] $\mathfrak{u}$ of $\mathfrak{g}$ whose [[Killing form|TWVQT18JXE]] $B_\mathfrak{u}$ is negative definite: $B_\mathfrak{u}(X, X) < 0$ for all nonzero $X \in \mathfrak{u}$.

## Remarks

Example: $\mathfrak{su}(n)$, the skew-Hermitian $n \times n$ matrices of trace $0$, is a compact real form of $\mathfrak{sl}_n(\C)$.
Its Killing form is $B(X, Y) = 2n \tr(XY)$, and for $X$ skew-Hermitian and nonzero, $\tr(X^2) = -\tr(X X^*) < 0$.
Non-example: $\mathfrak{sl}_2(\R)$ is a real form of $\mathfrak{sl}_2(\C)$ but not a compact one, since $h = \operatorname{diag}(1, -1)$ has $B(h, h) = 8 > 0$.
A real semisimple Lie algebra has negative definite Killing form if and only if it is the Lie algebra of a [[compact Lie group|9TFC6ADC1C]].
Every complex semisimple Lie algebra has a compact real form, and any two are conjugate under an automorphism of $\mathfrak{g}$.

## Explanations

### L1 human

A compact real form is a real form in which the Killing form has a fixed negative sign.
It is the real form that comes from a compact Lie group, such as $\mathfrak{su}(n)$ inside $\mathfrak{sl}_n(\C)$.
