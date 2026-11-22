---
tag: RJB83Z4N9B
kind: example
name: A tree with n vertices has n - 1 edges, by induction on n
msc: ["05C05"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [B2D8PTFNN1]
uses: [B2D8PTFNN1, 0MJ0JS72DZ, EA8S0JHXMP, 0JDE56HWQ8, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Tree_(graph_theory)
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Tree_(graph_theory)
    locator: Definitions
---

## Example

We prove that every [[tree|0MJ0JS72DZ]] with $n \ge 1$ vertices has exactly $n - 1$ edges.
A tree is a finite [[graph|0JD5C82QMB]] that is [[connected|0FFAYNMAJZ]] and [[acyclic|0XNN9Z8E5A]].
The proof is an [[induction on size|B2D8PTFNN1]], with the number of vertices as the size.
The reduction deletes a leaf, so we first prove that a leaf exists.

**Lemma.** Every tree $T$ with at least $2$ vertices has a [[leaf|EA8S0JHXMP]], that is, a vertex of [[degree|0KS0KRDV4Y]] $1$.

1. The tree $T$ is connected and has two vertices, so there is a [[path|0JDE56HWQ8]] between them, and $T$ has at least one edge.
2. The graph $T$ is finite, so it has finitely many paths.
   Let $v_0 v_1 \cdots v_k$ be a path with the largest number of edges.
   By step 1, $k \ge 1$.
3. The vertex $v_0$ is adjacent to $v_1$.
   Suppose that $v_0$ has another neighbor $w \neq v_1$.
4. If $w = v_i$ for some $i \ge 2$, then $v_0 v_1 \cdots v_i v_0$ is a cycle.
   This contradicts the hypothesis that $T$ is acyclic.
5. If $w$ is not on the path, then $w v_0 v_1 \cdots v_k$ is a path with $k + 1$ edges.
   This contradicts the choice of the path in step 2.
6. So $v_1$ is the only neighbor of $v_0$, and $v_0$ is a leaf.

**Induction.** Let $P(n)$ be the statement "every tree with $n$ vertices has $n - 1$ edges".

1. Base case $n = 1$: each edge joins two distinct vertices, so a graph with one vertex has $0 = 1 - 1$ edges.
2. Induction step: let $n \ge 1$, assume $P(n)$, and let $T$ be an arbitrary tree with $n + 1$ vertices.
3. Since $n + 1 \ge 2$, the lemma gives a leaf $v$ of $T$.
   Let $e$ be the one edge at $v$.
4. Let $T'$ be the graph that we get from $T$ when we delete $v$ and $e$.
   It has $n$ vertices and one edge fewer than $T$.
5. The graph $T'$ is acyclic, because each cycle of $T'$ would be a cycle of $T$.
6. The graph $T'$ is connected.
   Let $x$ and $y$ be vertices of $T'$, and take a path from $x$ to $y$ in $T$.
   Each inner vertex of a path has two neighbors on the path, and $v$ has only one neighbor, so $v$ is not on this path, and the path lies in $T'$.
7. By steps 5 and 6, $T'$ is a tree with $n$ vertices, so it has $n - 1$ edges by $P(n)$.
8. So $T$ has $(n - 1) + 1 = (n + 1) - 1$ edges, and $P(n + 1)$ holds.
9. By induction, $P(n)$ holds for every $n \ge 1$.

## Remarks

The example shows the two parts of every induction on size.
A lemma proves that a reduction exists, here a leaf.
Then a check proves that the reduced object still satisfies the hypotheses of the claim, here steps 5 and 6.

The step starts from an arbitrary tree with $n + 1$ vertices and deletes a leaf.
It does not start from a tree with $n$ vertices and add a leaf, since that order would need a separate proof that every tree arises in this way.
Deleting an arbitrary vertex does not work either.
In the path with $3$ vertices, deleting the middle vertex leaves two separate vertices, which do not form a tree.

The lemma gives more than it states.
The same argument at the other end of the longest path shows that $v_k$ is a leaf too, so every tree with at least $2$ vertices has at least $2$ leaves.
The claim fails for graphs that are not trees.
A cycle with $n \ge 3$ vertices has $n$ edges, and two separate edges form an acyclic graph with $4$ vertices and only $2$ edges.

## Explanations

### L1 human

A tree is a network of points and lines with no loops, in which every point can be reached from every other point.
A tree with $2$ points has $1$ line, and a tree with $3$ points has $2$ lines.
In general there is always one line fewer than points.
To see this, find a point at the end of a branch, a leaf, and cut it off with its line.
What remains is a smaller tree, with one point fewer and one line fewer.
Repeat until one point and no line remain.

### L2 human

We follow the proof on the tree $T$ with vertices $1, 2, 3, 4, 5$ and edges $12$, $23$, $24$, $45$.
A longest path is $1\,2\,4\,5$, with $3$ edges, and its end vertex $1$ is a leaf.
Deleting vertex $1$ and edge $12$ leaves the vertices $2, 3, 4, 5$ and the edges $23$, $24$, $45$, which form a tree again.
In that tree a longest path is $3\,2\,4\,5$, and deleting the leaf $3$ leaves the vertices $2, 4, 5$ and the edges $24$, $45$.
Deleting the leaf $2$ and then the leaf $4$ leaves the vertex $5$ alone.

Check: we deleted $4$ edges in $4$ steps and reached $1$ vertex with $0$ edges, so $T$ has $4 = 5 - 1$ edges.
The typical use of the result is a test for trees: a connected graph with $n$ vertices is a tree exactly when it has $n - 1$ edges.
Watch out: the hypothesis does not apply to $T$ minus an arbitrary vertex, because the result may be disconnected and then it is not a tree.
