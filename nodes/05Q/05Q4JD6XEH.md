---
tag: 05Q4JD6XEH
kind: definition
name: Orthogonal family for a bilinear form
msc: [15A63]
defines: 01TXN7ETH2
uses: [0P799D6AMN]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Reflexive bilinear forms and orthogonal vectors
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, and let $B$ be a [[bilinear form|0SQZMXB6GP]] on $V$.
A family $(v_i)_{i \in I}$ of vectors of $V$ is *orthogonal* for $B$ when
$$B(v_i, v_j) = 0 \qquad \text{for all } i, j \in I \text{ with } i \ne j.$$

## Remarks

For an inner product, this is the usual notion of an orthogonal family.
For a general $B$, the relation $B(u, v) = 0$ need not be symmetric in $u$ and $v$; it is symmetric for symmetric and alternating forms.
In a basis that is orthogonal for $B$, the matrix of $B$ is diagonal.
Unlike in an inner product space, a nonzero vector can be orthogonal to itself: for $B(x, y) = x_1 y_1 - x_2 y_2$, take $v = (1, 1)$.

## Explanations

### L1 human

Orthogonality makes sense for every bilinear form, not only for inner products.
Two vectors are orthogonal when the form gives zero.
A basis of pairwise orthogonal vectors makes the matrix of the form diagonal.
