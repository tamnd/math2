---
tag: ~ef14dc2c
kind: statement
role: proposition
name: Dimension of the space of linear maps
msc: [15A03, 15A04]
uses: [~c02afeb7, ~a94fe0ae]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Vector space of linear maps
---

## Statement

Let $F$ be a field and let $V$ and $W$ be finite-dimensional vector spaces over $F$.
Then the [[space of linear maps|~0acf07d9]] $\Hom_F(V, W)$ is finite-dimensional, and
$$\dim \Hom_F(V, W) = \dim V \cdot \dim W.$$

## Remarks

With bases of $V$ and $W$, the map that sends $T$ to its matrix is an isomorphism $\Hom_F(V, W) \cong M_{m \times n}(F)$, with $n = \dim V$ and $m = \dim W$.
The matrices $E_{ij}$ form a basis of $M_{m \times n}(F)$, so its dimension is $mn$.
In particular, the [[dual space|~d8a7f260]] of $V$ has dimension $\dim V$.

## Explanations

### L1 human

A linear map from an $n$-dimensional space to an $m$-dimensional space is an $m \times n$ matrix.
A matrix of this size has $mn$ free entries.
So the space of these maps has dimension $mn$.
