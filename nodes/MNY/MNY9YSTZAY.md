---
tag: MNY9YSTZAY
kind: definition
name: Cluster analysis
msc: [62H30]
defines: D9Y3A9RH6J
uses: [08QMKTWF9T, 0VR671PHE5]
sources:
  - url: https://en.wikipedia.org/wiki/Cluster_analysis
---

## Definition

Let $x_1, \ldots, x_n$ be data points and let $d(x_i, x_j) \ge 0$ be a dissimilarity with $d(x_i, x_i) = 0$ and $d(x_i, x_j) = d(x_j, x_i)$.
A (hard) *clustering* of the data into $K$ clusters is a [[partition|08QMKTWF9T]] of $\set{1, \ldots, n}$ into $K$ non-empty sets $C_1, \ldots, C_K$.
*Cluster analysis* is the task of choosing a clustering in which dissimilarities within clusters are small and dissimilarities between clusters are large.
A method of cluster analysis makes this precise.
It may minimise an objective function over all clusterings, or follow a rule that merges or splits clusters.
A *hierarchical clustering* is a nested sequence of clusterings, from $n$ singletons to one cluster.

## Remarks

Example: the points $0, 1, 10, 11$ on the real line with $d(x, y) = \abs{x - y}$ have the natural clustering $\set{0, 1}$, $\set{10, 11}$: within-cluster distances are $1$ and between-cluster distances are at least $9$.
Non-example: the sets $\set{0, 1}$ and $\set{1, 10, 11}$ are not a clustering, because the point $1$ lies in two sets, so they do not form a partition.
Soft or fuzzy clusterings relax the partition to membership weights in $[0, 1]$ that add up to $1$ for each point.
Single linkage merges at each step the two clusters with the smallest minimum distance; complete linkage uses the maximum distance instead.
