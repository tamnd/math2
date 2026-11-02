---
tag: 53MWMX2HWT
kind: statement
role: theorem
name: Bochner's classification of orthogonal polynomial eigenfunctions
msc: [33C45, 34B24]
uses: [47WJ34NC9K, 0BQAA2BK3Q, 0P4JRMSWNH, 7WV6B2502K]
about: [47WJ34NC9K]
sources:
  - url: https://en.wikipedia.org/wiki/Classical_orthogonal_polynomials
---

## Statement

Let $\sigma$ and $\tau$ be real polynomials, not both zero, with $\deg \sigma \le 2$ and $\deg \tau \le 1$, and let $\mathcal{D} = \sigma(x) \frac{d^2}{dx^2} + \tau(x) \frac{d}{dx}$.
Let $(p_n)_{n \ge 0}$ be real polynomials with $\deg p_n = n$, each an eigenfunction of $\mathcal{D}$: $\mathcal{D} p_n = \lambda_n p_n$ for some real [[eigenvalue|0BQAA2BK3Q]] $\lambda_n$.
Assume that $(p_n)$ is orthogonal for a weight.
That is, there are an open interval $I$ and a continuous $w \colon I \to (0, \infty)$ with all moments finite such that $\int_I p_m p_n\, w\, dx = 0$ for $m \ne n$.
Then, up to an affine change of variable and nonzero constant factors, $(p_n)$ is one of the [[classical orthogonal polynomial|47WJ34NC9K]] families: Jacobi, Laguerre or Hermite.

## Remarks

Every operator $\mathcal{D}$ of this form maps polynomials of degree at most $n$ to themselves.
In fact $\mathcal{D} x^n = \left( n(n-1)\sigma_2 + n \tau_1 \right) x^n + \text{lower terms}$, where $\sigma_2$ and $\tau_1$ are the coefficients of $x^2$ in $\sigma$ and of $x$ in $\tau$.
The proof sorts $\sigma$ by its degree and its roots, up to affine changes.
Orthogonality for a positive weight forces $w$ to solve the Pearson equation $(\sigma w)' = \tau w$, and only the Jacobi, Laguerre and Hermite cases give a positive weight with finite moments.
Example: $\sigma = 1$ and $\tau = -2x$ give $\mathcal{D} = \frac{d^2}{dx^2} - 2x \frac{d}{dx}$, with eigenfunctions the [[Hermite polynomials|MGACY98E9H]] and $\lambda_n = -2n$; the check for $H_2 = 4x^2 - 2$ is $8 - 2x \cdot 8x = -16x^2 + 8 = -4 H_2$.
The orthogonality hypothesis is necessary: $\sigma = x^2$ and $\tau = 2x + 2$ have the Bessel polynomials as eigenfunctions, which are not orthogonal for any positive weight on a real interval.
Without the orthogonality hypothesis, Bochner's list also contains the Bessel polynomials and the powers $x^n$, which are eigenfunctions of $x^2 \frac{d^2}{dx^2}$.

## Explanations

### L1 human

Many famous polynomial families solve a second-order differential equation, one polynomial for each degree.
Bochner asked which families can do this, and the answer is a short list.
If one also asks for orthogonality with a positive weight, only the Jacobi, Laguerre and Hermite families remain.

### L2 human

This is the reason the classical families are singled out among all orthogonal polynomials.
The operator $\mathcal{D}$ becomes symmetric for the inner product $\int f g\, w\, dx$ when $(\sigma w)' = \tau w$, the Pearson equation for the weight, and $\sigma w$ vanishes fast enough at the ends of $I$.
Then $\mathcal{D}$ is a [[Sturm–Liouville operator|7WV6B2502K]], and the $p_n$ are its eigenfunctions, orthogonal because they belong to different eigenvalues.
Discrete analogues with difference operators lead to the Hahn, Meixner, Krawtchouk and Charlier polynomials, and $q$-analogues to the Askey scheme.
