---
tag: VPHQ121S8A
kind: proof
name: Proof that open balls are open
msc: ["54E35"]
proves: 0B2305GNAZ
uses: [063W5JMY85, 0DC3MPR7C9, 01M6CW9VM6, 0A26X79RTB]
sources:
  - url: https://proofwiki.org/wiki/Open_Ball_of_Metric_Space_is_Open_Set
---

## Proof

1. Let $(X, d)$ be a [[metric space|063W5JMY85]], let $x \in X$ and let $r > 0$. Let $B(x, r) = \set{z \in X : d(x, z) < r}$ be the [[open ball|0DC3MPR7C9]].
2. Let $y \in B(x, r)$. Then $d(x, y) < r$.
3. Put $\varepsilon = r - d(x, y)$. By step 2, $\varepsilon > 0$.
4. Let $z \in B(y, \varepsilon)$, so $d(y, z) < \varepsilon$.
5. By the [[triangle inequality|01M6CW9VM6]], $d(x, z) \le d(x, y) + d(y, z) < d(x, y) + \varepsilon = r$.
6. So $z \in B(x, r)$. As $z$ was arbitrary, $B(y, \varepsilon) \subseteq B(x, r)$.
7. Each point $y$ of $B(x, r)$ thus has a ball about it inside $B(x, r)$.
8. By the [[description of the open sets of a metric space|0A26X79RTB]], $B(x, r)$ is open in $X$.

## Idea

A point $y$ inside the ball is at distance $d(x, y)$ from the centre. So it still has room $r - d(x, y)$ before it reaches the edge. The triangle inequality shows that the ball of that radius about $y$ stays inside.
