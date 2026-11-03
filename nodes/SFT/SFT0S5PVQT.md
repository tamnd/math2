---
tag: SFT0S5PVQT
kind: definition
name: Randić index
msc: [05C09, 05C92]
defines: R37X2BTK50
uses: [0JD5C82QMB, 0KS0KRDV4Y, AE724Y8CQX]
sources:
  - url: https://en.wikipedia.org/wiki/Randić_index
---

## Definition

Let $G$ be a finite simple [[graph|0JD5C82QMB]] with edge set $E$, and let $d(v)$ be the [[degree|0KS0KRDV4Y]] of a vertex $v$.
The *Randić index* of $G$ is
$$R(G) = \sum_{uv \in E} \frac{1}{\sqrt{d(u)\, d(v)}}.$$
Each term is defined, since both ends of an edge have degree at least $1$.

## Remarks

Example: the path $P_3$ has two edges, each joining a vertex of degree $1$ to a vertex of degree $2$, so $R(P_3) = 2/\sqrt 2 = \sqrt 2$.
The star $K_{1,k}$ has $k$ edges with degrees $1$ and $k$, so $R(K_{1,k}) = k/\sqrt k = \sqrt k$.
An $r$-regular graph on $n$ vertices, with $r \ge 1$, has $nr/2$ edges of weight $1/r$, so its index is $n/2$.
Non-example: the sum $\sum_{uv \in E} d(u)\, d(v)$ is a different index, the second Zagreb index, not the Randić index.
Isolated vertices do not contribute to $R(G)$.
A general form replaces the exponent $-1/2$ by a real number $\alpha$.
