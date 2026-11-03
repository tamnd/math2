---
tag: WXBB2NRRMY
kind: definition
name: Nussinov algorithm
msc: [92C40, 92D20, 90C39]
defines: EH7XF8CNFQ
uses: [R3FXF08WBH, 1P6EP01HZF]
sources:
  - url: https://en.wikipedia.org/wiki/Nussinov_algorithm
---

## Definition

Let $s = s_1 \cdots s_n$ be a [[string|1P6EP01HZF]] over $\set{A, C, G, U}$, and call $\set{x, y}$ a *complementary pair* if it is $\set{A, U}$, $\set{G, C}$ or $\set{G, U}$.
A *secondary structure* of $s$ is a set $P$ of pairs $(i, j)$ with $1 \le i < j \le n$ such that:

1. $\set{s_i, s_j}$ is complementary for each $(i, j) \in P$;
2. each position lies in at most one pair of $P$;
3. there are no $(i, j), (k, l) \in P$ with $i < k < j < l$.

Let $\delta(i, j) = 1$ if $\set{s_i, s_j}$ is complementary and $\delta(i, j) = 0$ otherwise.
The *Nussinov algorithm* computes $N(i, j)$ for $1 \le i \le j \le n$, in order of increasing $j - i$, by $N(i, i) = 0$, $N(i, i-1) = 0$, and for $i < j$
$$N(i, j) = \max\Bigl( N(i+1, j),\ N(i, j-1),\ N(i+1, j-1) + \delta(i, j),\ \max_{i < k < j - 1} \bigl(N(i, k) + N(k+1, j)\bigr) \Bigr).$$
It returns $N(1, n)$, and a structure is recovered by traceback.

## Remarks

By induction on $j - i$, $N(i, j)$ is the largest size of a secondary structure of $s_i \cdots s_j$.
Indeed, in an optimal structure either $i$ or $j$ is unpaired, or $i$ pairs with $j$, or the structure splits into two independent parts.
There are $O(n^2)$ entries, each a maximum over $O(n)$ terms, so the time is $O(n^3)$.
A common variant also requires $j - i > h$ for each pair, so that a hairpin loop has at least $h$ unpaired bases; $h = 3$ is a usual choice.
Example: for $s = GGGAAACCC$ the pairs $(1, 9), (2, 8), (3, 7)$ form a secondary structure, even with $h = 3$, and it is optimal because $s$ has only three $C$ and no $U$, so $N(1, 9) = 3$.
Non-example: in $s = GCGC$ the set $\set{(1, 2), (3, 4), (1, 4)}$ is not a secondary structure, since position $1$ lies in two pairs.
