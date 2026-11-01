---
tag: TXB2F07CC6
kind: definition
name: Riemann zeta function
msc: [11M06]
defines: 1XWBY4N0VT
uses: [8MWTEF6462, 0NAHXR1FRH, 0ZZ7ZYDR8W, 0M3YQJ81NB]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_zeta_function
---

## Definition

For a complex number $s$ and an integer $n \ge 1$, let $n^{-s} = e^{-s \log n}$.
For $\operatorname{Re} s > 1$, the [[Dirichlet series|8MWTEF6462]]
$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$$
converges absolutely, and it defines a [[holomorphic function|0NAHXR1FRH]] on the half-plane $\operatorname{Re} s > 1$.
This function has a unique [[analytic continuation|0M3YQJ81NB]] to a [[meromorphic function|0ZZ7ZYDR8W]] on $\C$.
The *Riemann zeta function* is this meromorphic function $\zeta$.
Its only pole is a simple pole at $s = 1$, with residue $1$.

## Remarks

Example: $\zeta(2) = \pi^2/6$, the value of the series in the [[Basel problem|0DMY75D6FV]].
Non-example of the series form: at $s = 1$ the series is the harmonic series, which diverges, and $\zeta$ has its pole there.
At $s = 0$ or $s = -1$ the series diverges too, but $\zeta$ is defined there by continuation: $\zeta(0) = -1/2$ and $\zeta(-1) = -1/12$.
For $\operatorname{Re} s > 0$ the continuation is given by
$$\zeta(s) = \frac{s}{s - 1} - s \int_1^{\infty} \frac{x - \floor{x}}{x^{s+1}} \, dx,$$
since the integral converges there.
The [[functional equation|NFXKNDJX9C]] gives the continuation to all of $\C$.
The uniqueness of the continuation follows from the [[identity theorem|0YBVKMYX0W]].
