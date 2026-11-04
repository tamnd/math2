---
tag: 92NKFM9W1C
kind: proof
name: Proof that K5 and K3,3 are not planar
msc: [05C10]
proves: 030A3FHN14
uses: [03WKB2H474, 0V0GC7BQAN, 029JQEK15B, 0FFAYNMAJZ, 05RN90E14Y, 0SM1REAVYJ, 0W1C598HMS, 07DVHJ8N0A, 0VJZM0F9YM]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Planar_graph
    locator: Euler's formula
  - url: https://en.wikipedia.org/wiki/Three_utilities_problem
    locator: Unsolvability
---

## Proof

We use the edge bound for $K_5$, and Euler's formula with a face count for $K_{3,3}$.

*The graph $K_5$.*

1. The [[complete graph|03WKB2H474]] $K_5$ is simple, and it is [[connected|0FFAYNMAJZ]] because any two distinct vertices are adjacent.
2. It has $v = 5$ vertices and, by the [[number of edges of a complete graph|05RN90E14Y]], $e = \binom{5}{2} = 10$ edges.
3. Suppose that $K_5$ is [[planar|029JQEK15B]]. Since $v = 5 \ge 3$, the [[edge bound for planar graphs|0SM1REAVYJ]] gives $e \le 3 \cdot 5 - 6 = 9$.
4. This contradicts $e = 10$. So $K_5$ is not planar.

*The graph $K_{3,3}$.*

5. Let the [[complete bipartite graph|0V0GC7BQAN]] $K_{3,3}$ have parts $A$ and $B$ with $\abs{A} = \abs{B} = 3$. It has $v = 6$ vertices and $e = 3 \cdot 3 = 9$ edges, one for each pair in $A \times B$.
6. It is connected. Two vertices in different parts are adjacent. Two vertices in the same part have a common neighbour in the other part.
7. Suppose that $K_{3,3}$ is planar, and fix a drawing with no crossings. Let $f$ be its number of faces.
8. By [[Euler's formula|0W1C598HMS]], $f = 2 - v + e = 2 - 6 + 9 = 5$.
9. For a face $F$, let $\ell(F)$ be the number of edge sides that border $F$, where an edge with $F$ on both sides counts twice. Each edge has two sides, and each side borders exactly one face. So $\sum_F \ell(F) = 2e = 18$.
10. The boundary of each face $F$ is traced by a closed [[walk|0VJZM0F9YM]] of length $\ell(F)$, since the graph is connected and has an edge.
11. The graph $K_{3,3}$ is [[bipartite|07DVHJ8N0A]]. Each step of a walk moves between $A$ and $B$, so a closed walk takes an even number of steps. Thus each $\ell(F)$ is even.
12. Each face borders some edge side, as the graph is connected with an edge, so $\ell(F) \ge 1$. A simple graph has no two edges with the same ends. So a boundary walk of length $2$ goes along one edge $xy$ and straight back. This happens only when $x$ and $y$ both have degree $1$. In $K_{3,3}$ every vertex has degree $3$, so this does not happen.
13. By Steps 11 and 12, $\ell(F) \ge 4$ for every face $F$. Hence $4f \le 18$ by Step 9.
14. By Step 8, $4f = 20 > 18$. This contradiction shows that $K_{3,3}$ is not planar.

## Idea

Euler's formula fixes the number of faces of any drawing, and each face needs enough edges around it. For $K_5$ there are too many edges for the bound $3v - 6$. For $K_{3,3}$ every face needs at least four edge sides, because the graph has no triangles, and $5$ faces would need $20$ sides while only $18$ exist.
