---
tag: NQNPP83YQN
kind: proof
name: Proof of Tutte's theorem via an edge-maximal counterexample
msc: [05C70]
proves: 08J7R35B6Q
uses: [0JD5C82QMB, 01VVP10MWJ, 05ZPH8KF9K, 0Z87BHAFTB, 0JDE56HWQ8, 0Z49NTR1DZ, 07CT9RDY7Q, 0P11X5HKAX]
methods: [0J0XBKG64S, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Tutte's_theorem_on_perfect_matchings
    locator: Proof
---

## Proof

For a [[graph|0JD5C82QMB]] $H$ on $V$ and $U \subseteq V$, write $o(H - U)$ for the number of odd [[connected components|01VVP10MWJ]] of $H - U$. Say that $H$ satisfies *Tutte's condition* if $o(H - U) \le \abs{U}$ for all $U \subseteq V$. Let $G$ be a finite graph with vertex set $V$.

*The condition is necessary.*

1. Let $M$ be a [[perfect matching|05ZPH8KF9K]] of $G$, and let $U \subseteq V$. Let $K$ be an odd component of $G - U$.
2. The edges of $M$ inside $K$ cover an even number of vertices of $K$. As $\abs{K}$ is odd, some vertex $x_K \in K$ is matched to a vertex $y_K \notin K$.
3. There are no edges between different components of $G - U$, so $y_K \in U$.
4. Distinct odd components give distinct vertices $x_K$. Since $M$ is a [[matching|0Z87BHAFTB]], they also give distinct $y_K$. So $K \mapsto y_K$ is injective, and $o(G - U) \le \abs{U}$.

*The condition is sufficient: setup.*

5. Suppose that $G$ satisfies Tutte's condition but has no perfect matching. We derive a contradiction.
6. For $U = \varnothing$, the condition gives $o(G) = 0$. So every component of $G$ is even, and $\abs{V}$ is even.
7. Among all graphs on $V$ that contain every edge of $G$ and have no perfect matching, choose one, $G^*$, with the most edges. Then $G^* + uv$ has a perfect matching for any two nonadjacent vertices $u \ne v$ of $G^*$.
8. The graph $G^*$ satisfies Tutte's condition. Let $U \subseteq V$. Each component of $G^* - U$ is a union of components of $G - U$, since $G$ is a [[subgraph|0P11X5HKAX]] of $G^*$.
9. A union of even sets is even, so each odd component of $G^* - U$ contains an odd component of $G - U$. These are distinct for distinct components. So $o(G^* - U) \le o(G - U) \le \abs{U}$.
10. Let $S$ be the set of vertices of $G^*$ adjacent to all other vertices.

*Case 1: every component of $G^* - S$ is a complete graph.*

11. Let $K_1, \dots, K_k$ be the odd components of $G^* - S$. By Step 8, $k \le \abs{S}$. Choose distinct $s_1, \dots, s_k \in S$ and vertices $x_i \in K_i$.
12. Match $x_i$ with $s_i$; this is an edge, since $s_i \in S$. The set $K_i \setminus \set{x_i}$ is even and complete, so pair up its vertices by edges.
13. Pair up the vertices of each even component in the same way.
14. Let $S' = S \setminus \set{s_1, \dots, s_k}$. Modulo $2$, $\abs{V} = \abs{S} + \sum_{\text{components}} \abs{K} \equiv \abs{S} + k$. As $\abs{V}$ is even, $\abs{S'} = \abs{S} - k$ is even.
15. Any two vertices of $S$ are adjacent, so pair up the vertices of $S'$ by edges.
16. Steps 12 to 15 give a perfect matching of $G^*$. This contradicts Step 7.

*Case 2: some component $K$ of $G^* - S$ is not complete.*

17. Choose nonadjacent vertices of $K$ and a shortest [[path|0JDE56HWQ8]] in $K$ between them. Let $a, b, c$ be its first three vertices. Then $ab$ and $bc$ are edges and $a, c$ are not adjacent, by minimality of the path.
18. Since $b \in K$, $b \notin S$. So there is a vertex $d \ne b$ not adjacent to $b$. Then $d \ne a, c$.
19. By Step 7, $G^* + ac$ has a perfect matching $M_1$, and $G^* + bd$ has a perfect matching $M_2$. Then $ac \in M_1$ and $bd \in M_2$, since $G^*$ has no perfect matching.
20. Also $bd \notin M_1$ and $ac \notin M_2$, since these are not edges of $G^* + ac$ and $G^* + bd$ respectively.
21. Let $D = M_1 \mathbin{\triangle} M_2$ be the [[symmetric difference|0Z49NTR1DZ]]. Each vertex lies on one edge of $M_1$ and one of $M_2$. So it lies on $0$ or $2$ edges of $D$, one from each matching.
22. Hence $D$ is a disjoint union of [[cycles|07CT9RDY7Q]] whose edges alternate between $M_1$ and $M_2$. By Step 20, $bd \in D$. Let $C$ be the cycle of $D$ through $bd$.
23. At each vertex of $C$, both its $M_1$-edge and its $M_2$-edge lie on $C$. So edges of $M_1$ or $M_2$ not on $C$ have no end on $C$.
24. *Case 2a: $ac \notin C$.* Let $M = (M_2 \setminus C) \cup (M_1 \cap C)$. The edges $M_1 \cap C$ cover each vertex of $C$ once, and $M_2 \setminus C$ covers each other vertex once, by Step 23.
25. So $M$ is a perfect matching. It avoids $bd$, which is on $C$ and not in $M_1$, and it avoids $ac$, which is not on $C$ and not in $M_2$. So $M$ is a perfect matching of $G^*$, a contradiction.
26. *Case 2b: $ac \in C$.* Walk along $C$ from $b$ through $d$, and stop at the first vertex $u \in \set{a, c}$. This exists, since $a, c$ lie on $C$ and $b, d \notin \set{a, c}$. Let $P$ be the part of $C$ from $d$ to $u$.
27. The path $P$ does not contain $ac$, since we stop on first reaching an end of $ac$. So $P$ reaches $u$ along the other $C$-edge at $u$, which is the $M_2$-edge of $u$.
28. The first edge of $P$ is the $M_1$-edge of $d$, as the $M_2$-edge of $d$ is $bd$. So the edges of $P$ alternate, starting in $M_1$ and ending in $M_2$.
29. The edge $ub$ is an edge of $G^*$ by Step 17. Let $C'$ be the cycle formed by $bd$, $P$ and $ub$. Its edges in order are $bd \in M_2$, then $P$ alternating from $M_1$ to $M_2$, then $ub$.
30. Let $N$ consist of $ub$ and the $M_1$-edges of $P$. These are every second edge of $C'$, so $N$ covers each vertex of $C'$ exactly once. No edge of $N$ is $ac$ or $bd$.
31. Each vertex of $C'$ has its $M_2$-edge on $C'$: for $b$ this is $bd$, and for the other vertices it lies on $P$. So the edges of $M_2$ not on $C'$ have no end on $C'$.
32. Let $M = (M_2 \setminus C') \cup N$. By Steps 30 and 31, $M$ is a perfect matching of $G^*$, since it avoids $bd$. This contradicts Step 7.
33. All cases lead to a contradiction. So $G$ has a perfect matching whenever it satisfies Tutte's condition.

## Idea

A perfect matching must send one vertex of each odd piece of $G - U$ into $U$, which gives necessity. For sufficiency, add edges until any further edge would create a perfect matching. If the graph splits around its universal vertices into complete pieces, a matching is easy to build. Otherwise two matchings of slightly larger graphs combine along an alternating cycle into a matching of the graph itself.
