---
tag: CSYZGA5YKS
kind: statement
role: theorem
name: Uniform convergence of absolutely summable Fourier series
msc: [42A20, 42A16]
uses: [5NN2YZZR3V, G12KXDHPPS, 08VZ57PT26, 0NX5NWAFC9, TPJZCSXSVN, 0X3WGX95FE]
about: [G12KXDHPPS]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_Fourier_series
---

## Statement

Let $f \colon \R \to \C$ be a [[continuous|0X3WGX95FE]] $2\pi$-periodic function whose [[Fourier coefficients|5NN2YZZR3V]] satisfy
$$\sum_{n \in \Z} \abs{\hat f(n)} < \infty.$$
Then the partial sums $S_N f(x) = \sum_{n=-N}^{N} \hat f(n) e^{inx}$ of its [[Fourier series|G12KXDHPPS]] converge to $f$ [[uniformly|08VZ57PT26]] on $\R$.

## Remarks

Since $\abs{\hat f(n) e^{inx}} = \abs{\hat f(n)}$, the [[Weierstrass M-test|0NX5NWAFC9]] shows that $S_N f$ converges uniformly to a continuous $2\pi$-periodic function $g$.
Uniform convergence allows integration term by term, so $\hat g(n) = \hat f(n)$ for all $n$.
Then $f - g$ is continuous with all Fourier coefficients zero, and its Fejér means, which converge uniformly to $f - g$ by [[Fejér's theorem|TPJZCSXSVN]], are all zero; hence $f = g$.
Example: for $f(x) = \abs{x}$ on $[-\pi, \pi]$, extended periodically, $\hat f(0) = \frac{\pi}{2}$ and $\hat f(n) = \frac{(-1)^n - 1}{\pi n^2}$ for $n \ne 0$, which is summable.
Without continuity the conclusion fails: if $f$ is only integrable with summable coefficients, the series converges uniformly to a continuous function that equals $f$ only almost everywhere.
Every $f \in C^1$ periodic satisfies the hypothesis, by the Cauchy–Schwarz inequality and Parseval's identity applied to $f'$.

## Explanations

### L1 human

If the sizes of the Fourier coefficients add up to a finite number, the Fourier series converges as nicely as possible: uniformly, to the function itself.
The finite sum of sizes bounds the error of all the tails at once.

### L2 human

This is the simplest sufficient condition for uniform convergence, and it is easy to check from decay of the coefficients, for instance $\abs{\hat f(n)} \le C \abs{n}^{-1-\delta}$ with $\delta > 0$.
The functions with summable Fourier coefficients form the [[Wiener algebra|5H8XESYCHQ]] $A(\mathbb{T})$.
Bernstein's theorem shows that Hölder continuity of order $\alpha > \frac{1}{2}$ is enough to be in $A(\mathbb{T})$.
The condition is far from necessary: there are continuous functions whose Fourier series converge uniformly but not absolutely.
