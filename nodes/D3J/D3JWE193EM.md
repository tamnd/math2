---
tag: D3JWE193EM
kind: definition
name: Kelvin functions
msc: [33C10]
defines: 77BS2B0A6Q
uses: [CZCMRDWDYW, 2ET068BZZH]
sources:
  - url: https://en.wikipedia.org/wiki/Kelvin_functions
---

## Definition

Let $\nu$ be real and let $x > 0$.
Let $J_\nu$ be the [[Bessel function of the first kind|CZCMRDWDYW]] and $K_\nu$ the [[modified Bessel function|2ET068BZZH]] of the second kind, with principal branches.
The *Kelvin functions* of order $\nu$ are the real functions $\operatorname{ber}_\nu$, $\operatorname{bei}_\nu$, $\operatorname{ker}_\nu$, $\operatorname{kei}_\nu$ on $(0, \infty)$ defined by
$$\operatorname{ber}_\nu(x) + i \operatorname{bei}_\nu(x) = J_\nu\left( x e^{3\pi i/4} \right),$$
$$\operatorname{ker}_\nu(x) + i \operatorname{kei}_\nu(x) = e^{-\nu\pi i/2}\, K_\nu\left( x e^{\pi i/4} \right).$$

## Remarks

The functions $J_\nu(x e^{3\pi i/4})$ and $K_\nu(x e^{\pi i/4})$ solve $x^2 w'' + x w' - (i x^2 + \nu^2) w = 0$, since $\left( x e^{3\pi i/4} \right)^2 = -i x^2$.
Example: for $\nu = 0$, $J_0(z) = \sum_m \frac{(-1)^m (z/2)^{2m}}{(m!)^2}$ and $(-1)^m e^{3\pi i m/2} = i^m$, so the real part keeps the terms with $m = 2k$ and gives $\operatorname{ber}_0(x) = \sum_{k \ge 0} \frac{(-1)^k (x/2)^{4k}}{((2k)!)^2}$.
The odd terms give $\operatorname{bei}_0(x) = \sum_{k \ge 0} \frac{(-1)^k (x/2)^{4k+2}}{((2k+1)!)^2}$.
A non-example: $J_0(x)$ on the real axis is not $\operatorname{ber}_0(x)$; its series has the term $-\frac{x^2}{4}$, which $\operatorname{ber}_0$ lacks, because the argument is not rotated to the ray $\arg z = \frac{3\pi}{4}$.
When $\nu = 0$ the index is usually dropped: $\operatorname{ber} = \operatorname{ber}_0$, and so on.
