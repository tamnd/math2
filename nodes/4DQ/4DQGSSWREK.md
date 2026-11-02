---
tag: 4DQGSSWREK
kind: definition
name: General recursive function
msc: [03D20]
defines: HBK5QHC1GC
uses: [5NVA2JRHPV, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/General_recursive_function
---

## Definition

A partial function $f \colon \N^k \rightharpoonup \N$ is a function from a subset of $\N^k$ to $\N$, where $\N$ is the set of [[natural numbers|0MWKJ44V5A]].
For a partial function $g \colon \N^{k+1} \rightharpoonup \N$, the *minimisation* $\mu g \colon \N^k \rightharpoonup \N$ is defined as follows.
The value $\mu g(\bar x)$ is the least $y$ such that $g(y, \bar x) = 0$ and $g(z, \bar x)$ is defined for all $z < y$.
If no such $y$ exists, then $\mu g(\bar x)$ is undefined.

The class of *partial recursive functions*, or *$\mu$-recursive functions*, is the smallest class of partial functions $\N^k \rightharpoonup \N$ with these properties.

1. It contains the zero function, the successor function and the projections, as for [[primitive recursive functions|5NVA2JRHPV]].
2. It is closed under composition and primitive recursion, where a value is defined only when all values used to compute it are defined.
3. It is closed under minimisation.

A *general recursive function* is a partial recursive function that is total, that is, defined at every point of $\N^k$.

## Remarks

Example: let $g(y, x) = x \mathbin{\dot-} y \cdot y$, where $a \mathbin{\dot-} b = \max(a - b, 0)$.
The function $g$ is primitive recursive, and $g(y, x) = 0$ exactly when $y^2 \ge x$.
So $\mu g(x) = \ceil{\sqrt x}$, which is defined for all $x$, and $\mu g$ is general recursive.

Non-example: let $g(y, x) = y + 1$, which is never $0$.
Then $\mu g$ is the empty function, which is partial recursive but not total, so it is not general recursive.

Terminology varies: some authors use "general recursive" for all partial recursive functions.
Every primitive recursive function is general recursive, and the [[Ackermann function|N470JF7ZJX]] shows that the converse fails.
