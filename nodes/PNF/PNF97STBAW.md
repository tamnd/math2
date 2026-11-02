---
tag: PNF97STBAW
kind: definition
name: k-means clustering
msc: [62H30]
defines: D5PN3G41D6
uses: [D9Y3A9RH6J, 08QMKTWF9T, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/K-means_clustering
---

## Definition

Let $x_1, \ldots, x_n \in \R^d$ and let $1 \le k \le n$.
For a [[partition|08QMKTWF9T]] of $\set{1, \ldots, n}$ into non-empty sets $S_1, \ldots, S_k$, let $m_j = \frac{1}{\abs{S_j}} \sum_{i \in S_j} x_i$ be the mean of cluster $j$.
The *$k$-means problem* is to find a partition that minimises the within-cluster sum of squares
$$W(S_1, \ldots, S_k) = \sum_{j=1}^k \sum_{i \in S_j} \abs{x_i - m_j}^2,$$
where $\abs{\cdot}$ is the [[Euclidean norm|0NPPGHQNXQ]].
*$k$-means clustering* is the [[clustering|D9Y3A9RH6J]] given by a solution, or by an approximate solution, of this problem.

## Remarks

Lloyd's algorithm starts from $k$ centres and repeats two steps: assign each $x_i$ to a nearest centre, then replace each centre by the mean of its assigned points.
Neither step increases $W$, and there are finitely many partitions, so the algorithm stops after finitely many steps, at a local minimum that need not be global.
Example: for $0, 1, 10, 11 \in \R$ and $k = 2$, the partition $\set{0, 1}, \set{10, 11}$ has means $0.5$ and $10.5$ and $W = 4 \cdot 0.25 = 1$.
Non-example: the partition $\set{0}, \set{1, 10, 11}$ has means $0$ and $22/3$ and $W = 546/9 \approx 60.7$, so it is not a solution.
The mean is used because, for fixed clusters, $m_j$ is the point $c$ that minimises $\sum_{i \in S_j} \abs{x_i - c}^2$.
