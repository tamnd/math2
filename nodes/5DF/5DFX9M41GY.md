---
tag: 5DFX9M41GY
kind: statement
role: theorem
name: Gale–Ryser theorem
msc: [05B20, 05A17]
uses: [0404R9P9J3, 0N1MY1T0W9, 5K7VT2VKZT]
about: [0404R9P9J3]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_kitchensink_zero-one-matrices.ptx#L60
    locator: source/s_kitchensink_zero-one-matrices.ptx:60
---

## Statement

Let $t$ be a positive integer, and let $R = (r_1 \ge r_2 \ge \dots)$ and $C = (c_1 \ge c_2 \ge \dots)$ be two [[partitions|0404R9P9J3]] of $t$.
A $0$-$1$ [[matrix|0N1MY1T0W9]] has row sums $R$ and column sums $C$ when it has one row for each part of $R$ and one column for each part of $C$, its entries are all $0$ or $1$, row $i$ adds up to $r_i$, and column $j$ adds up to $c_j$.

Let $R^d$ be the conjugate partition of $R$. Its $j$-th part is the number of parts of $R$ that are at least $j$.

Then a $0$-$1$ matrix with row sums $R$ and column sums $C$ exists if and only if $R^d$ dominates $C$ in the dominance order on partitions of $t$.
That is, for each $k \ge 1$, the sum of the $k$ largest parts of $R^d$ is at least the sum of the $k$ largest parts of $C$, where missing parts count as $0$.

## Remarks

The dominance condition is the [[majorization|5K7VT2VKZT]] of $C$ by $R^d$, applied to partitions of the same number.
Example: $R = (2, 2)$ and $C = (2, 2)$ give $R^d = (2, 2)$, which dominates $C$, and the matrix with all entries $1$ works.
Example: $R = (2, 2)$ and $C = (4)$ give $R^d = (2, 2)$, which does not dominate $(4)$, since $2 < 4$. No such matrix exists, as a column with $2$ rows cannot sum to $4$.
