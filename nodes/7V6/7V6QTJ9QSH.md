---
tag: 7V6QTJ9QSH
kind: proof
name: Proof that a union of open sets of a metric space is open
msc: ["54E35"]
proves: 0HEF46RPEK
uses: [063W5JMY85, 01ZQQDCERP, 05GK32H72H, 0DC3MPR7C9, 0A26X79RTB]
sources:
  - url: https://proofwiki.org/wiki/Union_of_Open_Sets_of_Metric_Space_is_Open
---

## Proof

1. Let $(X, d)$ be a [[metric space|063W5JMY85]] and let $(U_i)_{i \in I}$ be a family of [[open subsets|01ZQQDCERP]] of $X$.
2. Put $U = \bigcup_{i \in I} U_i$, the [[union|05GK32H72H]] of the family.
3. Let $x \in U$. By the definition of a union, there is $j \in I$ with $x \in U_j$.
4. The set $U_j$ is open. By the [[description of the open sets of a metric space|0A26X79RTB]], there is $\varepsilon > 0$ with $B(x, \varepsilon) \subseteq U_j$.
5. Here $B(x, \varepsilon)$ is the [[open ball|0DC3MPR7C9]] with centre $x$ and radius $\varepsilon$.
6. Since $U_j \subseteq U$, we get $B(x, \varepsilon) \subseteq U$.
7. So each point of $U$ has a ball about it inside $U$. By the same description of open sets, $U$ is open in $X$.

## Idea

A point of the union lies in one of the open sets. The ball that fits in that set also fits in the larger union. No bound on the number of sets is needed.
