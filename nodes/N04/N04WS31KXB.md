---
tag: N04WS31KXB
kind: statement
role: proposition
name: Universal property of the external direct sum
msc: ["15A03", "18A30"]
topics: [QHKTJ89V6S]
audience: ug2
about: [0S7W6EG32V]
uses: [02WZB422CE, 0RJF668P1T, 05EGHEQZAW]
formal:
  - system: lean4
    library: mathlib
    decl: DirectSum.toModule
    match: partial
sources:
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Universal property
  - book: isbn:9783031410253
    locator: Section 3E
---

## Statement

A linear map out of a direct sum is the same thing as one linear map on each summand.
Let $F$ be a field, let $(V_i)_{i \in I}$ be a family of vector spaces over $F$, and let $\iota_j \colon V_j \to \bigoplus_{i \in I} V_i$ be the canonical injections of the [[external direct sum|02WZB422CE]].
Let $X$ be a [[vector space|05EGHEQZAW]] over $F$, and for each $i \in I$ let $f_i \colon V_i \to X$ be a [[linear map|0RJF668P1T]].
Then there is exactly one linear map $f \colon \bigoplus_{i \in I} V_i \to X$ with $f \circ \iota_i = f_i$ for every $i \in I$.
It is given by
$$f\big((v_i)_{i \in I}\big) = \sum_{i \in I} f_i(v_i),$$
where the sum has only finitely many nonzero terms.

## Remarks

### Why each hypothesis is needed

The families in the direct sum must have finite support, because otherwise the formula is an infinite sum.
Replace the direct sum by the [[product|0EX2HPXPJ6]] $\R^{\N}$ and take $f_i(t) = t$ for each $i$.
At the vector $(1, 1, 1, \dots)$ the formula asks for $1 + 1 + 1 + \cdots$, which has no value in $\R$.

The maps $f_i$ must be linear.
A composition $f \circ \iota_1$ of two linear maps is linear, so it can never equal a map such as $f_1(t) = t^2$ on $\R$.

All the maps $f_i$ must take values in the same space $X$.
Otherwise the terms $f_i(v_i)$ lie in different spaces, and their sum has no meaning.

### What it gives you

Take $V_1 = \R^2$, $V_2 = \R$, $X = \R$, $f_1(x, y) = x + y$ and $f_2(t) = 2t$.
The formula gives the map
$$f((x, y), t) = x + y + 2t,$$
and $f((x, y), 0) = x + y$ and $f((0, 0), t) = 2t$ confirm that $f$ restricts to $f_1$ and $f_2$; the example of [[a map out of R² ⊕ R|RWST1DAHFM]] works this out in full.
In matrix form, a linear map out of $V_1 \oplus V_2$ has the block row matrix $\begin{pmatrix} A_1 & A_2 \end{pmatrix}$, here $\begin{pmatrix} 1 & 1 & 2 \end{pmatrix}$.

In general, the map $f \mapsto (f \circ \iota_i)_{i \in I}$ is an isomorphism of [[spaces of linear maps|0X9MBPP2Z3]],
$$\mathcal{L}\Big(\bigoplus_{i \in I} V_i, X\Big) \cong \prod_{i \in I} \mathcal{L}(V_i, X).$$
For $X = F$ this says that the dual of a direct sum is the product of the duals, $\left(\bigoplus_i V_i\right)^* \cong \prod_i V_i^*$.

### The converse

The property determines the direct sum up to a unique isomorphism.
Let a space $S$ with linear maps $j_i \colon V_i \to S$ have the same property.
The property of the direct sum gives $\varphi \colon \bigoplus_i V_i \to S$ with $\varphi \circ \iota_i = j_i$, and the property of $S$ gives $\psi \colon S \to \bigoplus_i V_i$ with $\psi \circ j_i = \iota_i$.
Then $(\psi \circ \varphi) \circ \iota_i = \iota_i$ for every $i$, and the identity map satisfies the same equations, so $\psi \circ \varphi$ is the identity by uniqueness.
In the same way $\varphi \circ \psi$ is the identity of $S$, so $\varphi$ is an isomorphism.
This is why the property is used as the definition of the [[coproduct|4FJ0S71P58]] in a category.

### Generalizations

The same statement and proof hold for modules over any ring, and for abelian groups.
For a finite family, the same space $V_1 \oplus \cdots \oplus V_k$ also has the [[universal property of the product|YT3GZ6YCAH]], so finite direct sums are both products and coproducts.

## History

Describing a construction by the maps out of it belongs to category theory, which Eilenberg and Mac Lane founded in 1945.
Pierre Samuel gave a general treatment of universal mappings in a paper of 1948.

## Explanations

### L1 human

To give a linear map out of a direct sum, give a linear map on each piece.
The map on the whole sum adds the results of the pieces.
For example, if one piece sends $(x, y)$ to $x + y$ and the other sends $t$ to $2t$, then the pair $((1, 2), 3)$ goes to $3 + 6 = 9$.
There is no other choice, because each vector of the sum is a sum of vectors from the pieces.

### L2 human

We find the linear map $f \colon \R \oplus \R \oplus \R \to \R^2$ with $f_1(s) = (s, 0)$, $f_2(t) = (t, t)$ and $f_3(u) = (0, -u)$ on the three summands.
The formula adds the three values:
$$f(s, t, u) = (s, 0) + (t, t) + (0, -u) = (s + t, t - u).$$
Check: $f(1, 0, 0) = (1, 0) = f_1(1)$, $f(0, 1, 0) = (1, 1) = f_2(1)$ and $f(0, 0, 1) = (0, -1) = f_3(1)$.
So the matrix of $f$ is the block row of the three columns,
$$\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & -1 \end{pmatrix}.$$
The typical use is exactly this: a map out of a direct sum is designed one summand at a time.
Watch out: for an infinite product in place of the direct sum, the same formula would need an infinite sum.

### L3 human

The property says that $\bigoplus_i V_i$ represents the functor $X \mapsto \prod_i \mathcal{L}(V_i, X)$.
Dually, the product $\prod_i V_i$ represents $X \mapsto \prod_i \mathcal{L}(X, V_i)$, by the [[universal property of the product|YT3GZ6YCAH]].
For finite families one space has both properties, so finite direct sums are biproducts and the category of vector spaces is additive.
Mathlib builds the induced map as `DirectSum.toModule`.
