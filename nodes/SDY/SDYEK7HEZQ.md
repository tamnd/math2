---
tag: SDYEK7HEZQ
kind: definition
name: Prolate spheroidal wave functions
msc: ["33E10", "42A38", "94A12"]
defines: QNHYXDFJJY
uses: [0BQAA2BK3Q, 0NEGN5CRSC, M2NEP1K5AE, P3T104G564]
sources:
  - url: https://en.wikipedia.org/wiki/Prolate_spheroidal_wave_function
---

## Definition

Let $c \ge 0$ be a real parameter, called the bandwidth parameter.
Consider the differential equation on $(-1, 1)$
$$\frac{d}{dx}\Big( (1 - x^2) \frac{d\psi}{dx} \Big) - c^2 x^2 \psi = -\chi \psi,$$
where $\chi$ is a real number.
There is an increasing sequence $\chi_0 < \chi_1 < \chi_2 < \cdots$ that tends to $\infty$ and has the following property.
The equation has a nonzero bounded solution on $(-1, 1)$ exactly when $\chi = \chi_m$ for some $m$.
For each $\chi_m$ this solution is unique up to a constant factor.
The *prolate spheroidal wave functions* with parameter $c$ are these solutions $\psi_0, \psi_1, \psi_2, \dots$, normalized by $\int_{-1}^1 \abs{\psi_m(x)}^2\, dx = 1$ and taken real.

## Remarks

Example: for $c = 0$ the equation is Legendre's equation $((1 - x^2)\psi')' = -\chi \psi$.
Its bounded solutions are the Legendre polynomials $P_m$ with $\chi_m = m(m + 1)$, so $\psi_m = \sqrt{(2m + 1)/2}\, P_m$; for instance $\psi_0 = 1/\sqrt{2}$ satisfies the equation with $\chi_0 = 0$.

Non-example: for $c = 0$ and $\chi = 0$, the function $\psi(x) = \frac12 \log \frac{1 + x}{1 - x}$ also solves the equation, since $(1 - x^2)\psi'(x) = 1$.
It is not bounded near $\pm 1$, so it is not a prolate spheroidal wave function.

For $c > 0$, the functions $\psi_m$ are also the [[eigenfunctions|0BQAA2BK3Q]] of the integral operator
$$Q_c \psi(x) = \int_{-1}^1 \frac{\sin c(x - y)}{\pi (x - y)}\, \psi(y)\, dy$$
on $L^2(-1, 1)$, which is [[self-adjoint|0NEGN5CRSC]], positive and [[compact|M2NEP1K5AE]].
Its eigenvalues satisfy $1 > \lambda_0 > \lambda_1 > \cdots > 0$.
The kernel of $Q_c$ is that of the projection onto functions whose Fourier transform, in the convention $\int f(t) e^{-i\omega t}\, dt$, vanishes outside $[-c, c]$.
Extending $\psi_m$ to $\R$ by the same integral, divided by $\lambda_m$, gives a [[band-limited function|P3T104G564]], and $\lambda_m$ is the fraction of its energy that lies in $[-1, 1]$.
