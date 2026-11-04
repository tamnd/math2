---
tag: DN38VXHCF2
kind: proof
name: Proof of the Chernoff bound
msc: ["60E15"]
proves: 014PEBGDYF
uses: [05PWWHYBX5, 0NNRNGKMFM, 0KN2V7840E, 0P9BNBW2W3]
sources:
  - url: https://en.wikipedia.org/wiki/Chernoff_bound
    locator: Generic Chernoff bounds
---

## Proof

We apply Markov's inequality to $e^{tX}$ for each $t > 0$.

1. Let $X$ be a real random variable with [[moment-generating function|0NNRNGKMFM]] $M_X(t) = E[e^{tX}] \in (0, \infty]$. Let $a \in \R$.
2. Fix $t > 0$. The map $x \mapsto tx$ is increasing, and the [[exponential function is strictly increasing|0KN2V7840E]]. So $x \ge a$ holds if and only if $e^{tx} \ge e^{ta}$.
3. Hence $\set{X \ge a} = \set{e^{tX} \ge e^{ta}}$ as events.
4. The [[exponential function is positive|0P9BNBW2W3]], so $e^{tX}$ takes values in $[0, \infty)$ and $e^{ta} > 0$.
5. By [[Markov's inequality|05PWWHYBX5]] for $e^{tX}$ and the level $e^{ta}$, $P(e^{tX} \ge e^{ta}) \le E[e^{tX}]/e^{ta}$. This holds in $[0, \infty]$, also when $M_X(t) = \infty$.
6. By steps 3 and 5, $P(X \ge a) \le e^{-ta} M_X(t)$ for each $t > 0$.
7. So $P(X \ge a)$ is a lower bound of the set $\set{e^{-ta} M_X(t) : t > 0}$. It is therefore at most the infimum of this set.
8. Thus $P(X \ge a) \le \inf_{t > 0} e^{-ta} M_X(t)$.

## Idea

For $t > 0$ the map $x \mapsto e^{tx}$ is increasing, so $X \ge a$ exactly when $e^{tX} \ge e^{ta}$. Markov's inequality bounds this event for every $t$. Then one picks the best $t$.
