---
tag: HFREZDYZH4
kind: proof
name: Proof of the description of the open sets of a metric space
msc: ["54E35"]
proves: 0A26X79RTB
uses: [063W5JMY85, 01ZQQDCERP, 0A6YRNZB2R, 0DC3MPR7C9]
sources:
  - url: https://en.wikipedia.org/wiki/Open_set
---

## Proof

We unfold the definitions.

1. Let $(X, d)$ be a [[metric space|063W5JMY85]] and let $U \subseteq X$.
2. By the definition of an [[open set|01ZQQDCERP]] of a metric space, $U$ is open in $X$ if and only if $U \in \tau_d$. Here $\tau_d$ is the [[metric topology|0A6YRNZB2R]].
3. By the definition of $\tau_d$, we have $U \in \tau_d$ if and only if each $x \in U$ has a real $\varepsilon > 0$ with $B(x, \varepsilon) \subseteq U$.
4. Here $B(x, \varepsilon)$ is the [[open ball|0DC3MPR7C9]] with centre $x$ and radius $\varepsilon$.
5. Steps 2 and 3 together give: $U$ is open if and only if each $x \in U$ has an $\varepsilon > 0$ with $B(x, \varepsilon) \subseteq U$.

## Idea

The open sets of a metric space are by definition the members of the metric topology. That topology is defined by the ball condition, so the statement only puts the two definitions side by side.
