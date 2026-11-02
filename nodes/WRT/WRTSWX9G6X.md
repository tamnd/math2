---
tag: WRTSWX9G6X
kind: definition
name: Maximal order
msc: [16H10, 11R54]
defines: E5DH1CSW1N
uses: [1ZBX4TKVZ9, 7NPY2CN5KB, X8H7A98Q55, MWBDFS2KJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Order_(ring_theory)
---

## Definition

Let $R$ be a Noetherian integral domain with field of fractions $K$, and let $A$ be a finite-dimensional algebra over $K$.
An $R$-[[order|1ZBX4TKVZ9]] $\Lambda$ in $A$ is *maximal* if there is no $R$-order $\Lambda'$ in $A$ with $\Lambda \subsetneq \Lambda'$.

## Remarks

Example: $M_n(\Z)$ is a maximal $\Z$-order in $M_n(\Q)$.
Example: for an [[algebraic number field|MWBDFS2KJ5]] $F$, the ring of integers $\mathcal{O}_F$ is the unique maximal $\Z$-order in $F$.
The reason is that every element of an order is integral over $\Z$ and so lies in $\mathcal{O}_F$.
Non-example: $\Z[\sqrt{-3}]$ is an order in $\Q(\sqrt{-3})$, but it is strictly contained in the order $\Z[\omega]$ with $\omega = (1 + \sqrt{-3})/2$, so it is not maximal.
Maximal orders need not be unique: with $g = \operatorname{diag}(1, 2)$, the order $g M_2(\Z) g^{-1}$ is maximal in $M_2(\Q)$ and contains the matrix $\begin{pmatrix} 0 & 1/2 \\ 0 & 0 \end{pmatrix}$, which is not in $M_2(\Z)$.
If $R$ is a [[Dedekind domain|7NPY2CN5KB]] and $A$ is a [[separable algebra|X8H7A98Q55]] over $K$, every $R$-order in $A$ is contained in a maximal $R$-order.
