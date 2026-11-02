---
tag: VVVJ655R0J
kind: definition
name: Tricomi confluent hypergeometric function
msc: [33C15]
defines: 234F5DNAJH
uses: [6AZ4ZBN1M8, 0H5SYBSED9, NT917KFR57]
sources:
  - url: https://en.wikipedia.org/wiki/Confluent_hypergeometric_function
---

## Definition

Let $a$ and $b$ be complex numbers, let $z \in \C \setminus (-\infty, 0]$, and let $z^{1 - b}$ be the principal branch.
Let $M$ be [[Kummer's function|6AZ4ZBN1M8]] and $\Gamma$ the [[gamma function|0H5SYBSED9]], with $1/\Gamma$ read as $0$ at the poles of $\Gamma$.
If $b \notin \Z$, the *Tricomi confluent hypergeometric function* is
$$U(a, b, z) = \frac{\Gamma(1 - b)}{\Gamma(a - b + 1)} M(a, b, z) + \frac{\Gamma(b - 1)}{\Gamma(a)} z^{1 - b} M(a - b + 1, 2 - b, z).$$
If $b \in \Z$, it is defined by continuity: $U(a, b, z) = \lim_{\beta \to b} U(a, \beta, z)$.

## Remarks

The function $U(a, b, \cdot)$ solves [[Kummer's equation|NT917KFR57]], since both terms of the definition do.
It is characterised among the solutions by $U(a, b, z) \sim z^{-a}$ as $z \to \infty$ with $\abs{\arg z} < \frac{3\pi}{2} - \delta$, for each $\delta > 0$.
For $\operatorname{Re} a > 0$ and $\operatorname{Re} z > 0$ it has the integral form
$$U(a, b, z) = \frac{1}{\Gamma(a)} \int_0^\infty e^{-zt}\, t^{a - 1} (1 + t)^{b - a - 1}\, dt.$$
Example: $U(a, a + 1, z) = z^{-a}$; for $\operatorname{Re} a > 0$ and $\operatorname{Re} z > 0$ the integral is $\frac{1}{\Gamma(a)} \int_0^\infty e^{-zt} t^{a - 1}\, dt = z^{-a}$.
Non-example: $M(a, b, z)$ itself is in general not a multiple of $U(a, b, z)$; for $a = b$ it is $e^z$, which grows faster than any power as $z \to +\infty$.
The two functions satisfy Kummer's second transformation $U(a, b, z) = z^{1 - b} U(a - b + 1, 2 - b, z)$.
