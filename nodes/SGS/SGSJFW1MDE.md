---
tag: SGSJFW1MDE
kind: proof
name: Proof of Turán's theorem by Zykov symmetrization
msc: [05C35]
proves: 0JG1KZSPFZ
uses: [0JD5C82QMB, 0G52BPNPKG, 0VTCABADBE, 0T0F6CCS9W, 01T3TMGTTE, 0RFWW56Y22]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Turán's_theorem
    locator: Proofs, Zykov Symmetrization and Complete Multipartite Optimization
---

## Proof

We show that a graph with the most edges among those with no large clique is a complete multipartite graph. Then we compare part sizes.

*Setup.*

1. Fix integers $n \ge r \ge 1$ and a set $V$ with $n$ elements. Call a simple [[graph|0JD5C82QMB]] on $V$ *admissible* if it has no [[clique|0G52BPNPKG]] with $r + 1$ vertices. Write $e(H)$ for the number of edges of a graph $H$, and $d_H$ and $N_H$ for [[degree|0T0F6CCS9W]] and [[neighbourhood|01T3TMGTTE]].
2. Let $V = V_1 \sqcup \dots \sqcup V_r$, where some parts may be empty, and let $n_i = \abs{V_i}$. The complete $r$-partite graph on these parts joins two vertices exactly when they lie in different parts.
3. This graph has $\sum_{i < j} n_i n_j$ edges. Since $n^2 = \left(\sum_i n_i\right)^2 = \sum_i n_i^2 + 2 \sum_{i<j} n_i n_j$, it has $\frac{1}{2}\left(n^2 - \sum_i n_i^2\right)$ edges.
4. This graph is admissible. Two vertices in the same part are not adjacent, so a clique has at most one vertex in each part, hence at most $r$ vertices.

*Cloning a vertex.*

5. Let $H$ be a graph on $V$, and let $p \ne q$ be nonadjacent vertices. Let $H'$ be obtained from $H$ by deleting all edges at $q$ and then joining $q$ to every vertex of $N_H(p)$. Note that $q \notin N_H(p)$.
6. Then $e(H') = e(H) - d_H(q) + d_H(p)$, and $q$ is still not adjacent to $p$.
7. If $H$ is admissible, so is $H'$. Let $S$ be a clique of $H'$. If $q \notin S$, then $S$ is a clique of $H$, because only edges at $q$ changed.
8. If $q \in S$, then $p \notin S$. Each vertex of $S \setminus \set{q}$ is adjacent to $q$ in $H'$, hence to $p$ in $H$. So $(S \setminus \set{q}) \cup \set{p}$ is a clique of $H$ of the same size as $S$.
9. In both cases $\abs{S} \le r$ when $H$ is admissible.

*An extremal graph is complete multipartite.*

10. There are finitely many graphs on $V$, and the empty graph is admissible. Let $M$ be the largest value of $e(H)$ over admissible $H$, and let $G^*$ be admissible with $e(G^*) = M$. Write $d = d_{G^*}$.
11. Let $x, y, z$ be pairwise distinct vertices such that $y$ is adjacent to neither $x$ nor $z$. We claim that $x$ is not adjacent to $z$. Suppose instead that $x$ and $z$ are adjacent.
12. If $d(y) < d(x)$, cloning $x$ onto $y$ as in Step 5 gives an admissible graph with $M - d(y) + d(x) > M$ edges. This contradicts the choice of $M$. So $d(y) \ge d(x)$, and in the same way $d(y) \ge d(z)$.
13. Clone $y$ onto $x$: this gives an admissible graph $G_1$ with $M - d(x) + d(y)$ edges. In $G_1$, the vertex $z$ lost its neighbour $x$ and gained nothing, since $z \notin N_{G^*}(y)$. So $d_{G_1}(z) = d(z) - 1$.
14. In $G_1$ the vertex $y$ has the same neighbours as in $G^*$, and $y$, $z$ are still not adjacent. Clone $y$ onto $z$ in $G_1$. This gives an admissible graph $G_2$.
15. By Step 6, $e(G_2) = M - d(x) + d(y) - (d(z) - 1) + d(y) = M + (d(y) - d(x)) + (d(y) - d(z)) + 1$.
16. By Step 12, $e(G_2) \ge M + 1$. This contradicts the choice of $M$, and proves the claim of Step 11.
17. Define $u \equiv v$ if $u = v$ or $u$ is not adjacent to $v$ in $G^*$. This relation is reflexive and symmetric. Let $u \equiv v$ and $v \equiv w$. If two of $u, v, w$ coincide, then $u \equiv w$ at once. Otherwise $u \equiv w$ by Step 11. So $\equiv$ is an equivalence relation.
18. Let $W_1, \dots, W_k$ be its classes. Two distinct vertices in one class are not adjacent. Two vertices in different classes are distinct and not related, so they are adjacent. Thus $G^*$ is the complete multipartite graph with parts $W_1, \dots, W_k$.
19. One vertex from each class gives a clique with $k$ vertices. As $G^*$ is admissible, $k \le r$. Add $r - k$ empty parts. Then $G^*$ is the complete $r$-partite graph of Step 2 for some part sizes $n_1, \dots, n_r$.

*Balancing the parts.*

20. Suppose that $n_i \ge n_j + 2$ for some $i, j$. Move one vertex from part $i$ to part $j$, and take the complete $r$-partite graph on the new parts. It is admissible by Step 4.
21. The sum of squares changes by $(n_i - 1)^2 + (n_j + 1)^2 - n_i^2 - n_j^2 = 2(n_j - n_i) + 2 \le -2$. By Step 3, the number of edges grows by at least $1$. This contradicts the choice of $M$.
22. So the sizes $n_1, \dots, n_r$ of $G^*$ differ pairwise by at most $1$. Let $a$ be the least of them, and let $t$ be the number of parts of size $a + 1$. Then $n = ra + t$ with $0 \le t \le r - 1$.
23. Hence $a = \floor{n/r}$ and $t = n - r\floor{n/r}$. The same holds for the part sizes of the [[Turán graph|0VTCABADBE]] $T(n, r)$, whose $r$ parts also differ in size by at most $1$.
24. So $G^*$ and $T(n, r)$ have the same multiset of part sizes. By Step 3 they have the same number of edges, and $M = e(T(n, r))$.

*Conclusion.*

25. Let $G$ be a simple graph with $n$ vertices and no clique with $r + 1$ vertices. Identify its vertex set with $V$. Then $G$ is admissible, so $e(G) \le M = e(T(n, r))$.
26. Let $m_1, \dots, m_r$ be the part sizes of $T(n, r)$. Apply the [[Cauchy–Schwarz inequality|0RFWW56Y22]] in $\R^r$ to $(m_1, \dots, m_r)$ and $(1, \dots, 1)$. This gives $n^2 = \left(\sum_i m_i\right)^2 \le r \sum_i m_i^2$.
27. By Step 3, $e(T(n, r)) = \frac{1}{2}\left(n^2 - \sum_i m_i^2\right) \le \frac{1}{2}\left(n^2 - \frac{n^2}{r}\right) = \left(1 - \frac{1}{r}\right) \frac{n^2}{2}$.
28. Therefore $G$ has at most $e(T(n, r))$ edges, and at most $\left(1 - \frac{1}{r}\right) \frac{n^2}{2}$ edges.

## Idea

If two nonadjacent vertices have different degrees, replacing the poorer one by a copy of the richer one adds edges and creates no new clique. Pushing this to the extreme shows that a best graph is complete multipartite, with at most $r$ parts. Moving vertices from large parts to small parts adds edges, so the best parts are balanced, which is the Turán graph.
