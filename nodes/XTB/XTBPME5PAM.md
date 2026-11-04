---
tag: XTBPME5PAM
kind: proof
name: Proof that the chromatic number of a complete bipartite graph is 2
msc: [05C15]
proves: 0FJBBCXYPS
uses: [0V0GC7BQAN, 0C5M7AM6FH, 0Y7VDAX8Q3, 0874138YP6]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_bipartite_graph
---

## Proof

We show that $K_{m,n}$ is $2$-colourable but not $1$-colourable.

1. Let $m, n \ge 1$. Let the [[complete bipartite graph|0V0GC7BQAN]] $K_{m,n}$ have vertex set $A \sqcup B$, where $\abs{A} = m$ and $\abs{B} = n$.
2. Define $c(a) = 1$ for $a \in A$ and $c(b) = 2$ for $b \in B$.
3. Every edge joins a vertex of $A$ to a vertex of $B$, so its ends get the different colours $1$ and $2$. Hence $c$ is a [[colouring|0874138YP6]], and $K_{m,n}$ is [[$2$-colourable|0Y7VDAX8Q3]].
4. Since $m, n \ge 1$, there are vertices $a \in A$ and $b \in B$, and they are adjacent.
5. A colouring with colours in $\set{1}$ would give $a$ and $b$ the same colour $1$. So $K_{m,n}$ is not $1$-colourable.
6. A colouring with colours in the empty set exists only when there are no vertices. Since $K_{m,n}$ has vertices, it is not $0$-colourable.
7. By Steps 3, 5 and 6, the smallest $k$ such that $K_{m,n}$ is $k$-colourable is $2$. So the [[chromatic number|0C5M7AM6FH]] of $K_{m,n}$ is $2$.

## Idea

The two parts give a colouring with two colours, because all edges go between the parts. One colour is not enough, because the graph has an edge, and the two ends of an edge need different colours.
