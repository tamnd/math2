---
tag: A4TRMA5V4V
kind: statement
role: proposition
name: Multiplication formula for the Fourier transform
msc: ["42B10", "42A38"]
uses: [DPVM34ADZV, SASP14MA1Z, 0R0T1VWH5X]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform
---

## Statement

Let $n \ge 1$ and let $f, g \in L^1(\R^n)$.
Let $\hat h(\xi) = \int_{\R^n} h(x) e^{-2\pi i x \cdot \xi}\, dx$ denote the [[Fourier transform|DPVM34ADZV]] of $h \in L^1(\R^n)$.
Then
$$\int_{\R^n} \hat f(y)\, g(y)\, dy = \int_{\R^n} f(y)\, \hat g(y)\, dy,$$
and both integrals converge absolutely.

## Remarks

Both sides equal the double integral $\int\int f(x) g(y) e^{-2\pi i x \cdot y}\, dx\, dy$.
This double integral converges absolutely, with bound $\norm{f}_1 \norm{g}_1$, so [[Fubini's theorem|0R0T1VWH5X]] allows either order of integration.
Absolute convergence of each side also follows from $\abs{\hat f} \le \norm{f}_1$ and $g \in$ [[$L^1$|SASP14MA1Z]].

Example: take $n = 1$, $f = \mathbf{1}_{[-1/2, 1/2]}$ and $g(y) = e^{-\pi y^2}$, so that $\hat g = g$.
The right side is $\int_{-1/2}^{1/2} e^{-\pi y^2}\, dy$.
The left side is $\int_\R \frac{\sin \pi y}{\pi y} e^{-\pi y^2}\, dy$, and the formula says the two numbers are equal.

The formula is the basis of the definition of the Fourier transform of a tempered distribution $T$, namely $\hat T(\varphi) = T(\hat \varphi)$.
By the formula, this agrees with the transform of $f$ when $T$ is integration against $f$.

## Explanations

### L1 human

The transform can be moved from one factor to the other inside an integral of a product.
It is a symmetry of the Fourier transform with respect to the pairing $\int f g$.

### L2 human

The formula is the main tool in proofs of the Fourier inversion theorem: one pairs $\hat f$ with a Gaussian of shrinking width and moves the transform onto the Gaussian.
It is also what makes the extension of the transform to tempered distributions consistent with the integral definition.
With complex conjugates it leads to the Parseval form $\int f \bar g = \int \hat f \overline{\hat g}$ on $L^1 \cap L^2$.
