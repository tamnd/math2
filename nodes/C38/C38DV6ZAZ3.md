---
tag: C38DV6ZAZ3
kind: definition
name: Indeterminate moment problem
msc: [44A60]
defines: GCTN4BZ1ET
uses: [CS7TWHY7JM, H0GY2J14CA, PR11BZQQPG, 01XAHPADBA]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_problem
---

## Definition

Let $K$ be a closed subset of $\R$.
Let $\mu$ be a positive Borel [[measure|PR11BZQQPG]] on $\R$ with support in $K$, such that every [[moment|01XAHPADBA]] $m_n = \int x^n \, d\mu(x)$, $n \ge 0$, is finite.
The [[moment problem|CS7TWHY7JM]] for $\mu$ on $K$ is *indeterminate* if there is a positive Borel measure $\nu \ne \mu$ with the following properties.
The support of $\nu$ lies in $K$, and $\int x^n \, d\nu(x) = m_n$ for all $n \ge 0$.
Equivalently, it is not [[determinate|H0GY2J14CA]].

## Remarks

Example: the log-normal density $f(x) = (x \sqrt{2\pi})^{-1} e^{-(\ln x)^2/2}$ on $(0, \infty)$.
The substitution $x = e^{u}$ shows $\int_0^\infty x^n f(x) \sin(2\pi \ln x) \, dx = e^{n^2/2} \int_{\R} \frac{e^{-v^2/2}}{\sqrt{2\pi}} \sin(2\pi v) \, dv = 0$, with $v = u - n$, since the last integrand is odd.
So $\nu$ with density $f(x)(1 + \sin(2\pi \ln x))$ is a different positive measure on $[0, \infty)$ with the same moments.
Non-example: the uniform distribution on $[0, 1]$ is not indeterminate, since a measure on a compact set is determined by its moments.
Every measure with finitely many atoms is determinate, so an indeterminate measure has infinite support; its support must also be unbounded.
