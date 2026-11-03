---
tag: HABSACSXKD
kind: definition
name: Blossom algorithm
msc: [05C70, 05C85, 90C27]
defines: JYBHEDWB6X
uses: [0MJ04A50QW, 00C0BR7D7H, 03NAMV1DHJ, 0Z05VCBQ7Y, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Blossom_algorithm
---

## Definition

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]], and let $M$ be a [[matching|0MJ04A50QW]] in $G$.
A vertex is *exposed* if no edge of $M$ contains it.
An *$M$-alternating* [[path|03NAMV1DHJ]] is a path whose edges lie alternately outside $M$ and in $M$.
An *$M$-augmenting path* is an $M$-alternating path whose two end vertices are distinct and exposed.
An *$M$-blossom* is a [[cycle|0Z05VCBQ7Y]] $B$ of odd length $2k + 1$ in $G$ that contains exactly $k$ edges of $M$.
Contracting $B$ gives the graph $G/B$, in which the vertices of $B$ are replaced by one new vertex $b$.
It also gives the matching $M/B$ of $G/B$, formed by the edges of $M$ outside $B$.

The *blossom algorithm* is the following [[algorithm|9DMSG5HAQX]].

1. Start with any matching $M$, for example $M = \emptyset$.
2. Grow alternating trees rooted at the exposed vertices; a vertex at even distance from its root is *outer*.
3. If an edge joins outer vertices of two different trees, the two tree paths and this edge form an $M$-augmenting path $P$. Replace $M$ by the symmetric difference of $M$ and the edge set of $P$, and go back to step 2.
4. If an edge joins two outer vertices of the same tree, it closes an $M$-blossom $B$. Continue the search in $G/B$ with $M/B$, and lift any augmenting path found there to an $M$-augmenting path in $G$.
5. If no edge of these two kinds remains, return $M$.

## Remarks

The returned matching is maximum because of Berge's lemma: $M$ is maximum if and only if there is no $M$-augmenting path.
The key fact is that, for a blossom $B$ found in the search, $G$ has an $M$-augmenting path if and only if $G/B$ has an $M/B$-augmenting path.
There are at most $\abs{V}/2$ augmentations, and each search is polynomial, so the algorithm runs in polynomial time; a direct implementation takes $O(\abs{V}^2 \abs{E})$ steps.

Example: let $G$ be the triangle on $a, b, c$ with an extra edge $c d$, and let $M = \set{\set{a, b}}$.
The vertices $c$ and $d$ are exposed, and the path $d, c$ of one edge is augmenting.
The new matching $\set{\set{a, b}, \set{c, d}}$ is perfect, hence maximum.

Non-example: the augmenting path search for bipartite graphs grows alternating trees but never contracts odd cycles.
On a graph with odd cycles it may miss an augmenting path that exists, so it can stop before the matching is maximum.
