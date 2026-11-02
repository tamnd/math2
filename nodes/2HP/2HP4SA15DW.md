---
tag: 2HP4SA15DW
kind: example
name: Riemann zeta function as a series
msc: [40A05, 11M06, 40A30]
instance_of: [8MWTEF6462]
uses: [HN0AXS6VSG, 0ZNSSK8ZK1, 0W3K3QPEWT, 0NX5NWAFC9, 0CXTMAY5PX, TXB2F07CC6]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_zeta_function
---

## Example

For a complex number $s$ with real part $\sigma = \operatorname{Re} s$, consider the series
$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}, \qquad n^{-s} = e^{-s \log n}.$$
It is the [[Dirichlet series|HN0AXS6VSG]] of the constant arithmetic function $a(n) = 1$.
Its terms satisfy $\abs{n^{-s}} = n^{-\sigma}$.
By the [[p-series test|0ZNSSK8ZK1]], $\sum_n n^{-\sigma}$ converges exactly when $\sigma > 1$.
So the series converges [[absolutely|0W3K3QPEWT]] for every $s$ with $\operatorname{Re} s > 1$.

Fix $\sigma_0 > 1$; on the half-plane $\operatorname{Re} s \ge \sigma_0$ the bound $\abs{n^{-s}} \le n^{-\sigma_0}$ holds.
So the [[Weierstrass M-test|0NX5NWAFC9]], in its form for complex-valued functions, shows that the series converges uniformly there.
On the whole half-plane $\operatorname{Re} s > 1$ the convergence is not uniform.
Indeed, for real $s \to 1^+$ the tail $\sum_{n > N} n^{-s}$ tends to $\sum_{n > N} n^{-1} = \infty$.
So for every $N$ the tail is unbounded on the half-plane.
At $s = 1$ the series is the [[harmonic series|0CXTMAY5PX]], which diverges.

## Remarks

The sum of this series on $\operatorname{Re} s > 1$ is the [[Riemann zeta function|1XWBY4N0VT]], which extends beyond the half-plane by analytic continuation.
At $s = 2$ the series gives $\zeta(2) = \pi^2/6$, the [[Basel problem|0DMY75D6FV]].

## Explanations

### L1 human

Add up $1$, then $1/2^s$, then $1/3^s$, and so on.
For $s = 2$ this is $1 + 1/4 + 1/9 + \cdots$, which adds up to $\pi^2/6$.
For $s = 1$ the terms shrink too slowly and the sum grows without bound.
The series works exactly when the real part of $s$ is larger than $1$, and it defines the zeta function there.
