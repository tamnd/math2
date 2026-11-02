---
tag: YXJPPC9CXS
kind: definition
name: Riesz potential operator
msc: [47G40, 31B15, 45P05]
defines: 5N5DXQMVP7
uses: [SASP14MA1Z, 0H5SYBSED9, 2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_potential
---

## Definition

Let $n \ge 1$ and let $\alpha$ be a real number with $0 < \alpha < n$.
Let
$$c_\alpha = \frac{\pi^{n/2} \, 2^\alpha \, \Gamma(\alpha/2)}{\Gamma((n - \alpha)/2)},$$
where $\Gamma$ is the [[gamma function|0H5SYBSED9]].
Let $f$ be a measurable function on $\R^n$.
At each point $x \in \R^n$ where the integral converges absolutely, the *Riesz potential* of order $\alpha$ of $f$ is
$$I_\alpha f(x) = \frac{1}{c_\alpha} \int_{\R^n} \frac{f(y)}{\abs{x - y}^{n - \alpha}} \, dy.$$
The integral is taken with respect to [[Lebesgue measure|2Z2QVWZ262]].
The map $f \mapsto I_\alpha f$ is the *Riesz potential operator* $I_\alpha$.

## Remarks

If $f \in L^p(\R^n)$ with $1 \le p < n/\alpha$, then $I_\alpha f(x)$ converges absolutely for almost every $x$.
For $1 < p < n/\alpha$ and $1/q = 1/p - \alpha/n$, the [[Hardy–Littlewood–Sobolev inequality|HG65C9R1SP]] gives $\norm{I_\alpha f}_q \le A \norm{f}_p$ with $A$ depending only on $n$, $\alpha$ and $p$, see [[Lp space|SASP14MA1Z]].

With the Fourier transform $\hat f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi} \, dx$, the constant $c_\alpha$ is chosen so that $\widehat{I_\alpha f}(\xi) = (2\pi \abs{\xi})^{-\alpha} \hat f(\xi)$ for nice $f$.
So $I_\alpha = (-\Delta)^{-\alpha/2}$, the inverse of the [[fractional Laplacian|F8RSNQBMBE]], and $I_\alpha I_\beta = I_{\alpha + \beta}$ when $\alpha + \beta < n$.

Example: $n = 3$ and $\alpha = 2$.
Then $c_2 = \pi^{3/2} \cdot 4 \cdot \Gamma(1) / \Gamma(1/2) = 4\pi$, since $\Gamma(1/2) = \sqrt{\pi}$.
So $I_2 f(x) = \frac{1}{4\pi} \int_{\R^3} \frac{f(y)}{\abs{x - y}} \, dy$, the Newtonian potential, which solves $-\Delta u = f$ for smooth $f$ with compact support.

Non-example: for $f = 1$ the integral $\int_{\R^n} \abs{x - y}^{\alpha - n} \, dy$ diverges at every $x$, because $\alpha - n > -n$, so $I_\alpha 1$ is not defined.

## Explanations

### L1 human

The Riesz potential averages $f$ with a weight that is large near the point $x$ and decays like a power of the distance.
