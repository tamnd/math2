---
tag: 7PCHXZM5YE
kind: definition
name: L-infinity space
msc: ["46E30"]
defines: ZT01G7BTSV
uses: [P15VQS5DJ9, YYNCJSR0PJ, WPC2XRMB9Y, RARTMA0ZEC]
sources:
  - url: https://en.wikipedia.org/wiki/L-infinity
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]], and let $\mathbb{K}$ be $\R$ or $\C$.
A [[measurable function|YYNCJSR0PJ]] $f \colon X \to \mathbb{K}$ is *essentially bounded* if there is $M \ge 0$ with $\mu(\set{x \in X : \abs{f(x)} > M}) = 0$.
Its norm is the [[essential supremum|WPC2XRMB9Y]]
$$\norm{f}_\infty = \inf \set{M \ge 0 : \mu(\set{x : \abs{f(x)} > M}) = 0}.$$
The space $L^\infty(\mu)$ is the set of essentially bounded measurable functions modulo equality [[almost everywhere|RARTMA0ZEC]], with the norm $\norm{\cdot}_\infty$.

## Remarks

Example: on $[0, 1]$ with Lebesgue measure, let $f(x) = x$ for rational $x$ and $f(x) = 0$ otherwise.
The set where $f \ne 0$ is countable, so it has measure $0$, and $\norm{f}_\infty = 0$.
So $f$ is the zero element of $L^\infty$.

Non-example: $f(x) = 1/x$ on $(0, 1]$ is not essentially bounded.
For each $M > 0$, the set $\set{f > M}$ contains the interval $(0, \min(1, 1/M))$, which has positive measure.

The infimum in the definition is attained: $\abs{f} \le \norm{f}_\infty$ almost everywhere.
With the counting measure on a set $I$, $L^\infty$ is the space $\ell^\infty(I)$ of bounded families with the supremum norm.
