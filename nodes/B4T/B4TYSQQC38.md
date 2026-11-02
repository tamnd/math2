---
tag: B4TYSQQC38
kind: definition
name: Band-limited function
msc: ["94A20", "42A38", "94A12"]
defines: P3T104G564
uses: [SASP14MA1Z, DPVM34ADZV, THY12GPZ8C]
sources:
  - url: https://en.wikipedia.org/wiki/Bandlimiting
---

## Definition

Let $f \in L^2(\R)$, and let $\hat f \in L^2(\R)$ be its [[Fourier transform|DPVM34ADZV]], normalized so that $\hat f(\xi) = \int_\R f(x) e^{-2\pi i x \xi}\, dx$ for integrable $f$.
Let $B > 0$.
The function $f$ is *band-limited* with bandwidth $B$ if $\hat f(\xi) = 0$ for almost every $\xi$ with $\abs{\xi} > B$.
It is *band-limited* if it is band-limited with some bandwidth $B > 0$.

## Remarks

If $f$ is band-limited with bandwidth $B$, then $\hat f$ lies in $L^2[-B, B] \subset L^1[-B, B]$, and $f$ agrees almost everywhere with the continuous function $x \mapsto \int_{-B}^{B} \hat f(\xi) e^{2\pi i x \xi}\, d\xi$; one always uses this continuous representative.

Example: $f(x) = \sin(\pi x)/(\pi x)$, with $f(0) = 1$, lies in [[$L^2(\R)$|SASP14MA1Z]], and $\int_{-1/2}^{1/2} e^{2\pi i x \xi}\, d\xi = f(x)$.
So $\hat f$ is the indicator of $[-\frac12, \frac12]$, and $f$ is band-limited with bandwidth $\frac12$.

Non-example: $f(x) = e^{-\pi x^2}$ has $\hat f(\xi) = e^{-\pi \xi^2}$, which is positive everywhere, so $f$ is not band-limited.

By the [[Paley–Wiener theorem|THY12GPZ8C]], the band-limited functions with bandwidth $B$ are exactly the restrictions to $\R$ of certain entire functions.
These are the entire functions of exponential type at most $2\pi B$ that are square-integrable on $\R$.
In particular a nonzero band-limited function cannot vanish on an interval.
The same definition is used for tempered distributions, with the condition that the support of the distribution $\hat f$ lies in $[-B, B]$.
In this wider sense $\sin(2\pi B x)$ is band-limited, though not in $L^2$.
