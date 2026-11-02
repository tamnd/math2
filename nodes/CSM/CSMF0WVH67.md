---
tag: CSMF0WVH67
kind: definition
name: Deficiency indices
msc: [47B25, 47A20]
defines: G4GMSNAX8X
uses: [HM2HHE3J51, H971WGMV6C, 86B7HF79PQ, 0S23E6YE83, 0WSFKKT6FF, 40SV748R64, DT49GKR9AS]
sources:
  - url: https://en.wikipedia.org/wiki/Extensions_of_symmetric_operators
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]], and let $A$ be a [[symmetric operator|H971WGMV6C]] on $H$ with dense domain and [[adjoint|86B7HF79PQ]] $A^*$.
The *deficiency subspaces* of $A$ are the closed subspaces
$$K_+ = \ker(A^* - iI), \qquad K_- = \ker(A^* + iI)$$
of $H$, where $\ker$ denotes the [[kernel|0S23E6YE83]].
The *deficiency indices* of $A$ are the [[Hilbert dimensions|40SV748R64]] $n_+ = \dim K_+$ and $n_- = \dim K_-$, which are cardinal numbers, possibly infinite.

## Remarks

Equivalently, $K_\pm$ is the orthogonal complement of the [[image|0WSFKKT6FF]] of $A \pm iI$.
Some authors exchange the names of $K_+$ and $K_-$; the pair $(n_+, n_-)$ is then reversed.
The operator $A$ is [[essentially self-adjoint|DT49GKR9AS]] if and only if $n_+ = n_- = 0$.
Example: on $L^2([0,1])$, let $A = -i \, d/dx$ on the smooth functions with compact support in $(0,1)$.
Then $A^*$ is $-i \, d/dx$ on the Sobolev space $H^1([0,1])$, and $A^* u = \pm i u$ means $u' = \mp u$.
So $K_+$ is spanned by $e^{-x}$ and $K_-$ by $e^{x}$, and $(n_+, n_-) = (1, 1)$.
Example with unequal indices: on $L^2([0, \infty))$, the same construction gives $K_+$ spanned by $e^{-x}$, while $e^{x}$ is not square integrable, so $(n_+, n_-) = (1, 0)$.
Non-example: the deficiency indices are not defined for an operator that is not densely defined, because then the adjoint is not a well-defined operator.
