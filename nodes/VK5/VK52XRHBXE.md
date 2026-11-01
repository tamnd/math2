---
tag: VK52XRHBXE
kind: definition
name: Torsion submodule
msc: [13C12, 13C05]
defines: 6PBS6KW0NC
uses: [0310REJJY8, 0NZ8JA25WK, 05WDSN597C, 0NNRDW10RZ]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_(algebra)
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $M$ be an [[$R$-module|0NZ8JA25WK]].
An element $m \in M$ is a *torsion element* if $r m = 0$ for some $r \in R$ that is not a [[zero divisor|0NNRDW10RZ]] of $R$.
The *torsion submodule* of $M$ is the set
$$T(M) = \set{m \in M : r m = 0 \text{ for some non-zero-divisor } r \in R}.$$
The module $M$ is *torsion-free* if $T(M) = 0$, and it is a *torsion module* if $T(M) = M$.

## Remarks

The set $T(M)$ is a [[submodule|05WDSN597C]]: if $r m = 0$ and $s n = 0$ with $r, s$ non-zero-divisors, then $rs$ is a non-zero-divisor and $rs(m + n) = 0$, and $r(am) = a(rm) = 0$ for $a \in R$.
Example: for $R = \Z$ and $M = \Z \oplus \Z/6\Z$, one has $T(M) = 0 \oplus \Z/6\Z$, since $6 (k, c) = (6k, 0)$ is zero exactly when $k = 0$.
Non-example: the element $(1, 0)$ of this $M$ is not torsion, because $n (1, 0) = (n, 0) \ne 0$ for every nonzero integer $n$.
When $R$ is an [[integral domain|0QVD7WBFGN]], the non-zero-divisors are the nonzero elements, and $M / T(M)$ is torsion-free.
For $R = \Z$ the torsion submodule is the [[torsion subgroup|0DBWXQRXQJ]].
