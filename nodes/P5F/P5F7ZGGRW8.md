---
tag: P5F7ZGGRW8
kind: definition
name: Mellin convolution
msc: [44A35, 44A15]
defines: A2PMJG7J68
uses: [X7GTF3D98F, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Definition

Let $f, g \colon (0, \infty) \to \C$ be measurable.
Let $x > 0$ be such that $y \mapsto f(x/y) g(y) / y$ is [[integrable|X7GTF3D98F]] on $(0, \infty)$.
The *Mellin convolution* of $f$ and $g$ at $x$ is the [[Lebesgue integral|DWJF7ABPR1]]
$$(f \star g)(x) = \int_0^\infty f\left(\frac{x}{y}\right) g(y) \, \frac{dy}{y}.$$

## Remarks

The substitution $y \mapsto x/y$ shows that $f \star g = g \star f$.
Assume that $f$ and $g$ are both Mellin convergent at $s$.
Then $f \star g$ is defined at almost every $x > 0$, it is Mellin convergent at $s$, and $\mathcal{M}(f \star g)(s) = \mathcal{M}f(s) \, \mathcal{M}g(s)$.
The proof is Fubini's theorem and the substitution $x = yu$, which splits the double integral.
Example: $f = g = \mathbf{1}_{(0, 1]}$.
The integrand $\mathbf{1}_{(0,1]}(x/y) \mathbf{1}_{(0,1]}(y) / y$ is $1/y$ for $x \le y \le 1$ and $0$ otherwise, which is integrable for each $x > 0$.
So $(f \star g)(x) = \int_x^1 dy/y = -\log x$ for $0 < x \le 1$ and $0$ for $x > 1$.
As a check, $\int_0^1 x^{s-1} (-\log x) \, dx = 1/s^2 = (1/s)^2$ for $\operatorname{Re} s > 0$.
Non-example: $f = g = 1$ on $(0, \infty)$; the integrand $1/y$ is not integrable on $(0, \infty)$, so $(f \star g)(x)$ is defined at no $x$.
Some authors use the other normalization $\int_0^\infty f(xy) g(y) \, dy$, whose Mellin transform is $\mathcal{M}f(s) \mathcal{M}g(1 - s)$.
