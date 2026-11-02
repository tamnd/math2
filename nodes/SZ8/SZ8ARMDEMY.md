---
tag: SZ8ARMDEMY
kind: statement
role: theorem
name: Szegő's theorem
msc: [42C05, 33C47, 47B35]
uses: [3F9G3DRQ62, 1RP3NVGNA6, GKY2WSHE26]
about: [3F9G3DRQ62]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_polynomials_on_the_unit_circle
---

## Statement

Let $\mu$ be a probability measure on the unit circle with infinite support, and let $(\alpha_n)_{n \ge 0}$ be its [[Verblunsky coefficients|1RP3NVGNA6]].
Write the Lebesgue decomposition of $\mu$ as $d\mu = w(\theta) \, \frac{d\theta}{2\pi} + d\mu_s$, where $w \ge 0$ is integrable and $\mu_s$ is singular with respect to arc length.
Then
$$\prod_{n=0}^{\infty} \big( 1 - \abs{\alpha_n}^2 \big) = \exp\left( \int_0^{2\pi} \log w(\theta) \, \frac{d\theta}{2\pi} \right),$$
where both sides are $0$ when $\int_0^{2\pi} \log w(\theta) \, d\theta = -\infty$.
In particular, $\sum_{n} \abs{\alpha_n}^2 < \infty$ if and only if $\int_0^{2\pi} \log w(\theta) \, d\theta > -\infty$.

## Remarks

The integral of $\log w$ is well defined in $[-\infty, 0]$, because Jensen's inequality gives $\int \log w \, \frac{d\theta}{2\pi} \le \log \int w \, \frac{d\theta}{2\pi} \le 0$.
By the norm formula for the [[monic orthogonal polynomials|3F9G3DRQ62]], the left side equals $\lim_{n \to \infty} \norm{\Phi_n}^2$.
And $\norm{\Phi_n}^2 = \min \set{ \norm{p}^2 : p \text{ monic of degree } n }$, so the theorem computes the best mean-square prediction error of $z^n$ from the past.
A standard proof treats this minimum as an extremal problem in the Hardy space $H^2$ of the disk.
Along the way, the singular part $\mu_s$ turns out not to affect the limit.

Equivalently, in terms of the [[Toeplitz matrices|GKY2WSHE26]] $T_n = (c_{j-k})_{j,k=0}^{n}$ of the moments $c_k = \int e^{-ik\theta} \, d\mu$, one has $\det T_n / \det T_{n-1} = \norm{\Phi_n}^2$.
So the theorem also gives $\lim_{n \to \infty} (\det T_n)^{1/(n+1)} = \exp \int \log w \, \frac{d\theta}{2\pi}$, Szegő's first limit theorem.

Example: for $d\mu = d\theta/2\pi$ one has $w = 1$ and all $\alpha_n = 0$, and both sides equal $1$.
If $\mu$ is singular, $w = 0$ almost everywhere, so $\prod (1 - \abs{\alpha_n}^2) = 0$ and $\sum \abs{\alpha_n}^2 = \infty$.

## Explanations

### L1 human

A measure on the circle is encoded by its Verblunsky coefficients, a sequence of points in the unit disk.
Szegő's theorem links the size of these coefficients to how small the density of the measure can get.
The coefficients are square-summable exactly when the density is not too close to zero, in the sense that the integral of its logarithm is finite.

### L2 human

The condition $\int \log w > -\infty$ is the Szegő condition.
The same condition governs the factorization $w = \abs{D}^2$ with an outer function $D$ in the Hardy space.
It also governs prediction for stationary sequences: the future is not determined by the past exactly when it holds.
The theorem is a sum rule, relating the coefficients to the measure, and it is a starting point for finer results such as the [[Szegő limit theorems|WNJPRHZ680]] on Toeplitz determinants.
