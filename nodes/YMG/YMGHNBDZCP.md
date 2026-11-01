---
tag: YMGHNBDZCP
kind: definition
name: Oscillation of a function
msc: [26A15]
defines: 5XW4N8KY3Y
uses: [0XHDTE5YMZ, 0BTMQ04556, 04KFTA34C5, 0GSZ7B0CGR, 0EEE2CZB2A, 0T4EJ8ZJM9, 0565EGK6XP]
sources:
  - url: https://en.wikipedia.org/wiki/Oscillation_(mathematics)
    locator: Definitions
---

## Definition

Let $D \subseteq \R$, let $f \colon D \to \R$ be a [[function|0XHDTE5YMZ]], and let $A \subseteq D$ be nonempty.
The *oscillation of $f$ on $A$* is
$$\operatorname{osc}_f(A) = \sup_{x \in A} f(x) - \inf_{x \in A} f(x) = \sup \set{\abs{f(x) - f(y)} : x, y \in A},$$
a value in $[0, \infty]$.
For $x_0 \in D$, the *oscillation of $f$ at $x_0$* is
$$\operatorname{osc}_f(x_0) = \inf_{\varepsilon > 0} \operatorname{osc}_f\big(D \cap (x_0 - \varepsilon, x_0 + \varepsilon)\big).$$

## Remarks

The quantity $\operatorname{osc}_f(D \cap (x_0 - \varepsilon, x_0 + \varepsilon))$ decreases as $\varepsilon$ decreases, so the infimum is also the limit as $\varepsilon \to 0^+$.
The function $f$ is [[continuous at|0EEE2CZB2A]] $x_0$ if and only if $\operatorname{osc}_f(x_0) = 0$.
For each $c > 0$, the set $\set{x \in D : \operatorname{osc}_f(x) \ge c}$ is closed in $D$.
So the set of discontinuities of $f$ is a countable union of closed subsets of $D$.

Example: let $f(x) = x^2$ on $\R$ and $x_0 = 1$.
On $(1 - \varepsilon, 1 + \varepsilon)$ with $\varepsilon < 1$, the values fill $((1 - \varepsilon)^2, (1 + \varepsilon)^2)$, a spread of $4\varepsilon$.
This tends to $0$, so $\operatorname{osc}_f(1) = 0$, as continuity predicts.

Non-example of continuity: the [[Dirichlet function|0T4EJ8ZJM9]], equal to $1$ on $\Q$ and $0$ elsewhere, takes both values on every interval.
So its oscillation is $1$ at every point, and it is continuous nowhere.
