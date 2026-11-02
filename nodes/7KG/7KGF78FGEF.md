---
tag: 7KGF78FGEF
kind: definition
name: Lp space
msc: ["46E30", 28A25]
defines: SASP14MA1Z
uses: [P15VQS5DJ9, YYNCJSR0PJ, DG76G5Z6XW, RARTMA0ZEC, 082RMRSY26, 08NYZ2FS6B]
sources:
  - url: https://en.wikipedia.org/wiki/Lp_space
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]], let $\mathbb{K}$ be $\R$ or $\C$, and let $1 \le p < \infty$.
Let $\mathcal{L}^p(\mu)$ be the set of [[measurable functions|YYNCJSR0PJ]] $f \colon X \to \mathbb{K}$ with $\int_X \abs{f}^p \, d\mu < \infty$, an [[integral of a non-negative function|DG76G5Z6XW]].
Call $f \sim g$ when $f = g$ [[almost everywhere|RARTMA0ZEC]].
The space $L^p(\mu)$ is the set of [[equivalence classes|082RMRSY26]] of $\mathcal{L}^p(\mu)$ under $\sim$, with pointwise operations on representatives.
Its [[norm|08NYZ2FS6B]] is
$$\norm{f}_p = \Big( \int_X \abs{f}^p \, d\mu \Big)^{1/p}.$$

## Remarks

Example: on $\R$ with Lebesgue measure, $f(x) = e^{-x^2}$ lies in $L^p$ for every $p$, since $\int e^{-p x^2} \, dx = \sqrt{\pi / p} < \infty$.

Non-example: $g(x) = 1 / (1 + \abs{x})$ on $\R$ is in $L^2$ but not in $L^1$.
Indeed $\int_\R (1 + \abs{x})^{-1} \, dx = \infty$, while $\int_\R (1 + \abs{x})^{-2} \, dx = 2$.

The operations and the norm do not depend on the representatives.
The map $\norm{\cdot}_p$ is a norm by the [[Minkowski inequality|N4QZS912MT]], and $\norm{f}_p = 0$ forces $f = 0$ almost everywhere.
With this norm $L^p(\mu)$ is a Banach space, by the [[Riesz–Fischer theorem|WVV4MFB2SE]].
For $p = \infty$ one uses the essential supremum instead, which gives the space [[L-infinity|ZT01G7BTSV]].
With the counting measure on $\N$, $L^p$ is the sequence space $\ell^p$.
