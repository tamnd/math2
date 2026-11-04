---
tag: K90CGWAE6S
kind: proof
name: Proof of the edge bound for planar graphs
msc: [05C10]
proves: 0SM1REAVYJ
uses: [029JQEK15B, 0FFAYNMAJZ, 0JD5C82QMB, 0W1C598HMS, 0VJZM0F9YM, 0F8YBHF2W3]
sources:
  - url: https://en.wikipedia.org/wiki/Planar_graph
    locator: Euler's formula
---

## Proof

We count the pairs of a face and an edge side on its boundary, and then apply Euler's formula.

1. Let $G$ be a finite simple [[connected|0FFAYNMAJZ]] [[planar graph|029JQEK15B]] with $v \ge 3$ vertices and $e$ edges. Fix a drawing of $G$ in the plane with no crossings, and let $f$ be its number of faces.
2. The graph $G$ has at least two edges. Indeed, $G$ is connected with at least two vertices, so each vertex lies on an edge. One edge covers only two of the $v \ge 3$ vertices.
3. Each edge of the drawing has two sides, and each side borders exactly one face. For a face $F$, let $\ell(F)$ be the number of edge sides that border $F$. An edge with $F$ on both sides counts twice.
4. Every edge side borders exactly one face, so $\sum_F \ell(F) = 2e$, where the sum runs over all $f$ faces. This is a [[double count|0F8YBHF2W3]] of the edge sides.
5. Since $G$ is connected and has an edge, the boundary of each face $F$ is traced by a closed [[walk|0VJZM0F9YM]] of length $\ell(F)$ in $G$.
6. We claim that $\ell(F) \ge 3$ for each face $F$. Since $G$ is connected and has an edge, every face borders some edge side, so $\ell(F) \ge 1$. A closed walk of length $1$ would use a loop, and a simple [[graph|0JD5C82QMB]] has no loops.
7. A simple graph has no two edges with the same ends. So a boundary walk of length $2$ goes along one edge $xy$ and straight back. Then $F$ lies on both sides of $xy$ and touches no other edge. At $x$ and $y$ the walk turns around, which happens only at vertices of degree $1$. Then $G$, being connected, would be the single edge $xy$, contrary to Step 2. This proves the claim.
8. By Steps 4 and 6, $3f \le \sum_F \ell(F) = 2e$.
9. By [[Euler's formula|0W1C598HMS]], $v - e + f = 2$, so $f = 2 - v + e$.
10. Substituting into Step 8 gives $3(2 - v + e) \le 2e$, that is, $6 - 3v + 3e \le 2e$.
11. Hence $e \le 3v - 6$.

## Idea

Each face is surrounded by at least three edge sides, and each edge has exactly two sides. So there are at most $2e/3$ faces. Euler's formula ties the number of faces to $v$ and $e$, and this turns the bound on faces into a bound on edges.
