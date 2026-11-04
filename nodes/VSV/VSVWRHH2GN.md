---
tag: VSVWRHH2GN
kind: proof
name: Proof of the five colour theorem by Kempe chains
msc: [05C15, 05C10]
proves: 06C0JBE52D
uses: [029JQEK15B, 0JD5C82QMB, 0C5M7AM6FH, 0Y7VDAX8Q3, 0874138YP6, 0T0F6CCS9W, 01VVP10MWJ, 0SM1REAVYJ, 0XAP8WHNES, 0V05FC4GKQ, 0JDE56HWQ8, 07CT9RDY7Q, 687RGCHBTP]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Five_color_theorem
    locator: Outline of the proof by contradiction
---

## Proof

We argue by induction on the number $N$ of vertices. We show that every finite [[planar graph|029JQEK15B]] $G$ is [[$5$-colourable|0Y7VDAX8Q3]], which means $\chi(G) \le 5$ by the definition of the [[chromatic number|0C5M7AM6FH]].

*Base case.*

1. If $N \le 5$, give the vertices pairwise distinct colours from $\set{1, \dots, 5}$. This is a [[colouring|0874138YP6]].

*A vertex of small degree.*

2. Let $G$ be a finite planar [[graph|0JD5C82QMB]] with $N \ge 6$ vertices. Graphs are simple here, and every subgraph of $G$ is planar, by erasing part of a drawing of $G$.
3. We claim that $G$ has a vertex of [[degree|0T0F6CCS9W]] at most $5$. Let $H$ be the subgraph induced by a [[connected component|01VVP10MWJ]] of $G$, with $m$ vertices. Each vertex of $H$ has the same degree in $H$ as in $G$.
4. If $m \le 2$, each vertex of $H$ has degree at most $1$.
5. If $m \ge 3$, then $H$ is a connected simple planar graph. By the [[edge bound for planar graphs|0SM1REAVYJ]], $H$ has at most $3m - 6$ edges.
6. By the [[handshaking lemma|0XAP8WHNES]], the degrees in $H$ sum to at most $2(3m - 6) = 6m - 12 < 6m$. So some vertex of $H$ has degree at most $5$. This proves the claim.

*Induction step.*

7. Let $x$ be a vertex of $G$ with degree at most $5$. Let $G' = G - x$ be the graph obtained by deleting $x$ and its edges. It is planar and has $N - 1$ vertices.
8. By the induction hypothesis, $G'$ has a colouring $c$ with colours in $\set{1, \dots, 5}$.
9. If the neighbours of $x$ use at most $4$ colours under $c$, give $x$ a colour that they do not use. This extends $c$ to a colouring of $G$.
10. Otherwise $x$ has exactly $5$ neighbours with $5$ distinct colours. Fix a drawing of $G$ with no crossings. Name the neighbours $y_1, \dots, y_5$ in the cyclic order in which their edges leave $x$. Rename the colours so that $c(y_i) = i$.

*Kempe chains.*

11. For colours $i \ne j$, let $G_{ij}$ be the [[subgraph induced|0V05FC4GKQ]] in $G'$ by the vertices of colour $i$ or $j$.
12. Let $K$ be a connected component of $G_{ij}$. Swapping the colours $i$ and $j$ on the vertices of $K$ gives a new colouring of $G'$. We check each edge $pq$ of $G'$.
13. If $p, q \in K$, they had the two different colours $i$ and $j$, and after the swap they still have different colours. If $p, q \notin K$, nothing changes at $pq$.
14. Let $p \in K$ and $q \notin K$. If $c(q) \in \set{i, j}$, then $q$ is a vertex of $G_{ij}$ adjacent to $p$, so $q \in K$, which is false. So $c(q) \notin \set{i, j}$, while $p$ still has colour $i$ or $j$. The colours differ.

*Case A: $y_1$ and $y_3$ are in different components of $G_{13}$.*

15. Swap the colours $1$ and $3$ on the component $K$ of $G_{13}$ that contains $y_1$. By Step 12, this gives a colouring of $G'$.
16. Now $y_1$ has colour $3$, and $y_3 \notin K$ keeps colour $3$. The vertices $y_2, y_4, y_5$ have colours $2, 4, 5$, so they are not in $G_{13}$ and keep their colours.
17. No neighbour of $x$ has colour $1$ now. Give $x$ colour $1$ to get a colouring of $G$.

*Case B: $y_1$ and $y_3$ are in the same component of $G_{13}$.*

18. Then there is a [[path|0JDE56HWQ8]] $P$ from $y_1$ to $y_3$ in $G_{13}$. All its vertices have colour $1$ or $3$, so $P$ avoids $x$, $y_2$ and $y_4$.
19. Adding $x$ and the edges $x y_1$ and $x y_3$ to $P$ gives a [[cycle|07CT9RDY7Q]] $C$ of $G$. Its drawing is a closed curve without self-intersections, since edges meet only at common ends.
20. By the [[Jordan curve theorem|687RGCHBTP]], the complement of $C$ in the plane has exactly two connected components, the inside and the outside.
21. Near $x$, the curve $C$ consists of the edges $x y_1$ and $x y_3$. The edges $x y_2$ and $x y_4$ leave $x$ into the two different angles between $x y_1$ and $x y_3$, by the cyclic order of Step 10. So they start on different sides of $C$.
22. The edges $x y_2$ and $x y_4$ meet $C$ only at $x$, and $y_2, y_4$ are not on $C$. So $y_2$ and $y_4$ lie in different components of the complement of $C$.
23. Suppose there were a path $Q$ from $y_2$ to $y_4$ in $G_{24}$. Its drawing is a connected curve from one component of the complement of $C$ to the other. So it meets $C$.
24. Edges meet only at common ends, so $Q$ and $C$ share a vertex. But the vertices of $Q$ have colours $2$ or $4$, while those of $C$ are $x$ or have colours $1$ or $3$. This is impossible.
25. Hence $y_2$ and $y_4$ are in different components of $G_{24}$. As in Steps 15 to 17, swap colours $2$ and $4$ on the component that contains $y_2$, and give $x$ colour $2$.

*Conclusion.*

26. In all cases $G$ has a colouring with $5$ colours. By induction, every finite planar graph $G$ satisfies $\chi(G) \le 5$.

## Idea

A planar graph always has a vertex $x$ of degree at most $5$, so colour the rest first. If the five neighbours of $x$ use all five colours, try to recolour a two-coloured "Kempe chain" to free a colour. Planarity prevents the chain from $y_1$ to $y_3$ and the chain from $y_2$ to $y_4$ from both existing, because they would have to cross.
