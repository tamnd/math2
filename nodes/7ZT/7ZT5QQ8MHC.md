---
tag: 7ZT5QQ8MHC
kind: definition
name: Circulation
msc: [76A02, 76B47]
defines: BTHH4Y71QR
uses: [0H5MR9B6GT, 0299VCW1TH, B3SXT9TWFA, 0AKRKVHW94]
sources:
  - url: https://en.wikipedia.org/wiki/Circulation_(physics)
---

## Definition

Let $\Omega \subseteq \R^n$ be open, with $n = 2$ or $n = 3$, and let $\mathbf{u} \colon \Omega \to \R^n$ be a continuous velocity field.
Let $C$ be a closed, oriented, piecewise continuously differentiable curve in $\Omega$.
The *circulation* of $\mathbf{u}$ around $C$ is the [[line integral|0H5MR9B6GT]]
$$\Gamma_C = \oint_C \mathbf{u} \cdot d\mathbf{l} = \int_a^b \mathbf{u}(\gamma(s)) \cdot \gamma'(s) \, ds,$$
where $\gamma \colon [a, b] \to \Omega$ is a parametrisation of $C$ with $\gamma(a) = \gamma(b)$.

## Remarks

If $\mathbf{u}$ is continuously differentiable and $C$ bounds an oriented surface $S$ in $\Omega$, then [[Stokes' theorem|0AKRKVHW94]] gives $\Gamma_C = \iint_S \boldsymbol{\omega} \cdot \mathbf{n} \, dA$, where $\boldsymbol{\omega}$ is the [[vorticity|B3SXT9TWFA]].
Example: for $\mathbf{u} = (-y, x)$ and the unit circle $\gamma(s) = (\cos s, \sin s)$, $0 \le s \le 2\pi$, the integrand is $\sin^2 s + \cos^2 s = 1$, so $\Gamma = 2\pi$; this equals the vorticity $2$ times the area $\pi$.
Non-example: for the uniform field $\mathbf{u} = (1, 0)$, the integral along the upper half of the circle is $-2$.
This is not a circulation, because the curve is not closed; around the full circle the circulation is $0$.
Reversing the orientation of $C$ changes the sign of $\Gamma_C$.
