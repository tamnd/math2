---
tag: KJ1A0GX9K0
kind: proof
name: Proof of the description of the closure in a metric space
msc: ["54E35"]
proves: 068P0P32DW
uses: [063W5JMY85, 0DRKT1QJR7, 0G5AV9Q4RR, 0DC3MPR7C9, 0B2305GNAZ, 0A26X79RTB]
sources:
  - url: https://en.wikipedia.org/wiki/Closure_(topology)
---

## Proof

We prove each direction separately.

1. Let $(X, d)$ be a [[metric space|063W5JMY85]], let $S \subseteq X$ and let $x \in X$. Let $\mathcal{F}$ be the family of all [[closed sets|0G5AV9Q4RR]] $F$ of $X$ with $S \subseteq F$.
2. By the definition of the [[closure|0DRKT1QJR7]], $\overline{S}$ is the intersection of the members of $\mathcal{F}$.
3. For $\varepsilon > 0$, let $B(x, \varepsilon)$ be the [[open ball|0DC3MPR7C9]]. A point $s$ lies in $B(x, \varepsilon)$ exactly when $d(x, s) < \varepsilon$.
4. First let $x \in \overline{S}$. Suppose, for a contradiction, that some $\varepsilon > 0$ has no $s \in S$ with $d(x, s) < \varepsilon$. Then $S \cap B(x, \varepsilon) = \varnothing$.
5. Put $F = X \setminus B(x, \varepsilon)$. Its complement $B(x, \varepsilon)$ is open, because [[open balls are open|0B2305GNAZ]]. So $F$ is closed.
6. By step 4, $S \subseteq F$. Hence $F \in \mathcal{F}$, and $\overline{S} \subseteq F$ by step 2.
7. But $d(x, x) = 0 < \varepsilon$, so $x \in B(x, \varepsilon)$ and $x \notin F$. This contradicts $x \in \overline{S} \subseteq F$.
8. So for each $\varepsilon > 0$ there is $s \in S$ with $d(x, s) < \varepsilon$.
9. Now suppose that for each $\varepsilon > 0$ there is $s \in S$ with $d(x, s) < \varepsilon$. Let $F \in \mathcal{F}$.
10. Suppose, for a contradiction, that $x \notin F$. Then $x$ lies in $X \setminus F$, which is open because $F$ is closed.
11. By the [[description of the open sets of a metric space|0A26X79RTB]], there is $\varepsilon > 0$ with $B(x, \varepsilon) \subseteq X \setminus F$.
12. By hypothesis, there is $s \in S$ with $d(x, s) < \varepsilon$. Then $s \in B(x, \varepsilon) \subseteq X \setminus F$, so $s \notin F$.
13. This contradicts $s \in S \subseteq F$. Hence $x \in F$.
14. So $x$ lies in each member of $\mathcal{F}$, and $x \in \overline{S}$ by step 2.

## Idea

If a ball about $x$ misses $S$, its complement is a closed set that holds $S$ but not $x$. So $x$ is not in the closure. If every ball about $x$ meets $S$, no closed superset of $S$ can leave $x$ out, since its open complement would hold such a ball.
