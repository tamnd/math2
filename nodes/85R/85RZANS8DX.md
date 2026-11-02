---
tag: 85RZANS8DX
kind: definition
name: Hermite functions
msc: [33C45, 42C10, 81Q05]
defines: 52VS07H6GK
uses: [MGACY98E9H, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Hermite_polynomials
---

## Definition

Let $H_n$ be the (physicists') [[Hermite polynomial|MGACY98E9H]] of degree $n \ge 0$.
The *Hermite function* of degree $n$ is the function $\psi_n \colon \R \to \R$ given by
$$\psi_n(x) = \left( 2^n \, n! \, \sqrt{\pi} \right)^{-1/2} H_n(x) \, e^{-x^2/2}.$$

## Remarks

Example: $\psi_0(x) = \pi^{-1/4} e^{-x^2/2}$, and $\int_{\R} \psi_0(x)^2 \, dx = \pi^{-1/2} \int_{\R} e^{-x^2} \, dx = 1$.
The orthogonality of the Hermite polynomials for the weight $e^{-x^2}$ gives $\int_{\R} \psi_m \psi_n \, dx = \delta_{mn}$.
The family $(\psi_n)_{n \ge 0}$ is complete, so it is an orthonormal basis of [[$L^2(\R)$|SASP14MA1Z]].
Each $\psi_n$ solves $-\psi_n'' + x^2 \psi_n = (2n + 1) \psi_n$.
With the Fourier transform $\hat{f}(\xi) = (2\pi)^{-1/2} \int_{\R} f(x) e^{-i x \xi} \, dx$, one has $\hat{\psi}_n = (-i)^n \psi_n$.
Non-example: the polynomial $H_0 = 1$ without the Gaussian factor is not square integrable on $\R$, so it is not an element of $L^2(\R)$ at all.
