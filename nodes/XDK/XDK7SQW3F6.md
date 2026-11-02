---
tag: XDK7SQW3F6
kind: definition
name: Harmonic polynomial
msc: [31B05]
defines: MVYFSYMECG
uses: [1G0B73WPX8, 0E0B6RA8K0, 2C3PAQ7H50, 3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_polynomial
---

## Definition

Let $n \ge 1$ and let $p \in \R[x_1, \dots, x_n]$ be a [[polynomial|1G0B73WPX8]] with real coefficients.
The polynomial $p$ is *harmonic* if its [[Laplacian|0E0B6RA8K0]] is the zero polynomial:
$$\Delta p = \frac{\partial^2 p}{\partial x_1^2} + \dots + \frac{\partial^2 p}{\partial x_n^2} = 0.$$

## Remarks

Example: $p(x, y, z) = x^2 + y^2 - 2z^2$ is harmonic, since $\Delta p = 2 + 2 - 4 = 0$.
Non-example: $p(x, y) = x^2 + y^2$ is not harmonic, since $\Delta p = 4$.
The Laplacian maps a [[homogeneous polynomial|2C3PAQ7H50]] of degree $k$ to one of degree $k - 2$, so a polynomial is harmonic if and only if each of its homogeneous parts is harmonic.
The homogeneous harmonic polynomials of degree $k$ in $n$ variables form a vector space $\mathcal{H}_k(\R^n)$ of dimension $\binom{n+k-1}{k} - \binom{n+k-3}{k-2}$, where the second term is $0$ for $k < 2$.
For $n = 2$ and $k \ge 1$ this dimension is $2$, with basis $\operatorname{Re}(x + iy)^k$ and $\operatorname{Im}(x + iy)^k$; for $n = 3$ it is $2k + 1$.
The restrictions of the elements of $\mathcal{H}_k(\R^n)$ to the unit sphere are the [[spherical harmonics|3F32Y21HP4]] of degree $k$.
