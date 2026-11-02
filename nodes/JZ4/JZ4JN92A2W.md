---
tag: JZ4JN92A2W
kind: definition
name: Symmetric monoidal category
msc: [18M05]
defines: 5S7ER95XAC
uses: [VT8SFWT0XW, M3MSQ3NKAE]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_monoidal_category
---

## Definition

A *symmetric monoidal category* is a [[braided monoidal category|VT8SFWT0XW]] $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho, \gamma)$ such that for all objects $A, B$ of $\mathcal{C}$
$$\gamma_{B,A} \circ \gamma_{A,B} = \id_{A \otimes B}.$$

## Remarks

Under this condition the two hexagon identities of the braiding are equivalent, so one of them suffices.
Example: $\mathbf{Vect}_k$ with $\gamma(v \otimes w) = w \otimes v$; applying the swap twice returns $v \otimes w$.
Example: $\Z/2$-graded vector spaces with the Koszul sign $\gamma(v \otimes w) = (-1)^{\abs{v}\abs{w}}\, w \otimes v$ on homogeneous elements; the signs cancel when the swap is applied twice.
Non-example: $\Z/3$-graded complex vector spaces with $\gamma(v \otimes w) = q^{\abs{v}\abs{w}}\, w \otimes v$, where $q = e^{2\pi i/3}$.
This is a braiding because $(a, b) \mapsto q^{ab}$ is a bicharacter of $\Z/3$, but applying it twice multiplies $v \otimes w$ by $q^{2\abs{v}\abs{w}}$, which is not $1$ when $\abs{v} = \abs{w} = 1$.
Symmetric monoidal categories form the special case of [[monoidal categories|M3MSQ3NKAE]] that model commutative operations.
