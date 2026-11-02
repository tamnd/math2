---
tag: 9CZVKQMCZP
kind: definition
name: Choquet integral
msc: ["28E10", 28A25]
defines: 36TXCRZ6GC
uses: [CRFQEGJDA9, N4KDT83V3S, YYNCJSR0PJ]
sources:
  - url: https://en.wikipedia.org/wiki/Choquet_integral
    locator: Definition
---

## Definition

Let $(X, \mathcal{F})$ be a [[measurable space|N4KDT83V3S]], and let $\nu \colon \mathcal{F} \to [0, \infty)$ be a [[fuzzy measure|CRFQEGJDA9]].
Let $f \colon X \to [0, \infty)$ be [[measurable|YYNCJSR0PJ]].
The *Choquet integral* of $f$ with respect to $\nu$ is
$$(C)\!\int f \, d\nu = \int_0^\infty \nu(\set{x \in X : f(x) \ge t}) \, dt.$$
The function $t \mapsto \nu(\set{f \ge t})$ is non-increasing, so the right side is a well-defined Lebesgue integral with value in $[0, \infty]$.

## Remarks

If $f$ takes the values $0 = a_0 < a_1 < \cdots < a_k$, then $(C)\!\int f \, d\nu = \sum_{i=1}^{k} (a_i - a_{i-1}) \, \nu(\set{f \ge a_i})$.
If $\nu$ is a measure, the Choquet integral equals the Lebesgue integral, by the [[layer cake representation|H78RXJC1K1]].
Example: let $X = \set{1, 2}$ with all subsets, $\nu(\set{1}) = \nu(\set{2}) = 0$ and $\nu(X) = 1$.
Then $\nu$ is monotone with $\nu(\emptyset) = 0$, and the indicators $1_{\set{1}}$ and $1_{\set{2}}$ have Choquet integral $0$.
Their sum $1_X$ has Choquet integral $\int_0^1 \nu(X) \, dt = 1$, so the integral is not additive.
Non-example: if $f$ is not measurable, some set $\set{f \ge t}$ lies outside $\mathcal{F}$, so $\nu$ is not defined on it and the formula makes no sense.
Some authors use $\set{f > t}$; this changes the integrand at only countably many $t$, so the integral is the same.
