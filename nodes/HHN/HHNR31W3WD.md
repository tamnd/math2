---
tag: HHNR31W3WD
kind: statement
role: proposition
name: Differentiation and multiplication under the Fourier transform
msc: ["42B10", "42A38"]
uses: [DPVM34ADZV, SASP14MA1Z, BYNV84PF86]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform
---

## Statement

Let $n \ge 1$, let $f \in L^1(\R^n)$, and let $\hat f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi}\, dx$ be its [[Fourier transform|DPVM34ADZV]].
Fix an index $j \in \set{1, \dots, n}$.

1. If the function $x \mapsto x_j f(x)$ lies in [[$L^1(\R^n)$|SASP14MA1Z]], then $\hat f$ has a continuous partial derivative in $\xi_j$, and $\partial_{\xi_j} \hat f(\xi)$ is the Fourier transform of $-2\pi i x_j f(x)$.
2. If $f$ is continuously differentiable and $\partial_j f$ lies in $L^1(\R^n)$, then the Fourier transform of $\partial_j f$ is $\xi \mapsto 2\pi i \xi_j \hat f(\xi)$.

## Remarks

For part 1, differentiate under the integral sign.
The difference quotients of $e^{-2\pi i x \cdot \xi}$ in $\xi_j$ are bounded by $2\pi \abs{x_j}$, so [[dominated convergence|BYNV84PF86]] applies with dominating function $2\pi \abs{x_j f(x)}$.
For part 2, integrate by parts in $x_j$.
On almost every line parallel to the $j$-th axis, $f$ and $\partial_j f$ are integrable, so $f$ has limits at both ends, and these limits are $0$; the boundary terms vanish.

Example: for $f(x) = e^{-\pi x^2}$ on $\R$, part 2 gives $\widehat{f'}(\xi) = 2\pi i \xi e^{-\pi \xi^2}$, and part 1 gives $\frac{d}{d\xi} e^{-\pi \xi^2} = -2\pi \xi e^{-\pi \xi^2}$; both agree with $f' = -2\pi x f$.

Iterating, if $f$ lies in the Schwartz space then $\widehat{\partial^\alpha f}(\xi) = (2\pi i \xi)^\alpha \hat f(\xi)$ and $\partial^\alpha \hat f$ is the transform of $(-2\pi i x)^\alpha f$ for every multi-index $\alpha$.
The integrability hypotheses cannot be dropped: if $x_j f$ is not integrable, $\hat f$ need not be differentiable, as for $f(x) = 1/(1 + x^2)$ on $\R$, whose transform $\pi e^{-2\pi \abs{\xi}}$ has a corner at $0$.

## Explanations

### L1 human

The Fourier transform swaps two operations.
Taking a derivative of $f$ becomes multiplying $\hat f$ by $2\pi i \xi$.
Multiplying $f$ by $x$ becomes, up to a constant, taking a derivative of $\hat f$.

### L2 human

These rules turn a linear differential operator with constant coefficients $P(\partial)$ into multiplication by the polynomial $P(2\pi i \xi)$.
This is how the transform solves the heat, wave and Schrödinger equations on $\R^n$.
They also give the duality between smoothness and decay: the more derivatives $f$ has in $L^1$, the faster $\hat f$ decays, and the faster $f$ decays, the smoother $\hat f$ is.
This duality is the reason the Schwartz space is mapped onto itself.
