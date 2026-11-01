---
tag: RC7HCZCRC5
kind: definition
name: Mori domain
msc: [13F05]
defines: 69HK75YAD1
uses: [09S3PFBEPM, 0VF11ZTTMD, 0MYSA6MYNA]
sources:
  - url: https://en.wikipedia.org/wiki/Mori_domain
---

## Definition

Let $A$ be an [[integral domain|09S3PFBEPM]] with [[field of fractions|0VF11ZTTMD]] $K$.
For a nonzero [[ideal|0MYSA6MYNA]] $I$ of $A$, let $I^{-1} = \set{x \in K : xI \subseteq A}$ and $I_v = \set{x \in K : x I^{-1} \subseteq A}$.
The ideal $I$ is *divisorial* if $I_v = I$.
$A$ is a *Mori domain* if every strictly ascending chain $I_1 \subsetneq I_2 \subsetneq \cdots$ of nonzero divisorial ideals of $A$ is finite.

## Remarks

Every nonzero principal ideal $aA$ is divisorial, since $(aA)^{-1} = a^{-1}A$ and then $(aA)_v = aA$.
Example: every Noetherian domain is a Mori domain, since it has no infinite strictly ascending chain of ideals at all.
Non-example: the ring $\overline{\Z}$ of all algebraic integers is not Mori; the principal ideals $(2^{1/2^n})$ for $n \ge 1$ form a strictly ascending chain, since $2^{1/2^{n+1}} / 2^{1/2^{n}} = 2^{-1/2^{n+1}}$ is not an algebraic integer.
Every [[Krull domain|CB9WJCN9BM]] is a Mori domain, and a Mori domain is Krull if and only if it is completely integrally closed.
