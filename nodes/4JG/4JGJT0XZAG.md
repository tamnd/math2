---
tag: 4JGJT0XZAG
kind: definition
name: Wigner quasiprobability distribution
msc: [81S30, 81P16]
defines: 563Y1P5HR8
uses: [V1JTB52E8C, RFNGJ09WDR, FCHW5QGG5V]
sources:
  - url: https://en.wikipedia.org/wiki/Wigner_quasiprobability_distribution
---

## Definition

Let $n \ge 1$ and $\hbar > 0$.
Let $\rho$ be a [[density operator|V1JTB52E8C]] on $L^2(\R^n)$, that is, a positive trace-class operator of trace $1$, and let $\rho(x, x')$ be its integral kernel.
The *Wigner quasiprobability distribution* of $\rho$ is the function $W_\rho$ on $\R^n \times \R^n$ given by
$$W_\rho(x, p) = \frac{1}{(2\pi\hbar)^n} \int_{\R^n} \rho\!\left(x + \tfrac{y}{2},\, x - \tfrac{y}{2}\right) e^{-i p \cdot y / \hbar}\, dy.$$
For a pure state $\rho = \psi \ip{\psi}{\cdot}$ with $\norm{\psi} = 1$, the kernel is $\psi(x)\overline{\psi(x')}$, and
$$W_\psi(x, p) = \frac{1}{(2\pi\hbar)^n} \int_{\R^n} \psi\!\left(x + \tfrac{y}{2}\right) \overline{\psi\!\left(x - \tfrac{y}{2}\right)} e^{-i p \cdot y / \hbar}\, dy.$$

## Remarks

$W_\rho$ is real-valued, and $\abs{W_\psi(x, p)} \le (\pi\hbar)^{-n}$ by the Cauchy–Schwarz inequality.
For a mixed state $\rho = \sum_k \lambda_k \psi_k \ip{\psi_k}{\cdot}$ with orthonormal $\psi_k$, $\lambda_k \ge 0$ and $\sum_k \lambda_k = 1$, one has $W_\rho = \sum_k \lambda_k W_{\psi_k}$.
For nice $\psi$ the marginals are $\int W_\psi(x, p)\, dp = \abs{\psi(x)}^2$ and $\int W_\psi(x, p)\, dx = \abs{\hat\psi(p)}^2$, where $\hat\psi$ is the unitary Fourier transform with the factor $\hbar$.
For a symbol $a$ with [[Weyl quantization|RFNGJ09WDR]] $A = \mathrm{Op}^w(a)$, under suitable integrability conditions, $\operatorname{tr}(\rho A) = \int_{\R^{2n}} a(x, p)\, W_\rho(x, p)\, dx\, dp$.
Up to the factor $(2\pi\hbar)^{-n}$, $W_\rho$ is the Weyl symbol of $\rho$.
Without the physical constants, $W_\psi$ is the [[Wigner distribution function|FCHW5QGG5V]] of time–frequency analysis.

Example: for $n = 1$ and the oscillator ground state $\psi(x) = (m\omega/\pi\hbar)^{1/4} e^{-m\omega x^2/2\hbar}$, one has $\psi(x + y/2)\psi(x - y/2) = (m\omega/\pi\hbar)^{1/2} e^{-m\omega x^2/\hbar} e^{-m\omega y^2/4\hbar}$.
The Gaussian integral in $y$ then gives
$$W_\psi(x, p) = \frac{1}{\pi\hbar} \exp\!\left(-\frac{m\omega x^2}{\hbar} - \frac{p^2}{m\omega\hbar}\right),$$
a positive Gaussian of total integral $1$.

Non-example of positivity: for the first excited state of the same oscillator, $W(0, 0) = -1/(\pi\hbar) < 0$, so a Wigner function need not be a probability density.
