---
tag: TW35GWE1XF
kind: definition
name: Torsion tensor
msc: [53B05]
defines: JZNQAN00ZJ
uses: [JX65KSVHSJ, 68FGQEBD6J, WX302T93TW]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_tensor
---

## Definition

Let $M$ be a smooth manifold with an [[affine connection|JX65KSVHSJ]] $\nabla$, and let $\mathfrak{X}(M)$ be the space of smooth vector fields on $M$.
The *torsion* of $\nabla$ is the map $T : \mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$ given by
$$T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y],$$
where $[X, Y]$ is the [[Lie bracket|68FGQEBD6J]].
The connection $\nabla$ is *torsion-free* if $T = 0$.

## Remarks

$T$ is $C^\infty(M)$-linear in each argument: for a smooth function $f$, $T(fX, Y) = f \nabla_X Y - (Yf) X - f \nabla_Y X - f [X, Y] + (Yf) X = f \, T(X, Y)$.
So $T$ is a [[tensor field|WX302T93TW]] of type $(1, 2)$, and $T(Y, X) = -T(X, Y)$.
In a chart, $T(\partial_i, \partial_j) = \sum_k (\Gamma^k_{ij} - \Gamma^k_{ji}) \partial_k$, since coordinate vector fields commute.
Example: the flat connection of $\R^n$ has $\Gamma^k_{ij} = 0$, so it is torsion-free.
Non-example: on $\R^3$ the connection $\nabla_X Y = D_X Y + X \times Y$, with $D$ the flat connection and $\times$ the cross product, is a connection but not torsion-free, since $T(X, Y) = 2 \, X \times Y \ne 0$ for independent $X, Y$.
