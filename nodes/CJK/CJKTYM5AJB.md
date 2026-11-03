---
tag: CJKTYM5AJB
kind: definition
name: Cauchy stress tensor
msc: [74A10]
defines: KG2XWEMJ30
uses: [HXGCGHS070, 0NRYHJPQG2, 0VR671PHE5]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_stress_tensor
---

## Definition

Let $t \colon \Omega \times S^2 \to \R^3$ be the traction field of a [[stress|HXGCGHS070]] field on an open set $\Omega \subseteq \R^3$, where $S^2$ is the set of unit vectors.
A *Cauchy stress tensor* at $x \in \Omega$ is a [[linear map|0NRYHJPQG2]] $\sigma(x) \colon \R^3 \to \R^3$ such that
$$t(x, n) = \sigma(x)\, n \quad \text{for every unit vector } n.$$
In the standard basis $e_1, e_2, e_3$, its components are $\sigma_{ij}(x) = e_i \cdot t(x, e_j)$, so that $t_i(x, n) = \sum_j \sigma_{ij}(x)\, n_j$.

## Remarks

By Cauchy's stress theorem, $\sigma(x)$ exists and is unique when the traction field satisfies the balance of linear momentum, and it is [[symmetric|0VR671PHE5]] when angular momentum is also balanced.
For a fluid at rest with pressure $p$, $\sigma = -p I$, and indeed $t(x, n) = -p\, n$.
For uniaxial tension of size $s$ along $e_1$, $\sigma = s\, e_1 e_1^T$, the matrix with $\sigma_{11} = s$ and all other entries $0$.
A traction field such as $t(x, n) = \abs{n_1} e_1$ has no Cauchy stress tensor, since it is not linear in $n$.
The diagonal entries $\sigma_{11}, \sigma_{22}, \sigma_{33}$ are normal stresses, and the off-diagonal entries are shear stresses.

## Explanations

### L1 human

The Cauchy stress tensor is the matrix that turns the direction of a cut into the force per area across the cut.
It is the basic way to record stress at a point.
