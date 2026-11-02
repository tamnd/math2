---
tag: 53MZ2DGDTQ
kind: statement
role: theorem
name: Weierstrass product for the gamma function
msc: [33B15, 30D10]
uses: [PY6K9AWR33, 00C5P9JZBK, RZ0Z2BTMT4]
about: [PY6K9AWR33, 0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
---

## Statement

Let $1/\Gamma$ be the [[reciprocal gamma function|PY6K9AWR33]] and let $\gamma$ be the [[Euler–Mascheroni constant|00C5P9JZBK]].
For every $z \in \C$,
$$\frac{1}{\Gamma(z)} = z \, e^{\gamma z} \prod_{n=1}^{\infty} \left(1 + \frac{z}{n}\right) e^{-z/n}.$$
The [[infinite product|RZ0Z2BTMT4]] converges absolutely and uniformly on every compact subset of $\C$.

## Remarks

Each factor is $1 + O(z^2/n^2)$, and $\sum 1/n^2 < \infty$ gives the convergence.
The partial product up to $n$ equals $\frac{z(z+1)\cdots(z+n)}{n!}\, e^{z(\gamma - H_n)}$, where $H_n$ is the [[harmonic number|0NANDX7V02]].
Since $H_n - \ln n \to \gamma$, this is the reciprocal of the quotient in the [[Euler–Gauss limit formula|SKRP9NDXR4]] times a factor tending to $1$, which proves the identity.
The product exhibits the simple zeros of $1/\Gamma$ at $0, -1, -2, \ldots$; it is the [[Weierstrass factorization|11VC51YHQJ]] of this entire function of order $1$.
Multiplying the products for $1/\Gamma(z)$ and $1/\Gamma(-z)$ and using [[Euler's sine product|DQEHD56649]] gives $\Gamma(z)\Gamma(-z) = -\pi/(z\sin \pi z)$, a form of the reflection formula.

## Explanations

### L1 human

The reciprocal of the gamma function can be written as an infinite product, much like a polynomial is a product of factors for its roots.
Here the roots are $0, -1, -2, \ldots$, and the exponential factors are there to make the infinite product converge.

### L2 human

Taking the logarithmic derivative of the product gives the series $\psi(z) = -\gamma - \frac1z + \sum_{n \ge 1}\left(\frac1n - \frac{1}{z+n}\right)$ for the [[digamma function|HWRRXB0YXS]].
Differentiating once more gives $(\ln\Gamma)''(x) = \sum_{n \ge 0} (x+n)^{-2} > 0$ on $(0, \infty)$, so $\ln \Gamma$ is convex there.
The product also yields the Taylor expansion of $\ln\Gamma(1 + z)$ around $0$, whose coefficients are values of the [[Riemann zeta function|1XWBY4N0VT]] at the integers $k \ge 2$.
