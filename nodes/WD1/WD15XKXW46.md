---
tag: WD15XKXW46
kind: definition
name: Weyl tensor
msc: [53B20, 53C18]
defines: SBHY31HESP
uses: [GH6CXWFNDJ, JA29ETCM02, 4GTNM0WHDH, ZHX2VYQDZ3]
sources:
  - url: https://en.wikipedia.org/wiki/Weyl_tensor
---

## Definition

Let $(M, g)$ be a [[pseudo-Riemannian manifold|GH6CXWFNDJ]] of dimension $n \ge 3$.
Let $\operatorname{Rm}(X, Y, Z, V) = g(R(X, Y)Z, V)$ be its [[Riemann curvature tensor|JA29ETCM02]], with $R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$.
Let $\operatorname{Ric}$ be its [[Ricci curvature|4GTNM0WHDH]] and $S$ its [[scalar curvature|ZHX2VYQDZ3]].
The *Schouten tensor* is
$$P = \frac{1}{n - 2} \left( \operatorname{Ric} - \frac{S}{2(n - 1)} \, g \right).$$
For symmetric $(0,2)$-tensors $h, k$, their Kulkarni–Nomizu product, written here $h \odot k$, is the $(0,4)$-tensor
$$(h \odot k)(X, Y, Z, V) = h(X, V) k(Y, Z) + h(Y, Z) k(X, V) - h(X, Z) k(Y, V) - h(Y, V) k(X, Z).$$
The *Weyl tensor* of $(M, g)$ is the $(0,4)$-tensor
$$W = \operatorname{Rm} - P \odot g.$$

## Remarks

Example: the unit sphere $S^n$, $n \ge 3$, has $R(X, Y)Z = g(Y, Z)X - g(X, Z)Y$, so $\operatorname{Rm} = \tfrac{1}{2} \, g \odot g$, $\operatorname{Ric} = (n - 1)g$ and $S = n(n - 1)$.
Then $P = \tfrac{1}{2} g$ and $P \odot g = \tfrac{1}{2} \, g \odot g = \operatorname{Rm}$, so $W = 0$.

Non-example: for $n = 2$ the Schouten tensor has the factor $1/(n - 2)$ and is not defined, so surfaces have no Weyl tensor in this sense.

The Weyl tensor has the symmetries of the curvature tensor and all its traces vanish.
For $n = 3$ it is always zero.
For $n \ge 4$, $W = 0$ if and only if each point has a neighbourhood on which $g$ is a positive function times a flat metric.
Under a change $\tilde g = e^{2f} g$, the Weyl tensor changes by $\tilde W = e^{2f} W$.
Sign and index conventions for $\operatorname{Rm}$ differ between texts, and the formula for $W$ changes accordingly.
