---
tag: YT3GZ6YCAH
kind: statement
role: proposition
name: Universal property of the direct product of vector spaces
msc: ["15A03", "18A30"]
topics: [QHKTJ89V6S]
audience: ug2
about: [0EX2HPXPJ6]
uses: [0MM085RX00, 0RJF668P1T, 05EGHEQZAW]
formal:
  - system: lean4
    library: mathlib
    decl: LinearMap.pi
    match: partial
sources:
  - url: https://en.wikipedia.org/wiki/Product_(category_theory)
    locator: Examples
  - book: isbn:9783031410253
    locator: Section 3E
---

## Statement

A linear map into a direct product is the same thing as one linear map into each factor.
Let $F$ be a field, let $(V_i)_{i \in I}$ be a family of vector spaces over $F$, and let $\pi_j \colon \prod_{i \in I} V_i \to V_j$ be the projections of the [[direct product|0MM085RX00]].
Let $X$ be a [[vector space|05EGHEQZAW]] over $F$, and for each $i \in I$ let $g_i \colon X \to V_i$ be a [[linear map|0RJF668P1T]].
Then there is exactly one linear map $g \colon X \to \prod_{i \in I} V_i$ with $\pi_i \circ g = g_i$ for every $i \in I$, namely
$$g(x) = \big(g_i(x)\big)_{i \in I}.$$

## Remarks

### Why each hypothesis is needed

The maps $g_i$ must be linear.
The composition $\pi_1 \circ g$ of two linear maps is linear, so it can never equal a map such as $g_1(t) = t^2$ on $\R$.

All the maps $g_i$ must start from the same space $X$.
The formula evaluates every $g_i$ at the same vector $x$, and that makes sense only when $x$ lies in the domain of each of them.

The target must be the full product, not the [[external direct sum|0S7W6EG32V]].
Take $X = \R$ and $g_i(t) = t$ for each $i \in \N$.
The combined map would need $g(1) = (1, 1, 1, \dots)$, which lies in $\R^{\N}$ but not in the direct sum $\R^{(\N)}$.

### What it gives you

Take $X = \R$, $V_1 = \R^2$ and $V_2 = \R$, with $g_1(t) = (t, -t)$ and $g_2(t) = 3t$.
The formula gives
$$g(t) = ((t, -t), 3t),$$
and then $\pi_1(g(t)) = (t, -t) = g_1(t)$ and $\pi_2(g(t)) = 3t = g_2(t)$.
In coordinates of $\R^3$, the matrix of $g$ is the column $(1, -1, 3)^{\mathsf{T}}$.
In general a linear map into $V_1 \times V_2$ has the block column matrix $\begin{pmatrix} B_1 \\ B_2 \end{pmatrix}$, with the matrix of $g_1$ on top of the matrix of $g_2$.

The statement also says that the map $g \mapsto (\pi_i \circ g)_i$ is an isomorphism of spaces of linear maps,
$$\mathcal{L}\Big(X, \prod_{i \in I} V_i\Big) \cong \prod_{i \in I} \mathcal{L}(X, V_i).$$

### The converse

The property determines the product up to a unique isomorphism.
Let a space $P$ with linear maps $p_i \colon P \to V_i$ have the same property.
The property of the product gives $\varphi \colon P \to \prod_i V_i$ with $\pi_i \circ \varphi = p_i$, and the property of $P$ gives $\psi \colon \prod_i V_i \to P$ with $p_i \circ \psi = \pi_i$.
Then $\pi_i \circ (\varphi \circ \psi) = \pi_i$ for every $i$, and the identity satisfies the same equations, so $\varphi \circ \psi$ is the identity by uniqueness.
In the same way $\psi \circ \varphi$ is the identity of $P$, so $\varphi$ is an isomorphism, and the property is the definition of the [[categorical product|S5744QZV4N]].

### Generalizations

The same statement and proof hold for modules over any ring, and for products of sets, groups and rings.
The dual statement, with maps out of a space instead of maps into it, is the [[universal property of the external direct sum|N04WS31KXB]].

## History

Describing a construction by the maps into it or out of it belongs to category theory, which Eilenberg and Mac Lane founded in 1945.

## Explanations

### L1 human

To give a linear map into a product, give a linear map into each factor.
The combined map lists the results.
For example, if one map sends $t$ to $(t, -t)$ and another sends $t$ to $3t$, the combined map sends $2$ to $((2, -2), 6)$.
There is no other choice, because a vector of the product is known once all its entries are known.

### L2 human

We find the linear map $g \colon \R^2 \to \R \times \R \times \R$ with parts $g_1(x, y) = x$, $g_2(x, y) = x + y$ and $g_3(x, y) = 2y$.
The formula lists the three values:
$$g(x, y) = (x, x + y, 2y).$$
Check at $(1, 2)$: the three parts give $1$, $3$ and $4$, and $g(1, 2) = (1, 3, 4)$.
The matrix of $g$ stacks the three rows of the parts:
$$\begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 2 \end{pmatrix}.$$
The typical use is this: a map into a product is designed one factor at a time.
Watch out: for infinitely many factors the combined map can leave the direct sum, so the target must be the product.

### L3 human

The product represents the functor $X \mapsto \prod_i \mathcal{L}(X, V_i)$.
This is dual to the universal property of the direct sum, which describes the maps out of $\bigoplus_i V_i$.
For finitely many factors the same space has both properties, so finite products of vector spaces are biproducts.
Mathlib builds the induced map as `LinearMap.pi`.
