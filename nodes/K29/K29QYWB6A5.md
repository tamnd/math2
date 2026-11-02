---
tag: K29QYWB6A5
kind: example
name: Stirling's series
msc: [33B15, 41A60]
instance_of: [BJQTEPEZ9G]
sources:
  - url: https://en.wikipedia.org/wiki/Stirling%27s_approximation
---

## Example

Let $\Gamma$ be the [[gamma function|0V3FZMVB4K]], let $\ln \Gamma$ be its principal branch on $\C \setminus (-\infty, 0]$, and let $B_{2k}$ be the [[Bernoulli numbers|0RAS24E1R5]].
Fix $\delta$ with $0 < \delta < \pi$.
As $z \to \infty$ in the sector $\abs{\arg z} \le \pi - \delta$,
$$\ln \Gamma(z) \sim \left(z - \tfrac{1}{2}\right) \ln z - z + \tfrac{1}{2} \ln(2\pi) + \sum_{k=1}^{\infty} \frac{B_{2k}}{2k(2k-1) \, z^{2k-1}}.$$
This is an [[asymptotic expansion|BJQTEPEZ9G]] in the scale $z \ln z, z, \ln z, 1, z^{-1}, z^{-3}, z^{-5}, \ldots$.
With $B_2 = \frac{1}{6}$, $B_4 = -\frac{1}{30}$ and $B_6 = \frac{1}{42}$, the first correction terms are
$$\frac{1}{12 z} - \frac{1}{360 z^3} + \frac{1}{1260 z^5}.$$

## Remarks

The series diverges for every $z$.
Indeed $\abs{B_{2k}}$ grows like $2 (2k)! / (2\pi)^{2k}$, so the terms grow like a factorial divided by a power of $z$.
For real $z = x > 0$, the error after the term in $z^{-(2N-1)}$ has the sign of the first omitted term and is smaller in absolute value.
For $x = 10$, the first correction $\frac{1}{120}$ already gives $\ln \Gamma(10) = \ln(9!)$ with an error below $\frac{1}{360\,000} < 3 \cdot 10^{-6}$.
Taking the exponential of the first terms gives [[Stirling's formula|0KC0F51T6A]] $n! \sim \sqrt{2\pi n} \, (n/e)^n$.

## Explanations

### L1 human

Stirling's series is a sharpened Stirling formula for the logarithm of the factorial.
Each extra term makes the estimate better for large $z$, up to a point.
If one keeps adding terms forever, the sum blows up, which shows that a useful asymptotic expansion can diverge.
