---
tag: WC9WZ53ZNS
kind: definition
name: Invariant basis number
msc: [16D40, "16E20"]
defines: AG1GMQDTDW
uses: [0B1261B5ED, 0NZ8JA25WK, 0DZ9DKAKZR]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_basis_number
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with $1$.
For an integer $n \ge 0$, let $R^n$ be the [[free left module|0DZ9DKAKZR]] of rank $n$ over $R$.
The ring $R$ has *invariant basis number* (IBN) if, for all integers $m, n \ge 0$, an isomorphism $R^m \cong R^n$ of left $R$-[[modules|0NZ8JA25WK]] implies $m = n$.

## Remarks

Example: every nonzero commutative ring $R$ has IBN.
To check it, take a maximal ideal $\mathfrak{m}$ of $R$; an isomorphism $R^m \cong R^n$ gives an isomorphism $(R/\mathfrak{m})^m \cong (R/\mathfrak{m})^n$ of vector spaces over the field $R/\mathfrak{m}$, so $m = n$ by dimension.

Non-example: let $V$ be a vector space of countably infinite dimension over a field $k$ and let $R = \End_k(V)$.
Since $V \cong V \oplus V$, one gets $R \cong R^2$ as left $R$-modules, so $R$ does not have IBN.

The zero ring does not have IBN, since $0 = R^m$ for all $m$.
The condition can be stated with matrices: $R$ has IBN if and only if there are no matrices $A \in R^{m \times n}$ and $B \in R^{n \times m}$ with $m \ne n$, $AB = I_m$ and $BA = I_n$.
This form is symmetric in left and right, so the definition does not depend on the side.
