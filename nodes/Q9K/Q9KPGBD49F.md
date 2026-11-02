---
tag: Q9KPGBD49F
kind: definition
name: Order (ring theory)
msc: [16H10, 11R54, 16G30]
defines: 1ZBX4TKVZ9
uses: [0QVD7WBFGN, 0F2PTGX1A2, 3CTW1P4HBP, 0GNCRPYXYV, 05QY1VEBYD]
sources:
  - url: https://en.wikipedia.org/wiki/Order_(ring_theory)
---

## Definition

Let $R$ be a Noetherian [[integral domain|0QVD7WBFGN]] with [[field of fractions|0F2PTGX1A2]] $K$, and let $A$ be a finite-dimensional [[associative algebra|3CTW1P4HBP]] over $K$.
An *$R$-order* in $A$ is a [[subring|0GNCRPYXYV]] $\Lambda$ of $A$, with the same identity, such that:

1. $\Lambda$ is a [[finitely generated|05QY1VEBYD]] $R$-module.
2. $\Lambda$ contains a $K$-basis of $A$, that is $K \Lambda = A$.

## Remarks

Example: $\Lambda = \Z[i]$ in $A = \Q(i)$, with $R = \Z$.
It is a subring containing $1$, it is generated as a $\Z$-module by $1$ and $i$, and $1, i$ is a $\Q$-basis of $\Q(i)$.
Other examples are $M_n(\Z)$ in $M_n(\Q)$ and the group ring $\Z G$ of a finite group $G$ in $\Q G$.
Non-example: $\Z[\tfrac{1}{2}]$ is a subring of $\Q$ that spans $\Q$, but it is not a finitely generated $\Z$-module, so clause 1 fails.
Non-example: $\Z$ inside $\Q(i)$ is finitely generated but fails clause 2, since $\Q \cdot \Z = \Q \ne \Q(i)$.
When $R$ is a principal ideal domain, clause 1 makes $\Lambda$ a free $R$-module, and clause 2 then says its rank is $\dim_K A$.
Every element of an order is integral over $R$.
