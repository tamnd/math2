---
tag: V3G5YQTQ00
kind: statement
role: theorem
name: Eilenberg–Zilber theorem
msc: [55U25, 55N10]
uses: [M0Q5CFJ7ZH]
about: [M0Q5CFJ7ZH]
sources:
  - url: https://en.wikipedia.org/wiki/Eilenberg%E2%80%93Zilber_theorem
same_as:
  wikidata: Q1349282
  wikipedia: Eilenberg–Zilber theorem
---

## Statement

Let $X$ and $Y$ be topological spaces with singular [[chain complexes|WQ82C0M3QB]] $C_\bullet(X)$ and $C_\bullet(Y)$.
Let $C_\bullet(X) \otimes C_\bullet(Y)$ be the tensor product chain complex, with $(C_\bullet(X) \otimes C_\bullet(Y))_n = \bigoplus_{i + j = n} C_i(X) \otimes_{\Z} C_j(Y)$ and $\partial(a \otimes b) = \partial a \otimes b + (-1)^i a \otimes \partial b$ for $a \in C_i(X)$.
Then there are [[chain maps|HTK9WQZJ1G]]
$$C_\bullet(X \times Y) \rightleftarrows C_\bullet(X) \otimes C_\bullet(Y),$$
natural in $X$ and $Y$, that are inverse to each other up to [[chain homotopy|4EBHAWJJ8C]].
In particular, $H_n(X \times Y) \cong H_n\big(C_\bullet(X) \otimes C_\bullet(Y)\big)$ for every $n$.

## Remarks

A standard choice of maps is the Alexander–Whitney map from $C_\bullet(X \times Y)$ and the shuffle map into it.
The existence and uniqueness up to homotopy of such natural maps follows from the method of acyclic models.
Both functors are free on the models $(\Delta^p, \Delta^q)$ and acyclic on them, because $\Delta^p \times \Delta^q$ is contractible.

Example: with the algebraic [[Künneth theorem|77K0BZQ4MK]], the theorem gives the topological Künneth formula.
Over a field $F$, $H_n(X \times Y; F) \cong \bigoplus_{i + j = n} H_i(X; F) \otimes_F H_j(Y; F)$.
For the torus $S^1 \times S^1$ this gives $H_1 \cong F^2$ and $H_2 \cong F$.

## Explanations

### L1 human

The product of two spaces, such as a square from two intervals, can be cut into pieces in two ways.
One can use simplices of the product, or products of a simplex of each factor.
The theorem says that both ways give the same homology.
So the homology of a product can be computed from the chains of the two factors.

### L2 human

The theorem is the bridge between the homology of a product and the algebra of tensor products of chain complexes.
Combined with the Künneth theorem of homological algebra, it computes the homology of products.
The Alexander–Whitney map, composed with the diagonal $X \to X \times X$, also gives the cup product on singular cohomology.
