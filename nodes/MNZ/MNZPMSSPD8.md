---
tag: MNZPMSSPD8
kind: definition
name: Trigonometric series
msc: [42A20, 42A32]
defines: FZK2M8KGXQ
uses: [0NM626FH6Q, 07GJV36896, J3NJQ5FZJ5, G12KXDHPPS]
sources:
  - url: https://en.wikipedia.org/wiki/Trigonometric_series
---

## Definition

Let $(c_n)_{n \in \Z}$ be a sequence of complex numbers.
The *trigonometric series* with coefficients $c_n$ is the formal [[series|0NM626FH6Q]] of functions of $x \in \R$
$$\sum_{n=-\infty}^{\infty} c_n e^{inx},$$
where $e^{inx}$ is the [[complex exponential|07GJV36896]].
Its $N$-th partial sum is the [[trigonometric polynomial|J3NJQ5FZJ5]] $S_N(x) = \sum_{n=-N}^{N} c_n e^{inx}$.
The series *converges* at $x$ when $\lim_{N \to \infty} S_N(x)$ exists.

## Remarks

In real form the series is $\frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)$, with $a_n = c_n + c_{-n}$ and $b_n = i(c_n - c_{-n})$, and its partial sums are the same.
Example: $\sum_{n=1}^{\infty} \frac{\cos nx}{n^2}$ is a trigonometric series with $c_0 = 0$ and $c_n = c_{-n} = \frac{1}{2n^2}$ for $n \ge 1$; it converges at every $x$ by comparison with $\sum 1/n^2$.
Non-example: the power series $\sum_{n \ge 0} x^n$ is a series of functions, but its terms are powers of $x$ and not multiples of $e^{inx}$, so it is not a trigonometric series.
A trigonometric series is the [[Fourier series|G12KXDHPPS]] of an integrable function only for special coefficients.
For instance, $\sum_{n \ge 2} \frac{\sin nx}{\log n}$ converges at every $x$ but is not the Fourier series of a Lebesgue integrable function.
