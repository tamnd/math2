---
tag: 81AQ28RQDP
kind: definition
name: Weierstrass transform
msc: [44A15, 35K05]
defines: 5HYB6DDZH8
uses: [VP2HN86VAG, KD404MF042, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_transform
---

## Definition

Let $f \colon \R \to \C$ be measurable with $\int_\R \abs{f(y)}\, e^{-c y^2}\, dy < \infty$ for every $c > 0$.
The *Weierstrass transform* of $f$ is the function $Wf \colon \R \to \C$ given by
$$(Wf)(x) = \frac{1}{\sqrt{4\pi}} \int_\R f(y)\, e^{-(x - y)^2/4}\, dy.$$

## Remarks

The kernel $\frac{1}{\sqrt{4\pi}} e^{-u^2/4}$ is the density of the [[normal distribution|05AQE0QR0D]] with mean $0$ and variance $2$.
So $Wf(x) = \mathbb{E}[f(x + Y)]$ for a random variable $Y$ with that law.
It is the [[heat kernel|KD404MF042]] $\frac{1}{\sqrt{4\pi t}} e^{-u^2/(4t)}$ at $t = 1$, so $Wf = u(\cdot, 1)$ where $u$ solves the [[heat equation|VP2HN86VAG]] $u_t = u_{xx}$ with $u(\cdot, 0) = f$.
For integrable $f$ and $\hat f(\xi) = \int f(x) e^{-i x \xi}\, dx$, one has $\widehat{Wf}(\xi) = e^{-\xi^2} \hat f(\xi)$.
The growth condition can be weakened to $\int \abs{f(y)} e^{-c y^2}\, dy < \infty$ for one $c < \frac14$, which is enough for the integral to converge for every $x$.

Example: $f(x) = x^2$.
With $Y$ of mean $0$ and variance $2$, $Wf(x) = \mathbb{E}[(x + Y)^2] = x^2 + 2x\, \mathbb{E}[Y] + \mathbb{E}[Y^2] = x^2 + 2$.
Likewise $W[e^{a x}](x) = e^{a x} \mathbb{E}[e^{aY}] = e^{a^2} e^{a x}$ for every real $a$.

Non-example: $f(x) = e^{x^2/4}$ fails the condition for $c < \frac14$, and indeed $\int_\R e^{y^2/4} e^{-(x-y)^2/4}\, dy = e^{-x^2/4} \int_\R e^{x y/2}\, dy$ diverges for every $x$.
