---
tag: QDY3FRAGRS
kind: definition
name: Differential entropy
msc: [94A17, 62B10]
defines: B4PNYNYVKK
uses: [045D8P03E0, 0ZY9DX8FBF, DWJF7ABPR1, 04DXAFN2ES, 05AQE0QR0D, Y86E072V0V]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_entropy
---

## Definition

Let $X$ be a [[random vector with a density|045D8P03E0]] $f$ on $\R^n$, that is, a [[probability density function|0ZY9DX8FBF]] with respect to Lebesgue measure.
Assume that the [[Lebesgue integral|DWJF7ABPR1]] of $f \log f$ over $\set{f > 0}$ exists in $[-\infty, +\infty]$, that is, its positive part or its negative part is finite.
The *differential entropy* of $X$ is
$$h(X) = -\int_{\set{f > 0}} f(x) \log f(x) \, dx \in [-\infty, +\infty].$$

## Remarks

It depends only on the law of $X$, so one also writes $h(f)$.
With the [[natural logarithm|04DXAFN2ES]] the unit is the nat.

Example: if $X$ is uniform on $[0, a]$ with $a > 0$, then $f = 1/a$ on $[0, a]$ and $h(X) = -\int_0^a \frac1a \log \frac1a \, dx = \log a$, which is negative for $a < 1$.
For the [[normal distribution|05AQE0QR0D]] with variance $\sigma^2$, $h(X) = \frac12 \log (2 \pi e \sigma^2)$.

Non-example: a random variable with $P(X = 0) = 1$ has no density, so it has no differential entropy in this sense.
It is the limit of the uniform laws on $[0, a]$ as $a \to 0$, whose entropies $\log a$ tend to $-\infty$.

For an invertible $n \times n$ matrix $A$ and $b \in \R^n$, $h(AX + b) = h(X) + \log \abs{\det A}$.
If $X$ is discretized into cells of side $\Delta$, the [[Shannon entropy|Y86E072V0V]] of the result is close to $h(X) - n \log \Delta$ for small $\Delta$, under mild regularity of $f$.

## Explanations

### L1 human

Differential entropy is the formula of Shannon entropy with the sum replaced by an integral and the probabilities replaced by a density.
