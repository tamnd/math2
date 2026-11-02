---
tag: NEB29GSM22
kind: definition
name: Influence function
msc: [62F35, 62G35]
defines: EB2QJQNE5Z
uses: [0VGMEBVW1M, 099SXAG014, PDXR52YGPD, 0DCT0QZVQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Robust_statistics
---

## Definition

Let $\mathcal{D}$ be a convex set of [[probability distributions|0VGMEBVW1M]] on $\R$ that contains every [[point mass|099SXAG014]] $\delta_x$, and let $T \colon \mathcal{D} \to \R$ be a functional.
Let $F \in \mathcal{D}$ and $x \in \R$.
The *influence function* of $T$ at $F$ is
$$\mathrm{IF}(x; T, F) = \lim_{\varepsilon \downarrow 0} \frac{T\big((1 - \varepsilon) F + \varepsilon \delta_x\big) - T(F)}{\varepsilon},$$
defined at those $x$ where the limit exists.

## Remarks

It is the one-sided [[Gateaux derivative|PDXR52YGPD]] of $T$ at $F$ in the direction $\delta_x - F$.
The gross-error sensitivity is $\gamma^*(T, F) = \sup_x \abs{\mathrm{IF}(x; T, F)}$, and $T$ is called B-robust at $F$ when $\gamma^*$ is finite.
Under regularity conditions, $\sqrt{n}\big(T(F_n) - T(F)\big)$ is asymptotically normal with mean $0$ and variance $E_F\big[\mathrm{IF}(X; T, F)^2\big]$, where $F_n$ is the empirical distribution.

Example: the mean $T(F) = \int t \, dF(t)$, on distributions with finite mean.
Then $T((1-\varepsilon)F + \varepsilon\delta_x) = (1-\varepsilon)\mu + \varepsilon x$ with $\mu = T(F)$, so $\mathrm{IF}(x; T, F) = x - \mu$, which is unbounded.
For the median at a distribution $F$ with median $m$ and a density $f$ that is continuous and positive at $m$, $\mathrm{IF}(x; T, F) = \sgn(x - m) / (2 f(m))$ for $x \ne m$, which is bounded.

Non-example: the mean is not defined at a distribution $F$ without a finite [[expectation|0DCT0QZVQ1]], such as the Cauchy distribution.
Then $F$ lies outside $\mathcal{D}$, and the mean has no influence function at $F$.
