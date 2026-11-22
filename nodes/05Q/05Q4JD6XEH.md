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

Orthogonality for a bilinear form means that the form gives zero, and it extends the right angles of an inner product to every bilinear form.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $B$ be a [[bilinear form|0P799D6AMN]] on $V$.

1. Vectors $u, v \in V$ are *orthogonal* for $B$, written $u \perp v$, when $B(u, v) = 0$.
2. A family $(v_i)_{i \in I}$ of vectors of $V$ is *orthogonal* for $B$ when $B(v_i, v_j) = 0$ for all $i, j \in I$ with $i \ne j$.
3. For a subset $W \subseteq V$, the *orthogonal complement* of $W$ is
$$W^\perp = \{v \in V : B(w, v) = 0 \text{ for all } w \in W\}.$$
4. An *orthogonal basis* is a basis of $V$ that is an orthogonal family.

## Notation

The set in item 3 is the right orthogonal complement.
The left orthogonal complement is ${}^\perp W = \{u \in V : B(u, w) = 0 \text{ for all } w \in W\}$.
For a symmetric or an alternating form, the two complements are equal.

## Remarks

Each condition reads the form in one order, and the order matters.
In item 1 the vector $u$ sits in the first slot and $v$ in the second, so for a general $B$ the statement $u \perp v$ need not imply $v \perp u$.
The relation is symmetric exactly for the [[reflexive forms|M0G958M917]].
Item 2 asks nothing about $B(v_i, v_i)$, and this is what makes the matrix of $B$ in an orthogonal basis diagonal, with the values $B(v_i, v_i)$ on the diagonal.
In item 3, $W$ may be any subset, and $W^\perp$ is still a subspace, because it is the intersection of the kernels of the linear forms $B(w, \cdot)$ for $w \in W$.

For the dot product on $\mathbb{R}^n$ these are the usual notions.
For $B(x, y) = x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$, the vector $v = (1, 1)$ has $B(v, v) = 1 - 1 = 0$, so a nonzero vector can be orthogonal to itself, which no inner product allows.
The [[concept page|01TXN7ETH2]] works out complements and their dimensions.

## Explanations

### L1 human

Orthogonality makes sense for every bilinear form, not only for inner products.
Two vectors are orthogonal when the form gives zero on them.
The orthogonal complement of a subspace collects all the vectors that are orthogonal to every vector of the subspace.
A basis of pairwise orthogonal vectors makes the matrix of the form diagonal.

### L2 human

Take $B(x, y) = x_1 y_2$ on $F^2$ and $W = \operatorname{span}(e_1)$.
The right complement asks for $B(e_1, v) = v_2 = 0$, so $W^\perp = W$.
The left complement asks for $B(u, e_1) = u_1 \cdot 0 = 0$, which holds for every $u$, so ${}^\perp W = F^2$.
Watch out: for a form that is not reflexive, the left and right complements can differ, as here, so always say which one you mean.
