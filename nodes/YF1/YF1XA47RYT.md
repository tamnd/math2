---
tag: YF1XA47RYT
kind: definition
name: Robin constant
msc: [31A15, 30C85]
defines: W3NVXBEMRQ
uses: [0R6EWFKRCF, 059TJN0NZ1, SFSRQCM3EG]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_radius
---

## Definition

Let $K$ be a [[compact set|0R6EWFKRCF]] in $\C$.
For a Borel [[probability measure|059TJN0NZ1]] $\mu$ on $K$, let
$$I(\mu) = \int_K \int_K \log \frac{1}{\abs{z - w}} \, d\mu(z) \, d\mu(w)$$
be its logarithmic [[energy|SFSRQCM3EG]], with values in $(-\infty, \infty]$.
The *Robin constant* of $K$ is
$$V(K) = \inf \set{ I(\mu) : \mu \text{ a Borel probability measure on } K },$$
with $V(K) = \infty$ when $I(\mu) = \infty$ for every such $\mu$.

## Remarks

The logarithmic capacity of $K$ is $\operatorname{cap}(K) = e^{-V(K)}$.
If $V(K) < \infty$ and $\Omega$ is the unbounded component of $\hat\C \setminus K$, the Green function of $\Omega$ with pole at infinity satisfies $g_\Omega(z, \infty) = \log \abs{z} + V(K) + o(1)$ as $z \to \infty$.

Example: let $K$ be the circle of radius $r$ centred at $0$ and let $\mu$ be normalized arc length on it.
For $\abs{z} = r$ the mean value of $\log(1/\abs{z - w})$ over the circle is $-\log r$, so $I(\mu) = -\log r$.
This $\mu$ is the minimizer, so $V(K) = -\log r$.
The Green function $\log(\abs{z}/r)$ of the outside of the circle agrees with the expansion above.

Non-example of a finite value: for $K = \set{0}$ the only probability measure is $\delta_0$, and $I(\delta_0) = \log(1/0) = \infty$, so $V(K) = \infty$.

Some authors use the opposite sign or the energy kernel $\log \abs{z - w}$, so that the Robin constant becomes $\log \operatorname{cap}(K)$.
