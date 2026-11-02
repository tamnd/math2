---
tag: RBPR7BK5T5
kind: definition
name: Bimodule
msc: [16D20]
defines: EM7FHAFD3N
uses: [0894J980RK, 09VDS2W1E8]
sources:
  - url: https://en.wikipedia.org/wiki/Bimodule
---

## Definition

Let $R$ and $S$ be [[rings|0894J980RK]].
An *$(R, S)$-bimodule* is an abelian group $M$ with these structures:

1. a left [[$R$-module|09VDS2W1E8]] structure $(r, m) \mapsto rm$;
2. a right $S$-module structure $(m, s) \mapsto ms$;
3. the compatibility $(rm)s = r(ms)$ for all $r \in R$, $m \in M$ and $s \in S$.

## Remarks

An $(R, R)$-bimodule is also called an $R$-bimodule.
Example: for a field $K$, the space $M_{m \times n}(K)$ of $m \times n$ matrices is an $(M_m(K), M_n(K))$-bimodule under matrix multiplication.
Clauses 1 and 2 are the usual rules of matrix arithmetic, and clause 3 is associativity $(AX)B = A(XB)$.
Every ring $R$ is an $R$-bimodule, and its sub-bimodules are its two-sided ideals.
Non-example: let $R$ be a noncommutative ring and give $R$ the "right action" $m \cdot s = sm$.
This fails clause 2, since $(m \cdot s) \cdot t = tsm$ while $m \cdot (st) = stm$, and $ts \ne st$ for some $s, t$.
For a commutative ring $K$, every $K$-module is a $K$-bimodule with $mk = km$.
