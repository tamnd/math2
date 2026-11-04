---
tag: 2TR8XV1ZBW
kind: proof
name: Proof that the continuous image of a closed interval is a closed interval
msc: [26A15]
proves: 06ZARTQTQE
uses: [0WS1A8E2P9, 00KAFBR32E, 0P27W9RW0G, 0EEE2CZB2A]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: Theorem
---

## Proof

We combine the extreme value theorem with the intermediate value theorem.

1. Let $a \le b$ and let $f \colon [a, b] \to \R$ be [[continuous|0P27W9RW0G]].
2. By the [[extreme value theorem|0WS1A8E2P9]], there are $c, d \in [a, b]$ with $f(c) \le f(x) \le f(d)$ for all $x \in [a, b]$.
3. Let $m = f(c)$ and $M = f(d)$. These are the minimum and the maximum of $f$ on $[a, b]$, and step 2 gives $f([a, b]) \subseteq [m, M]$.
4. Conversely, let $y \in [m, M]$. If $c = d$, then $m = M$, so $y = f(c) \in f([a, b])$.
5. Otherwise, let $p = \min(c, d)$ and $q = \max(c, d)$. Then $a \le p < q \le b$.
6. Let $h$ be the restriction of $f$ to $[p, q]$. Let $z \in [p, q]$ and let $V$ be an open interval containing $h(z)$.
7. Continuity of $f$ at $z$ gives an open interval $U$ containing $z$ with $f(x) \in V$ for all $x \in U \cap [a, b]$. Since $U \cap [p, q] \subseteq U \cap [a, b]$, $h$ is [[continuous at|0EEE2CZB2A]] $z$.
8. So $h$ is continuous. The numbers $h(p)$ and $h(q)$ are $m$ and $M$ in some order, so $y$ lies between $h(p)$ and $h(q)$.
9. By the [[intermediate value theorem|00KAFBR32E]], there is $x \in [p, q]$ with $f(x) = h(x) = y$. So $y \in f([a, b])$.
10. By steps 3, 4 and 9, $f([a, b]) = [m, M]$.

## Idea

The extreme value theorem gives the smallest and largest values $m$ and $M$, both attained. The intermediate value theorem, used on the interval between a minimum point and a maximum point, fills in every value between them. Nothing outside $[m, M]$ can be hit, by the choice of $m$ and $M$.
