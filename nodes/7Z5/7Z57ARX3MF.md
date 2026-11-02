---
tag: 7Z57ARX3MF
kind: definition
name: FBI transform
msc: [35A27, 44A15, 35S30]
defines: 5BW26GPS2A
uses: [X7GTF3D98F, 3T5Q9WVQX8]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier%E2%80%93Bros%E2%80%93Iagolnitzer_transform
---

## Definition

Let $n \ge 1$ and let $f \colon \R^n \to \C$ be [[integrable|X7GTF3D98F]].
The *FBI transform* of $f$ is the function on $\R^n \times (\R^n \setminus \set{0})$ given by
$$Tf(x, \xi) = \int_{\R^n} e^{i \xi \cdot (x - y) - \frac{1}{2} \abs{\xi} \abs{x - y}^2}\, f(y)\, dy.$$
The same formula, read as a pairing, defines $Tf$ for a distribution $f$ with compact support.

## Remarks

The factor $e^{-\frac12 \abs{\xi} \abs{x - y}^2}$ is a Gaussian window centred at $x$ of width of order $\abs{\xi}^{-1/2}$, and $e^{i\xi \cdot (x - y)}$ selects the frequency $\xi$.
Authors use different normalizations of the window and of the constant in front; the qualitative properties do not depend on these choices.
The main property concerns the analytic [[wave front set|3T5Q9WVQX8]].
Cut $f$ off near a point $x_0$, and let $\xi_0 \ne 0$.
Then $(x_0, \xi_0)$ lies outside the analytic wave front set of $f$ exactly when $Tf(x, \lambda \xi)$ decays like $e^{-c\lambda}$ as $\lambda \to \infty$.
Here $c > 0$ is a constant and the bound is uniform for $(x, \xi)$ near $(x_0, \xi_0)$.

Example: $n = 1$ and $f(y) = e^{-y^2/2}$.
For $\xi > 0$ the exponent is a quadratic polynomial in $y$.
The Gaussian integral gives
$$Tf(x, \xi) = \sqrt{\frac{2\pi}{1 + \xi}}\, \exp\Big( i\xi x - \frac{\xi x^2}{2} + \frac{(\xi x - i\xi)^2}{2(1 + \xi)} \Big),$$
whose modulus is $\sqrt{2\pi/(1+\xi)}\, \exp\big(-\frac{\xi (x^2 + \xi)}{2(1 + \xi)}\big)$; it decays like $e^{-\xi/2}$ as $\xi \to \infty$, as it must for a real analytic function.

Non-example: $f(y) = e^{\abs{y}^3}$ is not integrable, and the integral defining $Tf(x, \xi)$ diverges for every $(x, \xi)$, because $e^{\abs{y}^3}$ grows faster than any Gaussian decays.
