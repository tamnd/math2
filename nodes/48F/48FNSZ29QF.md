---
tag: 48FNSZ29QF
kind: definition
name: UPGMA
msc: [92B10, 92D15, 62H30]
defines: 9TNRV45K3K
uses: [D9Y3A9RH6J, A6DPR620B5, 0Y0JGC2K9T, RK58WSHJSG]
sources:
  - url: https://en.wikipedia.org/wiki/UPGMA
---

## Definition

Let $X$ be a finite set of taxa and let $d \colon X \times X \to \R_{\ge 0}$ be a symmetric dissimilarity with $d(x, x) = 0$.
*UPGMA* is the following procedure, which outputs a [[rooted tree|0Y0JGC2K9T]] with leaf set $X$ and a height $h(v) \ge 0$ for each vertex $v$.

1. Start with the clusters $\set{x}$ for $x \in X$; each is a leaf of height $0$, and the distance between clusters is $D(\set{x}, \set{y}) = d(x, y)$.
2. While there are at least two clusters, choose two distinct clusters $A$ and $B$ with $D(A, B)$ minimal.
3. Replace $A$ and $B$ by the cluster $A \cup B$, a new vertex of height $D(A, B)/2$ whose children are the vertices of $A$ and $B$.
4. For every other cluster $C$, set
$$D(A \cup B, C) = \frac{\abs{A} \, D(A, C) + \abs{B} \, D(B, C)}{\abs{A} + \abs{B}}.$$

The last vertex created is the root.
The length of the edge from a vertex $u$ to its child $v$ is $h(u) - h(v)$.

## Remarks

The update rule in clause 4 makes $D(A, C)$ equal to the mean of $d(a, c)$ over all $a \in A$ and $c \in C$.
Example: take $X = \set{a, b, c}$ with $d(a, b) = 2$, $d(a, c) = 6$, $d(b, c) = 8$.
The first merge joins $a$ and $b$ at height $1$, and $D(\set{a, b}, \set{c}) = (6 + 8)/2 = 7$.
The second merge creates the root at height $7/2$.
Non-example: replacing the average in clause 4 by $\min(D(A, C), D(B, C))$ gives single-linkage clustering, which is a different method.
If $d$ is an [[ultrametric|A6DPR620B5]], UPGMA returns a tree whose path distances reproduce $d$ exactly.
If the rates of evolution differ between lineages, UPGMA can return the wrong tree; neighbor joining does not need the constant-rate assumption.
