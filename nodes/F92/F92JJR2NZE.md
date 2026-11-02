---
tag: F92JJR2NZE
kind: definition
name: Hierarchical matrix
msc: [65F55, 65F05, 65N38]
defines: 5P5EMYHXE5
uses: [0VD9ZSWWJG, 0ZC9YTXZRY, 062D9KXJB1]
sources:
  - url: https://en.wikipedia.org/wiki/Hierarchical_matrix
---

## Definition

Let $I = \set{1, \dots, n}$ be an index set.
A *cluster tree* on $I$ is a rooted [[tree|062D9KXJB1]] whose nodes are nonempty subsets of $I$.
Its root is $I$, and the children of each node partition that node.
Let $\mathcal{P}$ be a partition of $I \times I$ into blocks $\tau \times \sigma$ with $\tau$ and $\sigma$ nodes of the cluster tree.
Let $\mathcal{P} = \mathcal{P}^{+} \cup \mathcal{P}^{-}$ be a split into *admissible* blocks $\mathcal{P}^{+}$ and the remaining blocks $\mathcal{P}^{-}$.
Let $k \ge 0$ be an integer.
Let $M$ be a real [[matrix|0VD9ZSWWJG]] with rows and columns indexed by $I$.
It is a *hierarchical matrix* ($\mathcal{H}$-matrix) of local rank $k$ for $\mathcal{P}$ if each admissible block has small rank.
That is, $M|_{\tau \times \sigma}$ has [[rank|0ZC9YTXZRY]] at most $k$ for every $\tau \times \sigma \in \mathcal{P}^{+}$.

## Remarks

Each admissible block is stored as a product $X Y^T$ with $X$ of size $\abs{\tau} \times k$ and $Y$ of size $\abs{\sigma} \times k$.
The blocks in $\mathcal{P}^{-}$ are stored in full; the partition is built so that they are small.
In applications each index $i$ carries a point $x_i \in \R^d$, and $\Omega_\tau$ is the set of points of a cluster $\tau$.
The standard admissibility condition is $\min(\operatorname{diam} \Omega_\tau, \operatorname{diam} \Omega_\sigma) \le \eta \operatorname{dist}(\Omega_\tau, \Omega_\sigma)$ for a fixed $\eta > 0$.
With this condition, the matrices of asymptotically smooth kernels such as $1 / \abs{x - y}$ are well approximated by $\mathcal{H}$-matrices of small rank.
Example: let $n = 2m$, split $I$ into halves $\tau_1$ and $\tau_2$, and call the two off-diagonal blocks admissible.
A block diagonal matrix has zero off-diagonal blocks, of rank $0$, so it is an $\mathcal{H}$-matrix of every local rank $k$.
Non-example: the exchange matrix, with ones on the antidiagonal, has off-diagonal blocks of rank $m$.
So it is not an $\mathcal{H}$-matrix of local rank $k < m$ for this partition.
