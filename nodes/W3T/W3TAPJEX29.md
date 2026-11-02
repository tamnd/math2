---
tag: W3TAPJEX29
kind: definition
name: Riesz transform
msc: [42B20, 44A15]
defines: FRNDFJ9WQ5
uses: [HTMCEARGDD, 0SYR10HD4R, DPVM34ADZV, CG9JEATW3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_transform
---

## Definition

Let $n \ge 1$ and $j \in \set{1, \ldots, n}$.
Let $c_n = \Gamma\big(\frac{n+1}{2}\big) / \pi^{(n+1)/2}$, where $\Gamma$ is the gamma function.
For a [[Schwartz function|CG9JEATW3Q]] $f$ on $\R^n$, the *$j$-th Riesz transform* of $f$ is the [[principal value|0SYR10HD4R]]
$$R_j f(x) = c_n \lim_{\varepsilon \to 0^+} \int_{\abs{y} > \varepsilon} \frac{y_j}{\abs{y}^{n+1}} f(x - y) \, dy.$$

## Remarks

With $\hat f(\xi) = \int f(x) e^{-2\pi i x \cdot \xi} \, dx$, the [[Fourier transform|DPVM34ADZV]] of $R_j f$ is
$$\widehat{R_j f}(\xi) = -i \frac{\xi_j}{\abs{\xi}} \hat f(\xi).$$
So $\sum_{j=1}^n R_j^2 = -I$ on $L^2(\R^n)$, and each $R_j$ is bounded on $L^2$ with norm $1$.
Each $R_j$ extends to a bounded operator on $L^p(\R^n)$ for $1 < p < \infty$.

Example: for $n = 1$, $c_1 = \Gamma(1)/\pi = 1/\pi$ and the kernel is $\frac{1}{\pi}\frac{y}{\abs{y}^2} = \frac{1}{\pi y}$.
So $R_1$ is the [[Hilbert transform|NSCEBXM7ZM]], with multiplier $-i\sgn\xi$.

Non-example: the kernel $\abs{y}^{-n}$, with the same homogeneity but without the odd factor $y_j/\abs{y}$, does not define a principal value operator.
It has no cancellation, and $\int_{\varepsilon < \abs{y} < 1} \abs{y}^{-n} \, dy$ grows like $\log(1/\varepsilon)$.

The kernel $c_n y_j/\abs{y}^{n+1}$ is odd, homogeneous of degree $-n$, and smooth away from $0$, which makes $R_j$ a [[singular integral operator|HTMCEARGDD]].
