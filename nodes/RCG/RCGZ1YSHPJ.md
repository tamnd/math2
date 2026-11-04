---
tag: RCGZ1YSHPJ
kind: proof
name: Proof that a continuous injective function on an interval is strictly monotone
msc: [26A48]
proves: 0D6FCW80A0
uses: [00KAFBR32E, 0TR9SR9FTB, 0TK8Y3J5RW, 0P27W9RW0G, 0PVG1CRAJN]
sources:
  - url: https://proofwiki.org/wiki/Continuous_Injection_of_Interval_is_Strictly_Monotone
---

## Proof

We first show that $f$ is monotone on any three points, using the [[intermediate value theorem|00KAFBR32E]].

1. Let $x < y < z$ be points of $I$. Since $I$ is an [[interval|0TK8Y3J5RW]], $[x, z] \subseteq I$. The restriction of $f$ to any closed subinterval of $[x, z]$ is [[continuous|0P27W9RW0G]].
2. The values $f(x)$, $f(y)$, $f(z)$ are distinct, since $f$ is [[injective|0PVG1CRAJN]].
3. Claim: $f(y)$ lies strictly between $f(x)$ and $f(z)$. Suppose not. Then $f(y)$ is larger than both $f(x)$ and $f(z)$, or smaller than both.
4. Case $f(y) > f(x)$ and $f(y) > f(z)$, with $f(x) < f(z)$. Then $f(x) < f(z) < f(y)$. The intermediate value theorem on $[x, y]$ gives $t \in [x, y]$ with $f(t) = f(z)$. But $t \le y < z$, which contradicts injectivity.
5. Case $f(y) > f(x)$ and $f(y) > f(z)$, with $f(z) < f(x)$. Then $f(z) < f(x) < f(y)$. The intermediate value theorem on $[y, z]$ gives $t \in [y, z]$ with $f(t) = f(x)$. But $t \ge y > x$, which contradicts injectivity.
6. Case $f(y)$ smaller than both. Then $-f(y)$ is larger than $-f(x)$ and $-f(z)$, and $-f$ is continuous and injective. Steps 4 and 5 for $-f$ give a contradiction.
7. So the claim holds. Hence $f(y) - f(x)$ and $f(z) - f(y)$ are both positive or both negative.
8. Now let $w_1 < w_2 < \cdots < w_m$ be finitely many points of $I$, with $m \ge 2$. Put $d_i = f(w_{i+1}) - f(w_i)$ for $1 \le i < m$.
9. Each $d_i$ is nonzero by step 2. By step 7 for the triple $w_i < w_{i+1} < w_{i+2}$, $d_i$ and $d_{i+1}$ have the same sign. By induction on $i$, all $d_i$ have the sign of $d_1$.
10. If $d_1 > 0$, then $f(w_1) < f(w_2) < \cdots < f(w_m)$. If $d_1 < 0$, then $f(w_1) > \cdots > f(w_m)$.
11. If $I$ has fewer than two points, $f$ is [[strictly increasing|0TR9SR9FTB]] because there is nothing to check. Otherwise fix $p < q$ in $I$. By step 2, $f(p) < f(q)$ or $f(p) > f(q)$.
12. Suppose $f(p) < f(q)$. Let $u < v$ be points of $I$. List the set $\set{p, q, u, v}$ in increasing order as in step 8.
13. By step 10, $f$ is strictly increasing on this list or strictly decreasing on it. Since $p < q$ and $f(p) < f(q)$, it is strictly increasing. So $f(u) < f(v)$.
14. Thus $f$ is strictly increasing on $I$. If instead $f(p) > f(q)$, the same argument shows that $f$ is strictly decreasing.
15. In both cases $f$ is strictly monotone.

## Idea

If the middle one of three points had the largest or smallest value, the intermediate value theorem would make $f$ take some value twice. So $f$ goes the same way along any three points, and hence along any finite list of points. Comparing an arbitrary pair with one fixed pair then fixes the direction everywhere.
