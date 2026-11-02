---
tag: CAEZVHVJJD
kind: definition
name: Nonharmonic Fourier series
msc: [42C30, 42A65, 42C15]
defines: TKNA7PR99K
uses: [SASP14MA1Z, G12KXDHPPS, ZYDYD7FB1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_sequence
---

## Definition

Let $A > 0$ and let $\Lambda = (\lambda_n)_{n \in \Z}$ be a sequence of distinct complex numbers.
For $n \in \Z$ let $e_n(t) = e^{i \lambda_n t}$, a function in the [[Lebesgue space|SASP14MA1Z]] $L^2(-A, A)$.
A *nonharmonic Fourier series* with frequencies $\Lambda$ is a series
$$\sum_{n \in \Z} c_n \, e^{i \lambda_n t}, \quad t \in (-A, A),$$
with complex coefficients $c_n$, considered with convergence in $L^2(-A, A)$.

## Remarks

When $A = \pi$ and $\lambda_n = n$, this is an ordinary [[Fourier series|G12KXDHPPS]], and the $e_n / \sqrt{2\pi}$ form an orthonormal basis.
In general the $e_n$ are not orthogonal, and the theory asks which sequences $\Lambda$ make $(e_n)$ complete, a [[Riesz basis|ZYDYD7FB1Z]] or a frame of $L^2(-A, A)$.
When $(e_n)$ is a Riesz basis, every $f \in L^2(-A, A)$ has a unique expansion $f = \sum c_n e_n$, and $\sum \abs{c_n}^2$ is comparable to $\norm{f}^2_{L^2}$.

Example: let $A = \pi$ and $\lambda_n = n + \delta_n$ with real $\delta_n$ and $\sup_n \abs{\delta_n} < 1/4$.
By Kadec's $1/4$ theorem, $(e^{i\lambda_n t})$ is a Riesz basis of $L^2(-\pi, \pi)$, so every function in $L^2(-\pi, \pi)$ is the sum of a unique nonharmonic Fourier series with these frequencies.
The constant $1/4$ cannot be replaced by a larger number.

Non-example: let $A = \pi$ and $\lambda_n = 2n$.
The functions $e^{2int}$ all have period $\pi$, so they cannot represent $f = 1_{(0, \pi)}$, which is not $\pi$-periodic on $(-\pi, \pi)$.
So the closed span of $(e_n)$ is not all of $L^2(-\pi, \pi)$ and the system is not complete.
