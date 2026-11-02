---
tag: 793SSEV9ED
kind: definition
name: Riemann curvature tensor
msc: [53B20, 53B05]
defines: JA29ETCM02
uses: [JX65KSVHSJ, 68FGQEBD6J, WX302T93TW, CAZYGE1T4E, 7CBT4SM83Y]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_curvature_tensor
---

## Definition

Let $M$ be a smooth manifold with an [[affine connection|JX65KSVHSJ]] $\nabla$, and let $\mathfrak{X}(M)$ be the space of smooth vector fields on $M$.
The *curvature tensor* of $\nabla$ is the map $R : \mathfrak{X}(M)^3 \to \mathfrak{X}(M)$ given by
$$R(X, Y) Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z,$$
where $[X, Y]$ is the [[Lie bracket|68FGQEBD6J]].
When $(M, g)$ is a [[Riemannian manifold|7CBT4SM83Y]] and $\nabla$ is its [[Levi-Civita connection|CAZYGE1T4E]], $R$ is the *Riemann curvature tensor* of $(M, g)$.

## Remarks

$R$ is $C^\infty(M)$-linear in $X$, $Y$ and $Z$, so it is a [[tensor field|WX302T93TW]] of type $(1, 3)$, and $R(Y, X) = -R(X, Y)$.
Some books use the opposite sign; the convention here gives positive sectional curvature $g(R(X, Y) Y, X) > 0$ on the sphere.
Example: for the flat connection of $\R^n$, $\nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z = \nabla_{[X, Y]} Z$ by symmetry of second derivatives, so $R = 0$.
For the round sphere of radius $r$, $R(X, Y) Z = r^{-2} \big( g(Y, Z) X - g(X, Z) Y \big)$.
Non-example of a tensor: the expression $\nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z$ alone is not $C^\infty(M)$-linear in $X$, as replacing $X$ by $fX$ adds $-(Yf) \nabla_X Z$; the term $\nabla_{[X, Y]} Z$ removes this.
In a chart, $R(\partial_i, \partial_j) \partial_k = \sum_l R^l{}_{kij} \partial_l$ with $R^l{}_{kij} = \partial_i \Gamma^l_{jk} - \partial_j \Gamma^l_{ik} + \sum_m (\Gamma^l_{im} \Gamma^m_{jk} - \Gamma^l_{jm} \Gamma^m_{ik})$.
For the Levi-Civita connection, $R_{abcd} = g(R(X_c, X_d) X_b, X_a)$ is antisymmetric in $(a, b)$ and in $(c, d)$ and symmetric under $(a, b) \leftrightarrow (c, d)$.
