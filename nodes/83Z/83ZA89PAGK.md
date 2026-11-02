---
tag: 83ZA89PAGK
kind: definition
name: Cotton tensor
msc: [53C18, 53B20]
defines: 10CQ5007PH
uses: [GH6CXWFNDJ, CAZYGE1T4E, 4GTNM0WHDH, ZHX2VYQDZ3]
sources:
  - url: https://en.wikipedia.org/wiki/Cotton_tensor
---

## Definition

Let $(M, g)$ be a [[pseudo-Riemannian manifold|GH6CXWFNDJ]] of dimension $n \ge 3$, with [[Levi-Civita connection|CAZYGE1T4E]] $\nabla$, [[Ricci curvature|4GTNM0WHDH]] $\operatorname{Ric}$ and [[scalar curvature|ZHX2VYQDZ3]] $S$.
Let $P = \frac{1}{n - 2} \left( \operatorname{Ric} - \frac{S}{2(n - 1)} g \right)$ be the Schouten tensor.
The *Cotton tensor* of $(M, g)$ is the $(0,3)$-tensor
$$C(X, Y, Z) = (\nabla_Z P)(X, Y) - (\nabla_Y P)(X, Z),$$
for vector fields $X, Y, Z$; in index notation $C_{ijk} = \nabla_k P_{ij} - \nabla_j P_{ik}$.

## Remarks

Example: if $(M, g)$ is Einstein with $\operatorname{Ric} = \lambda g$ for a constant $\lambda$ and $n \ge 3$, then $S = n\lambda$ is constant and $P$ is a constant multiple of $g$.
Since $\nabla g = 0$, also $\nabla P = 0$, so $C = 0$.

Non-example: for $n = 2$ the factor $1/(n - 2)$ is not defined, so there is no Cotton tensor of a surface in this sense.

$C$ is antisymmetric in its last two arguments, and its trace over the first two arguments vanishes by the contracted Bianchi identity.
For $n = 3$, $C = 0$ if and only if $g$ is locally conformally flat.
For $n \ge 4$, the divergence of the [[Weyl tensor|SBHY31HESP]] is $(n - 3)$ times $C$, up to a sign fixed by the conventions.
Some texts use the opposite sign or a different order of indices.
