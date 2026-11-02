---
tag: TAJTC44XC9
kind: definition
name: Fractional integration
msc: [42B20, 31B15, 26A33]
defines: P1VFBJV1VN
uses: [DWJF7ABPR1, 2Z2QVWZ262, SASP14MA1Z, 0H5SYBSED9, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_potential
---

## Definition

Let $n \ge 1$ and let $0 < \alpha < n$.
Let $\Gamma$ be the [[gamma function|0H5SYBSED9]] and let
$$\gamma(\alpha) = \frac{\pi^{n/2} \, 2^\alpha \, \Gamma(\alpha/2)}{\Gamma((n - \alpha)/2)}.$$
Let $f$ be a measurable function on $\R^n$.
Its *fractional integral*, or *Riesz potential*, of order $\alpha$ is
$$I_\alpha f(x) = \frac{1}{\gamma(\alpha)} \int_{\R^n} \frac{f(y)}{\abs{x - y}^{n - \alpha}} \, dy,$$
at each point $x \in \R^n$ where the [[Lebesgue integral|DWJF7ABPR1]] converges absolutely.
The integral is with respect to [[Lebesgue measure|2Z2QVWZ262]].

## Remarks

If $f \in L^p(\R^n)$, an element of the [[Lp space|SASP14MA1Z]], with $1 \le p < n/\alpha$, the integral converges absolutely for almost every $x$.
With the [[Fourier transform|DPVM34ADZV]] $\hat f(\xi) = \int f(x) e^{-2\pi i x \cdot \xi} \, dx$, the constant $\gamma(\alpha)$ is chosen so that $\widehat{I_\alpha f}(\xi) = (2\pi\abs{\xi})^{-\alpha} \hat f(\xi)$, for example for Schwartz functions $f$.
In this sense $I_\alpha = (-\Delta)^{-\alpha/2}$, and $I_\alpha I_\beta = I_{\alpha + \beta}$ when $\alpha + \beta < n$.

Example: $n = 3$ and $\alpha = 2$.
Then $\gamma(2) = \pi^{3/2} \cdot 4 \cdot \Gamma(1)/\Gamma(1/2) = 4\pi$, since $\Gamma(1/2) = \sqrt{\pi}$.
So $I_2 f(x) = \frac{1}{4\pi}\int_{\R^3} \frac{f(y)}{\abs{x - y}} \, dy$ is the Newtonian potential, and $-\Delta I_2 f = f$ for smooth $f$ with compact support.

Non-example: the order $\alpha = n$ fails the condition $0 < \alpha < n$.
Then the kernel $\abs{x - y}^{0}$ is the constant $1$, so the formula gives $\int_{\R^n} f(y) \, dy$, which does not depend on $x$ and smooths nothing.
Also $\Gamma((n - \alpha)/2) = \Gamma(0)$ is undefined, so the normalization breaks down.
