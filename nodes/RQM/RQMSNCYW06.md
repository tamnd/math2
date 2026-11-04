---
tag: RQMSNCYW06
kind: proof
name: Proof that every walk contains a path
msc: [05C38]
proves: 09VZBHB33V
uses: [0VJZM0F9YM, 0JDE56HWQ8, 0KMVFSHFGZ]
sources:
  - url: https://en.wikipedia.org/wiki/Path_(graph_theory)
    locator: Walk, trail, and path
---

## Proof

We argue by [[strong induction|0KMVFSHFGZ]] on the length $k$ of the walk.

1. Claim for each $k \in \N$: let $W$ be a [[walk|0VJZM0F9YM]] of length $k$ from a vertex $u$ to a vertex $v$. Then there is a [[path|0JDE56HWQ8]] from $u$ to $v$ whose vertices and edges all belong to $W$.
2. Let $W = (w_0, w_1, \dots, w_k)$ be a walk from $u$ to $v$, and assume the claim for all lengths smaller than $k$.
3. If the vertices $w_0, \dots, w_k$ are pairwise distinct, then $W$ itself is a path, and we are done.
4. Otherwise there are indices $0 \le i < j \le k$ with $w_i = w_j$.
5. Let $W' = (w_0, \dots, w_i, w_{j+1}, \dots, w_k)$. If $j = k$, this is $W' = (w_0, \dots, w_i)$.
6. $W'$ is a walk: consecutive vertices inside the two blocks are adjacent in $W$, and $w_i = w_j \sim w_{j+1}$ when $j < k$.
7. $W'$ starts at $w_0 = u$. It ends at $w_k = v$ if $j < k$, and at $w_i = w_j = w_k = v$ if $j = k$.
8. The vertices of $W'$ are vertices of $W$. Its edges are edges of $W$, because the only new edge $w_i w_{j+1}$ equals the edge $w_j w_{j+1}$ of $W$.
9. The length of $W'$ is $k - (j - i) < k$. By the induction hypothesis, $W'$ contains a path from $u$ to $v$ as in the claim.
10. By step 8, the vertices and edges of that path are vertices and edges of $W$. This proves the claim for $k$, and hence the statement.

## Idea

If a walk visits some vertex twice, the part between the two visits is a detour. Cutting it out gives a shorter walk with the same ends, and this cannot go on forever.
