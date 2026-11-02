---
tag: DCH91F9YDK
kind: definition
name: de Casteljau's algorithm
msc: [65D17, 68U07, 41A10]
defines: HT4Q9K3P2Z
uses: [NEXBTGYYRG, 21SXYJYC59]
sources:
  - url: https://en.wikipedia.org/wiki/De_Casteljau%27s_algorithm
---

## Definition

Let $n \ge 1$, let $P_0, \dots, P_n$ be points of $\R^d$ (or real numbers), and let $t \in \R$.
*De Casteljau's algorithm* computes points $P_i^{(j)}$ for $0 \le j \le n$ and $0 \le i \le n - j$ by

1. $P_i^{(0)} = P_i$ for $i = 0, \dots, n$;
2. $P_i^{(j)} = (1 - t)\, P_i^{(j-1)} + t\, P_{i+1}^{(j-1)}$ for $j = 1, \dots, n$ and $i = 0, \dots, n - j$;

and returns $P_0^{(n)}$.

## Remarks

The output equals $B(t) = \sum_{k=0}^{n} \binom{n}{k} (1-t)^{n-k} t^k P_k$, the point of the [[Bézier curve|NEXBTGYYRG]] with these control points; by induction on $j$, $P_i^{(j)} = \sum_{k=0}^{j} \binom{j}{k} (1-t)^{j-k} t^k P_{i+k}$.
For $t \in [0, 1]$ each step is a [[convex combination|21SXYJYC59]].
Example: $n = 2$, $P_0 = (0, 0)$, $P_1 = (1, 2)$, $P_2 = (2, 0)$, $t = 1/2$: then $P_0^{(1)} = (1/2, 1)$, $P_1^{(1)} = (3/2, 1)$ and $P_0^{(2)} = (1, 1)$, which is $B(1/2)$.
Non-example: replacing step 2 by the average $\tfrac{1}{2}(P_i^{(j-1)} + P_{i+1}^{(j-1)})$ for all $t$ returns $B(1/2)$ no matter what $t$ is, so it does not compute $B(t)$ for $t \ne 1/2$.
The points $P_0^{(0)}, P_0^{(1)}, \dots, P_0^{(n)}$ and $P_0^{(n)}, P_1^{(n-1)}, \dots, P_n^{(0)}$ are the control points of the curve restricted to $[0, t]$ and to $[t, 1]$, reparametrized to $[0, 1]$.
The algorithm costs $O(n^2)$ operations, more than Horner's scheme, but it is more stable.
