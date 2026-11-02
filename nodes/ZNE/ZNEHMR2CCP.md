---
tag: ZNEHMR2CCP
kind: statement
role: proposition
name: Fourier transform of the Gaussian
msc: ["42B10", "42A38"]
uses: [DPVM34ADZV, HHNR31W3WD]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_function
---

## Statement

Let $n \ge 1$ and $a > 0$, and let $f(x) = e^{-\pi a \abs{x}^2}$ for $x \in \R^n$.
Let $\hat f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi}\, dx$ be its [[Fourier transform|DPVM34ADZV]].
Then
$$\hat f(\xi) = a^{-n/2}\, e^{-\pi \abs{\xi}^2 / a} \quad \text{for every } \xi \in \R^n.$$
In particular, for $a = 1$ the function $e^{-\pi \abs{x}^2}$ is its own Fourier transform.

## Remarks

Since $e^{-\pi a \abs{x}^2} = \prod_j e^{-\pi a x_j^2}$, the integral splits into $n$ one-dimensional integrals, so it suffices to take $n = 1$.
For $n = 1$ and $a = 1$, put $g = \hat f$.
By the [[rules for differentiation and multiplication|HHNR31W3WD]], the identity $f'(x) = -2\pi x f(x)$ becomes $g'(\xi) = -2\pi \xi g(\xi)$.
So $g(\xi) = g(0) e^{-\pi \xi^2}$, and $g(0) = \int_\R e^{-\pi x^2}\, dx = 1$ is the Gaussian integral.
The case of general $a$ follows by the change of variables $x \mapsto x / \sqrt{a}$.

The statement shows a trade-off: a narrow Gaussian (large $a$) has a wide transform (variance proportional to $a$).
For every $a > 0$ the product of the two widths is as small as possible, so every Gaussian is an equality case of the Heisenberg inequality.

## Explanations

### L1 human

The bell curve keeps its shape under the Fourier transform.
Squeezing the bell in space spreads it out in frequency by the same factor, and the reverse.
The standard bell $e^{-\pi x^2}$ is exactly fixed.

### L2 human

This computation is the base case for many proofs.
The Fourier inversion theorem, the Plancherel theorem and the solution of the heat equation all use the Gaussian as an approximate identity whose transform is known.
It also gives the characteristic function of the normal distribution after the change of variables $\xi = -t / (2\pi)$.
Gaussians are the extremal functions in the Babenko–Beckner and the Heisenberg inequalities.
