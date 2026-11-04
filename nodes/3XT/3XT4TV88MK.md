---
tag: 3XT4TV88MK
kind: proof
name: Proof that closed balls are closed
msc: ["54E35"]
proves: 0YS40B38JD
uses: [063W5JMY85, 05DSV40EB9, 0DC3MPR7C9, 01M6CW9VM6, 0A26X79RTB, 0G5AV9Q4RR]
sources:
  - url: https://proofwiki.org/wiki/Closed_Ball_is_Closed_in_Metric_Space
---

## Proof

We show that the complement of the closed ball is open.

1. Let $(X, d)$ be a [[metric space|063W5JMY85]], let $x \in X$ and let $r \ge 0$. Let $\bar{B}(x, r) = \set{z \in X : d(x, z) \le r}$ be the [[closed ball|05DSV40EB9]].
2. Put $C = X \setminus \bar{B}(x, r)$. Let $y \in C$. Then $d(x, y) > r$.
3. Put $\varepsilon = d(x, y) - r$. By step 2, $\varepsilon > 0$.
4. Let $z$ be in the [[open ball|0DC3MPR7C9]] $B(y, \varepsilon)$, so $d(y, z) < \varepsilon$.
5. By the [[triangle inequality|01M6CW9VM6]] and the symmetry of $d$, $d(x, y) \le d(x, z) + d(z, y) = d(x, z) + d(y, z)$.
6. Hence $d(x, z) \ge d(x, y) - d(y, z) > d(x, y) - \varepsilon = r$.
7. So $z \notin \bar{B}(x, r)$, that is, $z \in C$. Thus $B(y, \varepsilon) \subseteq C$.
8. Each point of $C$ has a ball about it inside $C$. By the [[description of the open sets of a metric space|0A26X79RTB]], $C$ is open.
9. By the definition of a [[closed set|0G5AV9Q4RR]], $\bar{B}(x, r)$ is closed in $X$.

## Idea

A point outside the closed ball is farther than $r$ from the centre, by some margin. The triangle inequality shows that a ball of that margin about the point stays outside. So the complement is open.
