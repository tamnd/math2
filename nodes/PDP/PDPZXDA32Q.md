---
tag: PDPZXDA32Q
kind: statement
role: lemma
name: Number of functions that avoid a given set of values
msc: [05A05]
uses: [05099E1NMJ, 08QQH9F7G0, 0Q3F20XB0A]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_inclusion-exclusion_surjections.ptx#L9
    locator: source/s_inclusion-exclusion_surjections.ptx:9
---

## Statement

Let $m$ and $n$ be positive integers. Put $[m]=\{1,\dots,m\}$ and $[n]=\{1,\dots,n\}$.

For a subset $S\subseteq[m]$, let $N(S)$ be the number of functions from $[n]$ to $[m]$ whose [[image|0Q3F20XB0A]] contains no element of $S$.

Then $N(S)$ depends only on the [[cardinality|05099E1NMJ]] of $S$. If $|S|=k$, then
$$N(S)=(m-k)^n.$$

## Remarks

A function that avoids $S$ is the same as a function from $[n]$ to the set $[m]\setminus S$, which has $m-k$ elements. The [[count of functions between finite sets|08QQH9F7G0]] gives $(m-k)^n$.

For $k=m$ the value is $0$, since $n\ge 1$ and there is no function into the empty set.
