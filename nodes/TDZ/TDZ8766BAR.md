---
tag: TDZ8766BAR
kind: definition
name: Bessel function of the first kind
msc: [33C10]
defines: CZCMRDWDYW
uses: [0H5SYBSED9, 0MZB06ST2B, EAV97QH9DF]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Definition

Let $\nu$ be a complex number and let $\Gamma$ be the [[gamma function|0H5SYBSED9]], with $\frac{1}{\Gamma(w)}$ read as $0$ when $w \in \set{0, -1, -2, \dots}$.
For $z \in \C \setminus (-\infty, 0]$, with the principal branch of $\left( \frac z2 \right)^\nu$, the *Bessel function of the first kind* of order $\nu$ is
$$J_\nu(z) = \left( \frac z2 \right)^{\nu} \sum_{k = 0}^{\infty} \frac{(-1)^k}{k!\, \Gamma(k + \nu + 1)} \left( \frac z2 \right)^{2k}.$$
If $\nu = n$ is an integer, the same formula defines $J_n$ as an entire function of $z$.

## Remarks

The [[power series|0MZB06ST2B]] in $\left( \frac z2 \right)^2$ converges for all $z$, since the ratio of consecutive terms is $\frac{-(z/2)^2}{(k + 1)(k + \nu + 1)} \to 0$.
The function $J_\nu$ solves [[Bessel's equation|EAV97QH9DF]] $z^2 y'' + z y' + (z^2 - \nu^2) y = 0$.
Example: $J_{1/2}(x) = \sqrt{\frac{2}{\pi x}} \sin x$ for $x > 0$.
Check: with $\Gamma(k + \frac32) = \frac{(2k + 1)!\, \sqrt{\pi}}{4^k\, k!\, 2}$, the term $k$ equals $\left( \frac x2 \right)^{1/2} \frac{2 (-1)^k x^{2k}}{\sqrt{\pi}\, (2k + 1)!}$, and summing gives $\sqrt{\frac{2}{\pi x}} \sum_k \frac{(-1)^k x^{2k + 1}}{(2k + 1)!}$.
For a positive integer $n$ and $\nu = -n$, the terms with $k < n$ vanish, and one gets $J_{-n} = (-1)^n J_n$.
So $J_n$ and $J_{-n}$ are not independent, and a second solution is the Bessel function of the second kind.
For integer $n$, the generating function is $\exp\left( \frac z2 \left( t - \frac1t \right) \right) = \sum_{n \in \Z} J_n(z)\, t^n$ for $t \ne 0$.
Non-example: $\cos z$ is not $J_0(z)$, although both equal $1$ at $0$; their series differ already in the $z^2$ term, $-\frac{z^2}{2}$ for $\cos z$ against $-\frac{z^2}{4}$ for $J_0(z)$.
