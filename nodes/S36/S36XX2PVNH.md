---
tag: S36XX2PVNH
kind: definition
name: Fourier series
msc: [42A16, 42A20]
defines: G12KXDHPPS
uses: [089KWVYD69, 0N1JQXZXHC, 07GJV36896, 0NM626FH6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Definition

Let $f \colon \R \to \C$ be a [[periodic function|089KWVYD69]] of period $2\pi$ whose real and imaginary parts are [[Riemann integrable|0N1JQXZXHC]] on $[-\pi, \pi]$.
For each integer $n$, the $n$-th *Fourier coefficient* of $f$ is
$$\hat f(n) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} \, dx,$$
where $e^{-inx}$ is the [[complex exponential|07GJV36896]].
The *Fourier series* of $f$ is the formal [[series|0NM626FH6Q]]
$$\sum_{n = -\infty}^{\infty} \hat f(n) e^{inx},$$
whose $N$-th partial sum is $S_N f(x) = \sum_{n=-N}^{N} \hat f(n) e^{inx}$.

## Remarks

For real $f$ the series is often written $\frac{a_0}{2} + \sum_{n \ge 1} (a_n \cos nx + b_n \sin nx)$, with $a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos nx \, dx$ and $b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin nx \, dx$.
Example: let $f(x) = x$ for $-\pi < x \le \pi$, extended with period $2\pi$.
Then $a_n = 0$ since $f$ is odd, and integration by parts gives $b_n = \frac{2}{\pi} \int_0^\pi x \sin nx \, dx = \frac{2 (-1)^{n+1}}{n}$.
So the Fourier series is $2 \sum_{n \ge 1} \frac{(-1)^{n+1}}{n} \sin nx$; at $x = \pi/2$ the series converges to $\pi/2$, which is the Leibniz formula $1 - \frac{1}{3} + \frac{1}{5} - \cdots = \frac{\pi}{4}$.
Non-example: the $2\pi$-periodic function equal to $1/\abs{x}$ for $0 < \abs{x} \le \pi$ is not integrable on $[-\pi, \pi]$, so its Fourier coefficients are not defined.
The series is formal: the definition says nothing about convergence, and there are continuous functions whose Fourier series diverge at some points.
In Lebesgue theory the same formulas define the Fourier series of every integrable $2\pi$-periodic function.
