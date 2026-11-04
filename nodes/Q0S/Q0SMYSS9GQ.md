---
tag: Q0SMYSS9GQ
kind: statement
role: proposition
name: Covering relation in the poset of partitions of an integer
msc: ["05A17", "06A07"]
uses: [0404R9P9J3, EHXHC4ZNPA]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_kitchensink_zero-one-matrices.ptx#L28
    locator: source/s_kitchensink_zero-one-matrices.ptx:28
---

## Statement

Let $t$ be a positive integer. Let $\mathcal{P}(t)$ be the poset of [[partitions|0404R9P9J3]] of $t$ under the dominance order. A partition is written as the list of its parts.

Let $V=(v_1,\dots,v_m)$ and $W=(w_1,\dots,w_n)$ be partitions of $t$, and suppose $V$ [[covers|EHXHC4ZNPA]] $W$ in $\mathcal{P}(t)$.

Then $n\le m+1$, and there are integers $i<j$ with $1\le i<j\le n$ such that all of the following hold.

1. $v_\alpha=w_\alpha$ for every $\alpha<i$.
2. $v_\beta=w_\beta$ for every $\beta$ with $j<\beta\le m$.
3. $v_i=w_i+1$.
4. One of two cases occurs. Either $j\le m$ and $w_j=v_j+1$, or $j=n=m+1$ and $w_j=1$.
5. If $j>i+1$, then $v_\gamma=w_\gamma=v_i-1$ for every $\gamma$ with $i<\gamma<j$.

## Remarks

In words, a cover moves one unit from an earlier part to a later part. The parts strictly between the two changed positions all equal $v_i-1$. In case (b) of item 4, the unit goes into a new last part of size $1$, so $W$ has one more part than $V$.
