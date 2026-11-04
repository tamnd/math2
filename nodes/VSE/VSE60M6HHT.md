---
tag: VSE60M6HHT
kind: proof
name: Proof that a tree on n vertices has n − 1 edges, by removing a leaf
msc: [05C05]
proves: 0VSNHTHK8T
uses: [0MJ0JS72DZ, 0FFAYNMAJZ, 0XNN9Z8E5A, 0WNGQBPPQX, 0H8Q4MANBD, 09VZBHB33V, 0JDE56HWQ8, 0P11X5HKAX]
sources:
  - url: https://github.com/oscarlevin/discrete-book/blob/a8e4949bc45daf100930c1182983778f56ab689f/ptx/sec_gt-trees.ptx#L245
---

## Proof

We argue by induction on $n$.

1. A [[tree|0MJ0JS72DZ]] is [[connected|0FFAYNMAJZ]], so it has at least one vertex. Thus $n \ge 1$.
2. Base case $n = 1$. An edge is a $2$-element set of vertices, and a $1$-element vertex set has no such subset. So $T$ has $0 = n - 1$ [[edges|0WNGQBPPQX]].
3. Induction step. Let $n \ge 2$, and assume that every tree with $n - 1$ vertices has $n - 2$ edges. Let $T$ have $n$ vertices.
4. By the [[leaf lemma|0H8Q4MANBD]], $T$ has a vertex $\ell$ of degree $1$. Let $\ell a$ be its only edge.
5. Let $T'$ be the graph $T$ with the vertex $\ell$ and the edge $\ell a$ removed. It has $n - 1$ vertices and one edge fewer than $T$.
6. $T'$ is acyclic: it is a [[subgraph|0P11X5HKAX]] of $T$, so each cycle of $T'$ is a cycle of $T$, and $T$ is [[acyclic|0XNN9Z8E5A]].
7. $T'$ has a vertex, namely $a$. Let $x, y$ be vertices of $T'$.
8. Since $T$ is connected, it has a walk from $x$ to $y$. By [[every walk contains a path|09VZBHB33V]], $T$ has a [[path|0JDE56HWQ8]] $(p_0, \dots, p_m)$ from $x$ to $y$.
9. The vertex $\ell$ is not $p_0 = x$ or $p_m = y$. If $\ell = p_i$ with $0 < i < m$, then $p_{i-1}$ and $p_{i+1}$ are two distinct neighbours of $\ell$, which contradicts $\deg(\ell) = 1$.
10. So the path avoids $\ell$, and hence also the edge $\ell a$. It is a walk in $T'$ from $x$ to $y$. Thus $T'$ is connected.
11. By steps 6 and 10, $T'$ is a tree with $n - 1$ vertices. By the induction hypothesis it has $n - 2$ edges.
12. By step 5, $T$ has $(n - 2) + 1 = n - 1$ edges. This completes the induction.

## Idea

Removing a leaf removes exactly one vertex and one edge, and what is left is still a tree. Repeating this shrinks the tree down to a single vertex with no edges.
