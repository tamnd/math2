---
tag: AJPKH8XY3G
kind: definition
name: Aliasing
msc: [94A20, 94A12, 42A38]
defines: FEC9RG38X9
uses: [DPVM34ADZV, P3T104G564, BMXDMHRXBG]
sources:
  - url: https://en.wikipedia.org/wiki/Aliasing
---

## Definition

Let $T > 0$ be a sampling period and let $f_s = 1/T$ be the sampling rate.

1. Two frequencies $\xi, \eta \in \R$ are *aliases* of each other at rate $f_s$ if $\xi - \eta \in f_s \Z$. Then $e^{2\pi i \xi n T} = e^{2\pi i \eta n T}$ for every $n \in \Z$.
2. Let $f \in L^2(\R)$ have [[Fourier transform|DPVM34ADZV]] $\hat f$, and let $S = \set{\xi \in \R : \hat f(\xi) \ne 0}$. Sampling $f$ at rate $f_s$ *causes aliasing* if, for some $k \in \Z$ with $k \ne 0$, the set $S \cap (S + k f_s)$ has positive Lebesgue measure.

## Remarks

Under mild conditions, the samples $f(nT)$ determine only the periodized spectrum $\sum_{k \in \Z} \hat f(\xi - k f_s)$, by the Poisson summation formula.
Clause 2 says that two of the shifted copies of $\hat f$ overlap, so that $\hat f$ cannot in general be read off from this sum.

Example: $\cos(2\pi \cdot 7 t)$ sampled at $f_s = 10$ gives $\cos(2\pi \cdot 7n/10) = \cos(2\pi n - 2\pi \cdot 3n/10) = \cos(2\pi \cdot 3n/10)$.
So the frequency $7$ is an alias of $-3$, and the samples are those of a $3$ hertz cosine.

Non-example: if $f$ is [[band-limited|P3T104G564]] with $\hat f = 0$ outside $[-B, B]$ and $f_s > 2B$, then $S \subseteq [-B, B]$ and $S + k f_s$ lies outside $[-B, B]$ for $k \ne 0$.
So clause 2 fails and there is no aliasing; this is the setting of the [[sampling theorem|BMXDMHRXBG]].
