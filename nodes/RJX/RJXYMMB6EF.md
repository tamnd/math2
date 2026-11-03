---
tag: RJXYMMB6EF
kind: definition
name: Hubbard–Stratonovich transformation
msc: [82B05, 81S40]
defines: 1J2YM04YYY
uses: [0DFT1GP1JP, 0KX66CZMBB, A6GX2K5YFB, 9G7K8DBT9Y]
sources:
  - url: https://en.wikipedia.org/wiki/Hubbard%E2%80%93Stratonovich_transformation
---

## Definition

Let $N \ge 1$ and let $A$ be a real symmetric [[positive definite matrix|0KX66CZMBB]] of size $N \times N$.
The *Hubbard–Stratonovich transformation* is the following identity for $x \in \R^N$.
$$\exp\Big(\frac12 x^{T} A x\Big) = \frac{1}{\sqrt{\det(2 \pi A)}} \int_{\R^N} \exp\Big( -\frac12 y^{T} A^{-1} y + x^{T} y \Big) \, dy.$$
It is used to replace the left side, which is quadratic in $x$, by the right side, which is linear in $x$ inside the integral.
For $N = 1$ and $a > 0$ it reads $e^{a x^2 / 2} = (2 \pi a)^{-1/2} \int_\R e^{-y^2/(2a) + x y} \, dy$.

## Remarks

The identity is the [[Gaussian integral|0DFT1GP1JP]] $\int_{\R^N} e^{-\frac12 y^T B y + x^T y} \, dy = (2\pi)^{N/2} (\det B)^{-1/2} e^{\frac12 x^T B^{-1} x}$ with $B = A^{-1}$, which is proved by completing the square.
Example: the [[Curie–Weiss model|A6GX2K5YFB]] with $N$ spins $\sigma_i = \pm 1$ and $M = \sum_i \sigma_i$ has partition function $Z = \sum_\sigma e^{\beta M^2/(2N)}$.
With $a = \beta / N$, the identity and $\sum_\sigma e^{y M} = (2\cosh y)^N$ give
$$Z = \sqrt{\frac{N}{2 \pi \beta}} \int_\R \exp\Big( N \Big[ -\frac{y^2}{2\beta} + \ln(2 \cosh y) \Big] \Big) dy.$$
By [[Laplace's method|9G7K8DBT9Y]] the integral is dominated by the maximum, where $y/\beta = \tanh y$; with $y = \beta m$ this is the mean-field equation $m = \tanh(\beta m)$.
Non-example: if $A$ is not positive definite, the right side is undefined or the integral diverges; a negative quadratic form $e^{-a x^2/2}$ is instead written with an imaginary coupling, $e^{-a x^2/2} = (2\pi a)^{-1/2} \int_\R e^{-y^2/(2a) + i x y} \, dy$.

## Explanations

### L1 human

The formula trades a square in the exponent for a Gaussian average of a linear exponent.
In physics $x$ is made of many spins or fermion operators, and $y$ becomes an auxiliary field.
