---
tag: XYH30V13SE
kind: definition
name: Day convolution
msc: [18M05, 18D20]
defines: 457T9T7Y75
uses: [M3MSQ3NKAE, 1X0WKFQX8K, W9QTFV0Z8D, VJXS8AK67E, RN9D96ESWN, EKJBDD07TY]
sources:
  - url: https://en.wikipedia.org/wiki/Day_convolution
---

## Definition

Let $(\mathcal{C}, \otimes, I)$ be a small [[monoidal category|M3MSQ3NKAE]], and let $[\mathcal{C}, \mathbf{Set}]$ be the [[functor category|1X0WKFQX8K]] of functors $\mathcal{C} \to \mathbf{Set}$.
The *Day convolution* of $F, G \in [\mathcal{C}, \mathbf{Set}]$ is the functor $F \ast G \colon \mathcal{C} \to \mathbf{Set}$ given by the [[coend|W9QTFV0Z8D]]
$$(F \ast G)(c) = \int^{a, b \in \mathcal{C}} \Hom_{\mathcal{C}}(a \otimes b, c) \times F(a) \times G(b).$$
With unit object the [[hom functor|VJXS8AK67E]] $\Hom_{\mathcal{C}}(I, -)$, Day convolution makes $[\mathcal{C}, \mathbf{Set}]$ a monoidal category.

## Remarks

Equivalently, $F \ast G$ is the left [[Kan extension|RN9D96ESWN]] of the functor $(a, b) \mapsto F(a) \times G(b)$ on $\mathcal{C} \times \mathcal{C}$ along $\otimes \colon \mathcal{C} \times \mathcal{C} \to \mathcal{C}$.
Natural transformations $F \ast G \to H$ correspond to families of maps $F(a) \times G(b) \to H(a \otimes b)$ natural in $a$ and $b$.
Example: let $\mathcal{C}$ be the discrete category on $\N$ with $\otimes = +$ and $I = 0$, so a functor $F$ is a sequence of sets $F(0), F(1), \ldots$.
Since $\Hom(a + b, n)$ is a point when $a + b = n$ and empty otherwise, $(F \ast G)(n) = \bigsqcup_{a + b = n} F(a) \times G(b)$, the Cauchy product.
Non-example: the pointwise product $(F \times G)(c) = F(c) \times G(c)$ is also a monoidal structure, but it is not the Day convolution.
In the example above it pairs elements of equal degree, and its unit is the constant functor with value a point, not $\Hom(0, -)$.
The monoidal category $[\mathcal{C}, \mathbf{Set}]$ with Day convolution is [[closed|EKJBDD07TY]], and $a \mapsto \Hom_{\mathcal{C}}(a, -)$ is a strong monoidal functor $\mathcal{C}^{\mathrm{op}} \to [\mathcal{C}, \mathbf{Set}]$.
The same construction works for functors into a cocomplete closed symmetric monoidal category $\mathcal{V}$ in place of $\mathbf{Set}$.
