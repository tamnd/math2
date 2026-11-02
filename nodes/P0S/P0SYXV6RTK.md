---
tag: P0SYXV6RTK
kind: definition
name: Coalgebra
msc: [16T15]
defines: A06RA8KB0T
uses: [04C5ZBG1WT, 000AYPA9AJ, 0BF2DE2SYK, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Coalgebra
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]].
A *coalgebra* over $K$ is a [[vector space|000AYPA9AJ]] $C$ over $K$ with [[linear maps|0NRYHJPQG2]] $\Delta \colon C \to C \otimes C$, the comultiplication, and $\varepsilon \colon C \to K$, the counit, such that:

1. $(\Delta \otimes \id_C) \circ \Delta = (\id_C \otimes \Delta) \circ \Delta$ as maps $C \to C \otimes C \otimes C$ (coassociativity).
2. $(\varepsilon \otimes \id_C) \circ \Delta = \id_C = (\id_C \otimes \varepsilon) \circ \Delta$, where $K \otimes C$ and $C \otimes K$ are identified with $C$ (counit law).

Here $\otimes$ is the [[tensor product|0BF2DE2SYK]] over $K$.

## Remarks

Example: for a set $S$, let $C = K[S]$ be the vector space with basis $S$, and put $\Delta(s) = s \otimes s$ and $\varepsilon(s) = 1$ for $s \in S$.
Both sides of clause 1 send $s$ to $s \otimes s \otimes s$, and both maps in clause 2 send $s$ to $1 \cdot s = s$.
Non-example: the same $\Delta$ with $\varepsilon(s) = 0$ for all $s$ fails clause 2, since $(\varepsilon \otimes \id)\Delta(s) = 0 \ne s$.
Another example is $K[x]$ with $\Delta(x^n) = \sum_{k=0}^{n} \binom{n}{k} x^k \otimes x^{n-k}$ and $\varepsilon(x^n) = 1$ if $n = 0$ and $0$ otherwise.
The definition works in the same way over a commutative ring in place of $K$.
Over a field, every element of a coalgebra lies in a finite-dimensional subcoalgebra.
