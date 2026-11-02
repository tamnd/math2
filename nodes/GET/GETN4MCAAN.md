---
tag: GETN4MCAAN
kind: definition
name: Fractional Laplacian
msc: [35R11, 26A33, 47G30]
defines: F8RSNQBMBE
uses: [0E0B6RA8K0, CG9JEATW3Q, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_Laplacian
---

## Definition

Let $n \ge 1$ and $0 < s < 1$.
Let $\mathcal{S}(\R^n)$ be the [[Schwartz space|CG9JEATW3Q]], and let $\hat u(\xi) = \int_{\R^n} e^{-i x \cdot \xi} u(x) \, dx$ be the [[Fourier transform|DPVM34ADZV]] of $u$.
The *fractional Laplacian* of $u \in \mathcal{S}(\R^n)$ is the function $(-\Delta)^s u$ defined by
$$\widehat{(-\Delta)^s u}(\xi) = \abs{\xi}^{2s} \hat u(\xi), \qquad \xi \in \R^n.$$

## Remarks

Equivalently, for $u \in \mathcal{S}(\R^n)$ and $x \in \R^n$,
$$(-\Delta)^s u(x) = C_{n,s} \lim_{\varepsilon \to 0^+} \int_{\abs{x - y} > \varepsilon} \frac{u(x) - u(y)}{\abs{x - y}^{n + 2s}} \, dy, \qquad C_{n,s} = \frac{4^s \, \Gamma(n/2 + s)}{\pi^{n/2} \abs{\Gamma(-s)}}.$$
The integral formula also makes sense for bounded $C^2$ functions.
Example: for $u(x) = \cos(k \cdot x)$ with $k \in \R^n$, the integral formula gives $(-\Delta)^s u = \abs{k}^{2s} u$, in agreement with the multiplier $\abs{\xi}^{2s}$.
Non-example: the exponent $s = 1$ is excluded, since the constant $C_{n,s}$ tends to $0$ as $s \to 1$ and the singular integral diverges; the multiplier $\abs{\xi}^2$ gives the ordinary operator $-\Delta$ instead.
The function $(-\Delta)^s u$ is smooth but in general not in $\mathcal{S}(\R^n)$, since $\abs{\xi}^{2s}$ is not smooth at $\xi = 0$; it decays like $\abs{x}^{-n-2s}$.
