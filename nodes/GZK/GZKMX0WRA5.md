---
tag: GZKMX0WRA5
kind: definition
name: Cheeger constant
msc: [05C50, 05C40, 05C48]
defines: Y7S6W12N64
uses: [0JD5C82QMB, 0FFAYNMAJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Cheeger_constant_(graph_theory)
---

## Definition

Let $G = (V, E)$ be a finite [[graph|0JD5C82QMB]] with $\abs{V} \ge 2$.
For $S \subseteq V$, let $\partial S$ be the set of edges with one end in $S$ and the other end in $V \setminus S$.
The Cheeger constant of $G$ is
$$h(G) = \min \set{ \frac{\abs{\partial S}}{\abs{S}} : S \subseteq V, \ 1 \le \abs{S} \le \frac{\abs{V}}{2} }.$$

## Remarks

Example: in the complete graph $K_n$ with $n \ge 2$, a set $S$ of size $k$ has $k(n - k)$ edges leaving it, so the ratio is $n - k$.
The minimum over $1 \le k \le n/2$ gives $h(K_n) = n - \floor{n/2} = \ceil{n/2}$.
For the path with $n$ vertices, the first $\floor{n/2}$ vertices have one edge leaving them, so $h \le 1/\floor{n/2}$.
The bound $\abs{S} \le \abs{V}/2$ cannot be dropped: for $S = V$ the ratio would be $0$ for every graph.
$h(G) > 0$ if and only if $G$ is [[connected|0FFAYNMAJZ]].
If $G$ is $d$-regular and $\lambda_2$ is the second largest eigenvalue of its adjacency matrix, then $\frac{d - \lambda_2}{2} \le h(G) \le \sqrt{2d(d - \lambda_2)}$.
The notation $h(G)$ and the names edge expansion and isoperimetric number are also used.
