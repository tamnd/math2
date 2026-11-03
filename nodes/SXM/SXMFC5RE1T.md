---
tag: SXMFC5RE1T
kind: statement
role: theorem
name: Unique size of a nonempty finite set
msc: ["03E10", "05A05"]
uses: [0BBTH3YSZA, 0GG9TVW90M]
about: [05099E1NMJ]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_background_finite-sets.ptx#L6
    locator: source/s_background_finite-sets.ptx:6
---

## Statement

Let $X$ be a nonempty [[finite set|0BBTH3YSZA]]. Write $[n]$ for the set $\{1, 2, \dots, n\}$.
Then exactly one positive integer $n$ admits a [[bijection|0GG9TVW90M]] from $[n]$ onto $X$.

## Remarks

The number $n$ is the number of elements of $X$. This is why the [[cardinality of a finite set|05099E1NMJ]] is well defined.
Existence of $n$ is the definition of finiteness, and nonemptiness makes $n$ positive.
Uniqueness follows from the fact that no injection maps $[m]$ into $[n]$ when $m > n$.
