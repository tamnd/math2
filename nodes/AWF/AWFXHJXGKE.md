---
tag: AWFXHJXGKE
kind: definition
name: Lebesgue point
msc: [28A15]
defines: 19WRHM5NAT
uses: [2Z2QVWZ262, X7GTF3D98F, 0YE5868HZB]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_point
---

## Definition

Let $n \ge 1$, let $\lambda$ be [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$, and let $f \colon \R^n \to \R$ be locally [[integrable|X7GTF3D98F]].
For $x \in \R^n$ and $r > 0$, let $B(x, r)$ be the [[open ball|0YE5868HZB]] of centre $x$ and radius $r$.
A point $x \in \R^n$ is a *Lebesgue point* of $f$ if
$$\lim_{r \to 0^+} \frac{1}{\lambda(B(x, r))} \int_{B(x, r)} \abs{f(y) - f(x)} \, d\lambda(y) = 0.$$

## Remarks

Example: if $f$ is continuous at $x$, then $x$ is a Lebesgue point.
Given $\varepsilon > 0$, choose $r_0$ with $\abs{f(y) - f(x)} < \varepsilon$ on $B(x, r_0)$; then every average with $r < r_0$ is at most $\varepsilon$.

Non-example: let $n = 1$ and $f = \mathbf{1}_{[0, \infty)}$.
At $x = 0$, the integrand equals $1$ on $(-r, 0)$ and $0$ on $[0, r)$, so the average is $1/2$ for every $r$, and $0$ is not a Lebesgue point.

The set of Lebesgue points depends on the chosen function, not only on its class modulo null sets.
Changing $f$ at one point $x$ can destroy the Lebesgue point property at $x$ but at no other point.
