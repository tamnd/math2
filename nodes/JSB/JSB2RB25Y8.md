---
tag: JSB2RB25Y8
kind: proof
name: Proof of Euler's theorem on Eulerian circuits by a longest trail
msc: [05C45]
proves: 020422MDQF
uses: [01M5T0KDG7, 0JD5C82QMB, 0NNYDD1AVR, 062MQGP8M5, 0VJZM0F9YM, 0T0F6CCS9W, 0FFAYNMAJZ]
sources:
  - url: https://arxiv.org/pdf/2308.04512
---

## Proof

A [[graph|0JD5C82QMB]] is a special [[multigraph|01M5T0KDG7]], so we work with a multigraph $G = (V, E, r)$, where $V$ and $E$ are finite. We show necessity by counting, and sufficiency with a longest trail.

1. Conventions. A [[walk|0VJZM0F9YM]] is a sequence $(w_0, e_1, w_1, \dots, e_k, w_k)$ of vertices $w_t$ and edges $e_t$. We require $r(e_t) = \set{w_{t-1}, w_t}$ for each $t$. It is a [[trail|062MQGP8M5]] if $e_1, \dots, e_k$ are pairwise distinct.
2. In a graph an edge is determined by its ends, so these are the usual walks and trails. $G$ is [[connected|0FFAYNMAJZ]] if $V \ne \varnothing$ and any two vertices are joined by a walk.
3. Let $x$ be a vertex and $e$ an edge. Let $m_x(e) = 2$ if $e$ is a loop at $x$, and $m_x(e) = 1$ if $e$ is not a loop and $x \in r(e)$. Otherwise $m_x(e) = 0$. The [[degree|0T0F6CCS9W]] is $\deg(x) = \sum_{e \in E} m_x(e)$.
4. For a condition $\varphi$, let $[\varphi]$ be $1$ if $\varphi$ holds and $0$ otherwise. For each $t$, $m_x(e_t) = [w_{t-1} = x] + [w_t = x]$. Both cases of a loop and a non-loop agree with step 3.
5. Let $W$ be a trail as in step 1, and let $c_W(x) = \sum_{t=1}^{k} m_x(e_t)$. By step 4, $c_W(x) = 2 \sum_{t=1}^{k-1} [w_t = x] + [w_0 = x] + [w_k = x]$ if $k \ge 1$.
6. Hence $c_W(x) \equiv [w_0 = x] + [w_k = x] \pmod 2$. This also holds for $k = 0$, where both sides are even.
7. Necessity. Let $W$ be an [[Eulerian circuit|0NNYDD1AVR]]. Each edge of $G$ is exactly one $e_t$, so $c_W(x) = \deg(x)$ for every $x$.
8. Since $w_0 = w_k$, step 6 gives $\deg(x) \equiv 2[w_0 = x] \equiv 0 \pmod 2$. So every vertex has even degree.
9. Sufficiency. Assume every vertex has even degree. A trail has length at most $\abs{E}$, so there is a trail $W = (w_0, e_1, \dots, e_k, w_k)$ of largest length.
10. $G$ has an edge $e$, with $r(e) = \set{a, b}$ or $\set{a}$. Then $(a, e, b)$ or $(a, e, a)$ is a trail of length $1$. So $k \ge 1$.
11. $W$ is closed. Suppose $w_0 \ne w_k$, and let $x = w_k$. By step 6, $c_W(x)$ is odd, while $\deg(x)$ is even.
12. So $c_W(x) \ne \deg(x)$. Since $c_W(x)$ sums $m_x$ over the edges of $W$, some edge $f$ not in $W$ has $m_x(f) > 0$, so $x \in r(f)$.
13. Let $y$ be the other end of $f$, or $y = x$ if $f$ is a loop. Then $(w_0, e_1, \dots, e_k, w_k, f, y)$ is a trail of length $k + 1$. This contradicts step 9, so $w_0 = w_k$.
14. Let $S = \set{w_0, \dots, w_k}$, and suppose some edge of $G$ is not in $W$. We claim that some edge not in $W$ has an end in $S$.
15. Suppose not, and take an edge $g$ not in $W$ with an end $z$. Then $z \notin S$.
16. Since $G$ is connected, there is a walk from $w_0 \in S$ to $z \notin S$. Some edge $h$ of this walk has an end in $S$ and an end outside $S$.
17. By the assumption in step 15, $h$ lies in $W$. But every edge of $W$ has both ends in $S$, a contradiction.
18. So there is an edge $g$ not in $W$ with an end $w_s \in S$, where $0 \le s \le k$. Since $w_k = w_0$, we may take $s \le k - 1$.
19. Then $(w_s, e_{s+1}, \dots, e_k, w_k, e_1, w_1, \dots, e_s, w_s)$ is a trail. It uses the same $k$ edges as $W$, because $w_k = w_0$. For $s = 0$ it is $W$ itself.
20. Appending $g$ and its other end to this trail, as in step 13, gives a trail of length $k + 1$. This contradicts step 9.
21. So the assumption of step 14 fails, and every edge of $G$ lies in $W$. Since $W$ is a trail, each edge appears exactly once, and $w_0 = w_k$ by step 13.
22. So $W$ is an Eulerian circuit of $G$.

## Idea

A trail passes through a vertex by using two of its edges, so only its ends can have an unpaired edge. For necessity this shows all degrees are even.
For sufficiency take a longest trail. Even degrees leave a free edge at an open end, so the trail is closed. Connectedness gives a free edge at some vertex of the closed trail, and starting the trail there would make it longer.
