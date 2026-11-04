---
tag: WDPRC89NXK
kind: proof
name: Proof that a finite intersection of open sets of a metric space is open
msc: ["54E35"]
proves: 09NDE9V7X1
uses: [063W5JMY85, 01ZQQDCERP, 0HBRW4E6G1, 0DC3MPR7C9, 0A26X79RTB]
sources:
  - url: https://proofwiki.org/wiki/Finite_Intersection_of_Open_Sets_of_Metric_Space_is_Open
---

## Proof

1. Let $(X, d)$ be a [[metric space|063W5JMY85]], let $n \ge 1$, and let $U_1, \ldots, U_n$ be [[open subsets|01ZQQDCERP]] of $X$.
2. Put $U = U_1 \cap \cdots \cap U_n$, the [[intersection|0HBRW4E6G1]] of these sets.
3. Let $x \in U$. Then $x \in U_k$ for each $k = 1, \ldots, n$.
4. Each $U_k$ is open. By the [[description of the open sets of a metric space|0A26X79RTB]], there is $\varepsilon_k > 0$ with $B(x, \varepsilon_k) \subseteq U_k$.
5. Here $B(x, \varepsilon_k)$ is the [[open ball|0DC3MPR7C9]] with centre $x$ and radius $\varepsilon_k$.
6. Put $\varepsilon = \min(\varepsilon_1, \ldots, \varepsilon_n)$. This is the least of finitely many positive reals, so $\varepsilon > 0$.
7. Let $y \in B(x, \varepsilon)$. Then $d(x, y) < \varepsilon \le \varepsilon_k$, so $y \in B(x, \varepsilon_k) \subseteq U_k$ for each $k$.
8. Thus $y \in U$, and so $B(x, \varepsilon) \subseteq U$.
9. Each point of $U$ has a ball about it inside $U$. By the same description of open sets, $U$ is open in $X$.

## Idea

Each of the sets gives a radius that works for it. The smallest radius works for all of them at once. Finiteness matters: the minimum of finitely many positive numbers is positive, but an infimum of infinitely many can be $0$.
