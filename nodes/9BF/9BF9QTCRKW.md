---
tag: 9BF9QTCRKW
kind: statement
role: theorem
name: Mehler kernel
msc: [33C45, 42C10]
uses: [MGACY98E9H, 52VS07H6GK]
about: [MGACY98E9H]
sources:
  - url: https://en.wikipedia.org/wiki/Mehler_kernel
same_as:
  wikidata: Q6809515
  wikipedia: Mehler kernel
---

## Statement

Let $H_n$ be the (physicists') [[Hermite polynomial|MGACY98E9H]] of degree $n$.
Let $\rho \in \C$ with $\abs{\rho} < 1$, and let $x, y \in \R$.
Then (Mehler's formula)
$$\sum_{n=0}^{\infty} \frac{H_n(x) H_n(y)}{n!} \left( \frac{\rho}{2} \right)^n = \frac{1}{\sqrt{1 - \rho^2}} \exp\left( \frac{2\rho x y - \rho^2 (x^2 + y^2)}{1 - \rho^2} \right),$$
where the square root is the principal one.
The right-hand side, as a function of $(x, y)$, is the *Mehler kernel*.

## Remarks

Proof idea: insert the integral formula $H_n(x) = \frac{2^n}{\sqrt{\pi}} \int_{\R} (x + it)^n e^{-t^2} \, dt$ for both factors.
The sum over $n$ becomes an exponential, and the remaining double integral is Gaussian and can be computed in closed form.
Check at $x = y = 0$: $H_0(0) = 1$, $H_2(0) = -2$ and $H_4(0) = 12$ give $1 + \frac{\rho^2}{2} + \frac{3\rho^4}{8} + \cdots$, which is the expansion of $(1 - \rho^2)^{-1/2}$.
In terms of the [[Hermite functions|52VS07H6GK]] $\psi_n$ the formula reads
$$\sum_{n=0}^{\infty} \rho^n \psi_n(x) \psi_n(y) = \frac{1}{\sqrt{\pi (1 - \rho^2)}} \exp\left( -\frac{(1 + \rho^2)(x^2 + y^2) - 4\rho x y}{2 (1 - \rho^2)} \right).$$
So the Mehler kernel is the integral kernel of the operator that multiplies the $n$-th Hermite function by $\rho^n$.
The hypothesis $\abs{\rho} < 1$ is needed: at $\rho = 1$ the right side is undefined and the series does not converge to a function.

## Explanations

### L1 human

Mehler's formula adds up an infinite series of products of Hermite polynomials and gets a single Gaussian expression.
It is the Hermite analogue of summing a geometric series.
The resulting kernel describes how a quantum harmonic oscillator evolves in time.
It also describes a particle pulled back to the origin by a spring and shaken by noise.

### L2 human

Write $N$ for the operator with $N \psi_n = n \psi_n$, the number operator of the harmonic oscillator.
Then the Mehler kernel with $\rho = e^{-t}$, $t > 0$, is the kernel of $e^{-tN}$, a smoothing semigroup on $L^2(\R)$.
In probability, the probabilists' version of the same formula gives the transition density of the Ornstein–Uhlenbeck process.
Letting $\rho$ tend to a point $e^{-i\alpha}$ of the unit circle leads to the kernel of the fractional Fourier transform.
The formula is a model for bilinear generating functions of other orthogonal polynomials, such as the Hille–Hardy formula for Laguerre polynomials.
