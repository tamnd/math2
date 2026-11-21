---
tag: 6BFRDVHC63
kind: example
name: Vertex colorings of finite ordered graphs
aliases: [vertex-ramsey-ordered-graphs]
msc: ["05C55", "05D10"]
topics: [ZS8X8KS54R]
audience: research
instance_of: [8XS8FCTF8T]
uses: [8XS8FCTF8T, 00C0BR7D7H, 0EREPBVG2G, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_Ramsey_theory
    locator: Examples
---

## Example

Let $\mathcal{O}$ be the class of finite ordered [[graphs|00C0BR7D7H]]: graphs with a linear order on the vertices.
Nešetřil and Rödl proved that $\mathcal{O}$ is a [[Ramsey class|8XS8FCTF8T]].
We prove the case where $A$ is the one-vertex ordered graph.

1. For ordered graphs $B, D$, let $B[D]$ have vertex set $B \times D$, ordered lexicographically.
2. Join $(x, y)$ and $(x', y')$ when $x \sim x'$ in $B$, or when $x = x'$ and $y \sim y'$ in $D$.
3. Let $B^{1} = B$ and $B^{k} = B[B^{k-1}]$. We show $B^k \to (B)^A_k$ by [[induction|0ASJVEFA9J]] on $k$.
4. For $k = 1$ there is one color, and $B$ itself is monochromatic.
5. Let $B^k$ be colored with $k$ colors. Suppose every fiber $\set{x} \times B^{k-1}$ contains a vertex of color $1$.
6. Pick one such vertex in each fiber. By step 2, these vertices induce a copy of $B$, in the right order, all of color $1$.
7. Otherwise some fiber avoids color $1$. It is an [[induced|0EREPBVG2G]] copy of $B^{k-1}$ colored with $k - 1$ colors.
8. By induction it contains a monochromatic copy of $B$.

## Remarks

Embeddings of a one-vertex ordered graph are just vertices, so this is the vertex-partition case of the Ramsey property.
The general case, for an arbitrary ordered graph $A$, needs the partite construction of Nešetřil and Rödl.
Abramson and Harrington proved it independently for ordered relational structures.

## Explanations

### L1 human

Replace each vertex of a graph by a copy of the graph, and repeat.
If each copy contains a red vertex, the red vertices chosen one per copy form a copy of the original graph.
If some copy has no red vertex, it uses fewer colors, and we repeat the argument inside it.

### L2 human

We take $B$ to be the ordered edge $0 < 1$ with $0 \sim 1$, and $k = 2$.

1. $B^2$ has vertices $(0, 0) < (0, 1) < (1, 0) < (1, 1)$, and it is the complete graph $K_4$.
2. Color the $4$ vertices red and blue in any way.
3. If both fibers have a red vertex, they give a red edge. Otherwise a fiber is all blue, and it is a blue edge.

The typical use is as the easiest instance of the Nešetřil-Rödl theorem.
A trap is to think the general case is as easy; colorings of edges need a much larger construction.
