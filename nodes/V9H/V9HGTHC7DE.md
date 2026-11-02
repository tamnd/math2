---
tag: V9HGTHC7DE
kind: definition
name: Connection on a vector bundle
msc: [53C05]
defines: 5ZYRRVE8BW
uses: [F45VQ47GPV, WWX7H5W1RP, WY6K3P4YCG]
sources:
  - url: https://en.wikipedia.org/wiki/Connection_(vector_bundle)
---

## Definition

Let $M$ be a smooth manifold, and let $\pi : E \to M$ be a smooth real vector bundle.
Let $\Gamma(E)$ be the space of smooth [[sections|WWX7H5W1RP]] of $E$, and let $\mathfrak{X}(M)$ be the space of smooth vector fields on $M$.
A *connection* on $E$ is a map
$$\nabla : \mathfrak{X}(M) \times \Gamma(E) \to \Gamma(E), \quad (X, s) \mapsto \nabla_X s,$$
such that for all $X, Y \in \mathfrak{X}(M)$, $s, t \in \Gamma(E)$, $f, h \in C^\infty(M)$ and $a, b \in \R$:

1. $\nabla_{fX + hY} s = f \nabla_X s + h \nabla_Y s$.
2. $\nabla_X (a s + b t) = a \nabla_X s + b \nabla_X t$.
3. $\nabla_X (f s) = (X f) \, s + f \nabla_X s$.

## Remarks

Example: on the trivial bundle $E = M \times \R^r$, a section is a smooth map $s = (s^1, \dots, s^r)$, and $\nabla_X s = (X s^1, \dots, X s^r)$ is a connection; clause 3 is the product rule $X(f s^i) = (Xf) s^i + f X s^i$.
Non-example: on the [[tangent bundle|WY6K3P4YCG]], the map $(X, Y) \mapsto [X, Y]$ satisfies clause 2 but fails clause 1, since $[fX, Y] = f[X, Y] - (Yf) X$.
By clause 1, $(\nabla_X s)(p)$ depends only on $X_p$, so $\nabla$ can be seen as a map $\Gamma(E) \to \Gamma(T^*M \otimes E)$.
In a local frame $e_1, \dots, e_r$ of $E$, $\nabla e_j = \sum_i \omega^i_j \otimes e_i$ for a matrix $(\omega^i_j)$ of $1$-forms, and locally $\nabla = d + \omega$.
The difference of two connections is $C^\infty(M)$-linear in both arguments, so it is a section of $T^*M \otimes \mathrm{End}(E)$; thus connections form an affine space over this space of sections.
Complex vector bundles are treated the same way with complex scalars.
