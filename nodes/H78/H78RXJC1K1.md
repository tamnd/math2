---
tag: H78RXJC1K1
kind: statement
role: theorem
name: Layer cake representation
msc: [28A25, "46E30"]
uses: [HQVXKEMN5N, DG76G5Z6XW, 2Z2QVWZ262, WEBBT18D4X]
about: [HQVXKEMN5N, DG76G5Z6XW]
sources:
  - url: https://en.wikipedia.org/wiki/Layer_cake_representation
same_as:
  wikidata: Q6505514
  wikipedia: Layer cake representation
---

## Statement

Let $(X, \Sigma, \mu)$ be a [[σ-finite|WEBBT18D4X]] measure space.
Let $f \colon X \to [0, \infty]$ be a measurable function with [[distribution function|HQVXKEMN5N]] $d_f(t) = \mu(\set{f > t})$.
Then
$$\int_X f \, d\mu = \int_0^\infty d_f(t) \, dt,$$
where the left side is the [[integral of a non-negative function|DG76G5Z6XW]] and the right side is taken with [[Lebesgue measure|2Z2QVWZ262]].
More generally, for $0 < p < \infty$,
$$\int_X f^p \, d\mu = p \int_0^\infty t^{p-1} d_f(t) \, dt.$$

## Remarks

The name comes from the pointwise identity $f(x) = \int_0^\infty \mathbf{1}_{\set{f > t}}(x) \, dt$.
It writes $f$ as a stack of thin horizontal layers, one for each height $t$.
Integrating over $X$ and exchanging the two integrals by Tonelli's theorem gives the formula.
The second formula follows in the same way from $f(x)^p = \int_0^{f(x)} p t^{p-1} \, dt$.

Example: for $f(x) = x$ on $[0, 1]$ with Lebesgue measure, $d_f(t) = 1 - t$ for $0 \le t \le 1$ and $0$ after.
Both sides equal $1/2$.

For a non-negative random variable $Y$ the first formula reads $\mathbb{E}[Y] = \int_0^\infty P(Y > t) \, dt$.

## Explanations

### L1 human

To find the volume under a graph, one can slice it vertically or horizontally.
The layer cake formula slices horizontally.
At each height $t$ it measures the size of the region where the function is above $t$, and then adds these sizes over all heights.

### L2 human

The formula turns integrals of $f$ into integrals of its distribution function.
This is why the $L^p$ norms depend only on $d_f$, so equimeasurable functions and decreasing rearrangements have the same norms.
It is the basic tool behind weak $L^p$ estimates, the Marcinkiewicz interpolation theorem and the bounds for the Hardy–Littlewood maximal function.
