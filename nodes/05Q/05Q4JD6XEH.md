---
tag: 05Q4JD6XEH
kind: definition
name: Orthogonality for a bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
defines: 01TXN7ETH2
uses: [0P799D6AMN]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Reflexive bilinear forms and orthogonal vectors
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: General bilinear forms
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, and let $B$ be a [[bilinear form|0P799D6AMN]] on $V$.

1. Vectors $u, v \in V$ are *orthogonal* for $B$, written $u \perp v$, when $B(u, v) = 0$.
2. A family $(v_i)_{i \in I}$ of vectors of $V$ is *orthogonal* for $B$ when $B(v_i, v_j) = 0$ for all $i, j \in I$ with $i \neq j$.
3. For a subset $W \subseteq V$, the *orthogonal complement* of $W$ is
$$W^\perp = \{v \in V : B(w, v) = 0 \text{ for all } w \in W\}.$$
4. An *orthogonal basis* is a basis that is an orthogonal family.

## Notation

The set in item 3 is the right orthogonal complement.
The left orthogonal complement is ${}^\perp W = \{u \in V : B(u, w) = 0 \text{ for all } w \in W\}$.
For a symmetric or alternating form, the two complements are equal.

## Remarks

For an inner product, these are the usual notions of orthogonal vectors, families and complements.
For a general $B$, the relation $u \perp v$ need not be symmetric in $u$ and $v$.
It is symmetric exactly for the [[reflexive forms|~b3103bb5]].
In a basis that is orthogonal for $B$, the matrix of $B$ is diagonal.
Unlike in an inner product space, a nonzero vector can be orthogonal to itself: for $B(x, y) = x_1 y_1 - x_2 y_2$, take $v = (1, 1)$.
The set $W^\perp$ is a subspace of $V$ for every subset $W$, since it is an intersection of kernels of linear forms $B(w, \cdot)$.

## Explanations

### L1 human

Orthogonality makes sense for every bilinear form, not only for inner products.
Two vectors are orthogonal when the form gives zero.
The orthogonal complement of a subspace collects all vectors orthogonal to each vector of the subspace.
A basis of pairwise orthogonal vectors makes the matrix of the form diagonal.

### L2 human

For $B(x, y) = x_1 y_2$ on $F^2$ and $W = \operatorname{span}(e_1)$, we get $W^\perp = \{v : v_2 = 0\} = W$.
The left complement is ${}^\perp W = \{u : B(u, e_1) = 0\} = F^2$, since $B(u, e_1) = 0$ for every $u$.
A trap: for a form that is not reflexive, the left and the right complements can differ, as here.
