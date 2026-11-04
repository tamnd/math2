---
tag: TPQVT6GZAW
kind: proof
name: Proof of Mantel's theorem by double counting
msc: [05C35]
proves: 0MXEHSCYCS
uses: [0JD5C82QMB, 0T0F6CCS9W, 01T3TMGTTE, 07CT9RDY7Q, 0XAP8WHNES, 0RFWW56Y22, 0F8YBHF2W3]
sources:
  - url: http://www.its.caltech.edu/~dconlon/EGT1.pdf
    locator: Theorem 1, first proof
---

## Proof

We double count the sum of the squares of the degrees and apply the Cauchy–Schwarz inequality.

1. Let $G$ be a finite simple [[graph|0JD5C82QMB]] with vertex set $V$, $\abs{V} = n$, and $m$ edges. Suppose that $G$ has no [[cycle|07CT9RDY7Q]] of length $3$. For $v \in V$, write $d(v)$ for its [[degree|0T0F6CCS9W]] and $N(v)$ for its [[neighbourhood|01T3TMGTTE]].
2. If $m = 0$, then $m = 0 \le \floor{n^2/4}$. From now on let $m \ge 1$, so $n \ge 2$.
3. Let $xy$ be an edge. If a vertex $z$ were adjacent to both $x$ and $y$, then $z \ne x, y$ and $x, y, z, x$ would be a cycle of length $3$. So $N(x) \cap N(y) = \varnothing$.
4. Hence $d(x) + d(y) = \abs{N(x)} + \abs{N(y)} = \abs{N(x) \cup N(y)} \le n$ for every edge $xy$.
5. We [[double count|0F8YBHF2W3]] the sum $\sum_{xy} \big(d(x) + d(y)\big)$ over all edges $xy$. A vertex $v$ is an end of exactly $d(v)$ edges, and each of them contributes $d(v)$ to the sum.
6. So $\sum_{v \in V} d(v)^2 = \sum_{xy} \big(d(x) + d(y)\big) \le m n$, by Step 4.
7. By the [[handshaking lemma|0XAP8WHNES]], $\sum_{v \in V} d(v) = 2m$.
8. Apply the [[Cauchy–Schwarz inequality|0RFWW56Y22]] in $\R^n$, with the standard inner product, to the vectors $(d(v))_{v \in V}$ and $(1)_{v \in V}$. This gives $\left(\sum_v d(v)\right)^2 \le n \sum_v d(v)^2$.
9. By Steps 6, 7 and 8, $4m^2 \le n \cdot m n = m n^2$.
10. Divide by $4m > 0$ to get $m \le n^2/4$.
11. Since $m$ is an integer, $m \le \floor{n^2/4}$.

## Idea

In a triangle-free graph, the two ends of an edge have no common neighbour, so their degrees add up to at most $n$. Summing over edges bounds the sum of squared degrees by $mn$. Cauchy–Schwarz bounds the same sum from below by $4m^2/n$, and comparing the two gives $m \le n^2/4$.
