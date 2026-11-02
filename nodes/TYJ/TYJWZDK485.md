---
tag: TYJWZDK485
kind: example
name: Basel problem via Fourier series
msc: [42A16, 40A05]
illustrates: [3DGHC142FT]
uses: [0DMY75D6FV, G12KXDHPPS, 3DGHC142FT]
sources:
  - url: https://en.wikipedia.org/wiki/Basel_problem
---

## Example

Let $f$ be the $2\pi$-periodic function with $f(x) = x$ for $-\pi < x \le \pi$.
Its [[Fourier series|G12KXDHPPS]] is $2 \sum_{n \ge 1} \frac{(-1)^{n+1}}{n} \sin nx$: indeed $f$ is odd, so the cosine coefficients vanish, and integration by parts gives
$$b_n = \frac{2}{\pi} \int_0^\pi x \sin nx \, dx = \frac{2(-1)^{n+1}}{n}.$$
In complex form, $\hat f(0) = 0$ and $\abs{\hat f(n)} = \frac{1}{\abs{n}}$ for $n \ne 0$.
Parseval's identity, from the [[L2 convergence of Fourier series|3DGHC142FT]], gives
$$\frac{1}{2\pi} \int_{-\pi}^{\pi} x^2 \, dx = \sum_{n \ne 0} \frac{1}{n^2}, \qquad \text{that is} \qquad \frac{\pi^2}{3} = 2 \sum_{n=1}^{\infty} \frac{1}{n^2}.$$
So $\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$, which is the [[Basel problem|0DMY75D6FV]].

## Remarks

A second route uses the pointwise convergence of a Fourier series instead of Parseval.
The $2\pi$-periodic function equal to $x^2$ on $[-\pi, \pi]$ is continuous and piecewise smooth, and its Fourier series $\frac{\pi^2}{3} + 4 \sum_{n \ge 1} \frac{(-1)^n}{n^2} \cos nx$ converges to it everywhere.
At $x = \pi$ this gives $\pi^2 = \frac{\pi^2}{3} + 4 \sum_{n \ge 1} \frac{1}{n^2}$, the same value.
Parseval applied to $x^2$ gives $\sum_{n \ge 1} \frac{1}{n^4} = \frac{\pi^4}{90}$ in the same way.

## Explanations

### L1 human

The energy of the function $x$ on one period can be computed in two ways: directly, or as the sum of the energies of its waves.
The waves of $x$ have amplitudes $1/n$, so their energies are $1/n^2$.
Comparing the two answers forces the sum $1 + \frac{1}{4} + \frac{1}{9} + \cdots$ to equal $\frac{\pi^2}{6}$.
