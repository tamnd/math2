---
tag: ZVW3MT4WMT
kind: definition
name: Essential supremum
msc: [28A20, 28A25]
defines: WPC2XRMB9Y
uses: [P15VQS5DJ9, YYNCJSR0PJ, VQQM4Y550T, 04KFTA34C5, 0GSZ7B0CGR]
sources:
  - url: https://en.wikipedia.org/wiki/Essential_infimum_and_essential_supremum
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]] and let $f \colon X \to [-\infty, \infty]$ be a [[measurable function|YYNCJSR0PJ]].
A number $c \in [-\infty, \infty]$ is an *essential upper bound* of $f$ if the set $\set{x \in X : f(x) > c}$ is a [[null set|VQQM4Y550T]].
The *essential supremum* of $f$ is the [[infimum|04KFTA34C5]] of its essential upper bounds in the [[extended real line|0GSZ7B0CGR]]:
$$\operatorname{ess\,sup} f = \inf \set{c \in [-\infty, \infty] : \mu(\set{x \in X : f(x) > c}) = 0}.$$

## Remarks

Example: on $\R$ with Lebesgue measure, let $f = \mathbf{1}_{\Q}$, the indicator function of the rationals.
The set $\set{f > 0} = \Q$ is countable, so it has measure $0$, and $\operatorname{ess\,sup} f \le 0$.
For $c < 0$ the set $\set{f > c}$ is all of $\R$, so $\operatorname{ess\,sup} f = 0$, while $\sup f = 1$.

Non-example: the number $1/2$ is not an essential upper bound of $g(x) = x$ on $[0, 1]$ with Lebesgue measure.
The set $\set{g > 1/2} = (1/2, 1]$ has measure $1/2 \ne 0$.
In fact $\operatorname{ess\,sup} g = 1$.

The essential supremum is itself an essential upper bound, since $\set{f > c}$ is a countable union of the sets $\set{f > c + 1/n}$.
The *essential infimum* is $\operatorname{ess\,inf} f = -\operatorname{ess\,sup}(-f)$.
The quantity $\operatorname{ess\,sup} \abs{f}$ is the norm $\norm{f}_\infty$ of the space [[L-infinity|ZT01G7BTSV]].
