---
tag: TDCZV0SE8Z
kind: definition
name: Kingman's coalescent
msc: [60J90, 92D15]
defines: P2H42E2V2N
uses: [2W8Y2Y1C8J, TWQFE0FZZS, 08QMKTWF9T, 0E99F51GVB]
sources:
  - url: https://en.wikipedia.org/wiki/Coalescent_theory
---

## Definition

Let $n \ge 2$ and let $\mathcal P_n$ be the set of [[partitions|08QMKTWF9T]] of $\set{1, \dots, n}$.
*Kingman's $n$-coalescent* is the [[continuous-time Markov chain|TWQFE0FZZS]] $(\Pi_t)_{t \ge 0}$ on $\mathcal P_n$ such that:

1. $\Pi_0$ is the partition into singletons.
2. From a partition with blocks $B_1, \dots, B_k$, each pair of blocks $\set{B_i, B_j}$ merges into the single block $B_i \cup B_j$ at rate $1$.
3. No other transitions occur.

## Remarks

While there are $k$ blocks the holding time $T_k$ has the [[exponential distribution|0E99F51GVB]] with rate $\binom{k}{2}$, and the merging pair is uniform among the $\binom{k}{2}$ pairs.
So the expected time to the most recent common ancestor is $\sum_{k=2}^n 2/(k(k-1)) = 2(1 - 1/n)$, and the expected total branch length is $\sum_{k=2}^n k \cdot 2/(k(k-1)) = 2 \sum_{i=1}^{n-1} 1/i$.
Example: for $n = 3$, the first merger comes after an exponential time of mean $1/3$ and joins each of the three pairs with probability $1/3$.
The second merger comes after a further exponential time of mean $1$.
Non-example: a chain on $\mathcal P_n$ in which three blocks may merge at once at positive rate fails clause 3; such chains are the $\Lambda$-coalescents with multiple mergers.
In the haploid Wright–Fisher model with $N$ genes, one unit of time of the coalescent corresponds to $N$ generations ([[coalescent theory|2W8Y2Y1C8J]]).
