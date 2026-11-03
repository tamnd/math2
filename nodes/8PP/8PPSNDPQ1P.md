---
tag: 8PPSNDPQ1P
kind: definition
name: Born approximation
msc: [78A45, 81U05, 35P25]
defines: 3Y0VBDXHJD
uses: [MNXKTXJ35G, 8KJCN49V64, 2PCVRG9NBN, 8BQYB8H5CT]
sources:
  - url: https://en.wikipedia.org/wiki/Born_approximation
---

## Definition

Let $k > 0$ be a wavenumber and let $m \colon \R^3 \to \C$ be a bounded function with compact support, the contrast of the scatterer.
Let $u_i$ solve the [[Helmholtz equation|MNXKTXJ35G]] $\Delta u_i + k^2 u_i = 0$ on $\R^3$; this is the incident field.
The total field $u$ solves $\Delta u + k^2 (1 + m) u = 0$, and $u - u_i$ is outgoing.
Let $G(x) = \dfrac{e^{ik\abs{x}}}{4\pi \abs{x}}$ be the outgoing fundamental solution of $-(\Delta + k^2)$.
Then $u$ solves the Lippmann–Schwinger equation, an [[integral equation of the second kind|8KJCN49V64]]:
$$u(x) = u_i(x) + k^2 \int_{\R^3} G(x - y) \, m(y) \, u(y) \, dy.$$
The *Born approximation* (first Born approximation) of $u$ is the field obtained by putting $u_i$ in place of $u$ under the integral:
$$u_B(x) = u_i(x) + k^2 \int_{\R^3} G(x - y) \, m(y) \, u_i(y) \, dy.$$

## Remarks

For a plane wave $u_i(x) = e^{ik \hat{d} \cdot x}$, the far field of $u_B - u_i$ is $f_B(\hat{x}) e^{ikr}/r$ with
$$f_B(\hat{x}) = \frac{k^2}{4\pi} \int_{\R^3} e^{-ik(\hat{x} - \hat{d}) \cdot y} \, m(y) \, dy.$$
So $f_B$ is, up to a factor, the Fourier transform of $m$ at the momentum transfer $k(\hat{x} - \hat{d})$.

Example: let $m = \varepsilon \chi_B$, where $\chi_B$ is the indicator of a ball $B$ and $\varepsilon$ is small.
Then $u_B$ is given by the formula above, and $u - u_B = O(\varepsilon^2)$ as $\varepsilon \to 0$ for fixed $k$ and $B$.
Check: the Lippmann–Schwinger operator $T w = k^2 G * (m w)$ has norm $O(\varepsilon)$ on bounded continuous functions on $B$, so $u = \sum_{j \ge 0} T^j u_i$ and $u - u_B = \sum_{j \ge 2} T^j u_i$.

Non-example: the exact field $u$ is in general not the Born approximation, since $u - u_B = \sum_{j \ge 2} T^j u_i$ need not vanish.
Consider a strong scatterer, such as a ball with $k^2 \abs{m}$ times the squared radius of order $1$ or more.
Then the terms $T^j u_i$ need not decrease, and $u_B$ can be far from $u$.

The iterates $u_i + T u_i + \cdots + T^n u_i$ are the higher Born approximations, and the full sum is the [[Born series|2PCVRG9NBN]].
