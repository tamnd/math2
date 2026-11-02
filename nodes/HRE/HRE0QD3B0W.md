---
tag: HRE0QD3B0W
kind: definition
name: Determinate moment problem
msc: [44A60]
defines: H0GY2J14CA
uses: [CS7TWHY7JM, PR11BZQQPG, 01XAHPADBA]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_problem
---

## Definition

Let $K$ be a closed subset of $\R$.
Let $\mu$ be a positive Borel [[measure|PR11BZQQPG]] on $\R$ with support in $K$, such that every [[moment|01XAHPADBA]] $m_n = \int x^n \, d\mu(x)$, $n \ge 0$, is finite.
The [[moment problem|CS7TWHY7JM]] for $\mu$ on $K$ is *determinate* if the following holds.
Every positive Borel measure $\nu$ with support in $K$ and $\int x^n \, d\nu(x) = m_n$ for all $n \ge 0$ equals $\mu$.

## Remarks

Example: the standard normal distribution is determinate on $K = \R$.
Its moments are $m_{2n} = (2n - 1)!! \le (2n)^n$ and $m_{2n+1} = 0$, so $\sum_n m_{2n}^{-1/(2n)}$ diverges, and Carleman's condition applies.
Example: every measure with support in a compact set $K$ is determinate on $K$, by the density of polynomials in $C(K)$.
Non-example: the log-normal distribution with density $f(x) = (x \sqrt{2\pi})^{-1} e^{-(\ln x)^2/2}$ on $(0, \infty)$ is not determinate, since $f(x)(1 + \sin(2\pi \ln x))$ is a different density with the same moments.
Determinacy depends on $K$: a measure on $[0, \infty)$ can be determinate among measures on $[0, \infty)$ (Stieltjes determinate) but not among measures on $\R$ (Hamburger determinate).
