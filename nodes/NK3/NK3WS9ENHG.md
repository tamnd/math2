---
tag: NK3WS9ENHG
kind: proof
name: Proof that metric spaces are Hausdorff
msc: ["54E35"]
proves: 0P9DCDES73
uses: [0MXB4CKHFW, 0DC3MPR7C9, 0B2305GNAZ, 01M6CW9VM6, 063W5JMY85]
sources:
  - url: https://proofwiki.org/wiki/Metric_Space_is_Hausdorff
---

## Proof

We separate two points by balls of half their distance.

1. Let $x, y \in X$ with $x \neq y$. By the axioms of a [[metric|063W5JMY85]], $d(x, y) > 0$. Let $r = d(x, y) / 2 > 0$.
2. The [[open balls|0DC3MPR7C9]] $B(x, r)$ and $B(y, r)$ are [[open|0B2305GNAZ]]. They contain $x$ and $y$, since $d(x, x) = 0 < r$ and $d(y, y) = 0 < r$.
3. Suppose some $z$ lies in both balls. Then $d(x, z) < r$ and $d(z, y) < r$.
4. By the [[triangle inequality|01M6CW9VM6]], $d(x, y) \le d(x, z) + d(z, y) < 2r = d(x, y)$. This is impossible.
5. So $B(x, r) \cap B(y, r) = \varnothing$, and $X$ is [[Hausdorff|0MXB4CKHFW]].

## Idea

Two distinct points are at a positive distance. Balls of half that radius around them cannot meet, since a common point would give a path between them that is shorter than their distance.
