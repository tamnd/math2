---
tag: 9JVJKJTXDE
kind: definition
name: Gibbs phenomenon
msc: [42A20, 42A16]
defines: VMF169AT67
uses: [G12KXDHPPS, 004FH91BN5, V6Q24CHJG8]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbs_phenomenon
---

## Definition

Let $f \colon \R \to \R$ be a $2\pi$-periodic function that is piecewise continuously differentiable.
Let $x_0$ be a point of [[jump discontinuity|004FH91BN5]] of $f$, with jump $J = f(x_0^+) - f(x_0^-) \ne 0$.
Let $S_N f$ be the partial sums of the [[Fourier series|G12KXDHPPS]] of $f$.
The *Gibbs phenomenon* is the following behaviour of $S_N f$ near $x_0$:
$$\lim_{N \to \infty} S_N f\left(x_0 + \frac{\pi}{N}\right) = f(x_0^+) + J \left( \frac{1}{\pi} \int_0^{\pi} \frac{\sin t}{t} \, dt - \frac{1}{2} \right).$$
The symmetric formula holds at $x_0 - \frac{\pi}{N}$, where $f(x_0^-)$ and $-J$ replace $f(x_0^+)$ and $J$.

## Remarks

The constant $\frac{1}{\pi} \int_0^\pi \frac{\sin t}{t} \, dt - \frac{1}{2}$ is about $0.0895$, so the partial sums overshoot the jump by about $9\%$ of $\abs{J}$ on each side.
So $\sup_{x_0 < x < x_0 + \delta} S_N f(x)$ stays away from $f(x_0^+)$ for every $\delta > 0$, and the [[convergence|V6Q24CHJG8]] is not uniform on any interval with $x_0$ as an endpoint, although $S_N f(x) \to f(x)$ at each point of continuity.
Example: for the square wave equal to $\operatorname{sgn} x$ on $(-\pi, \pi)$, with $J = 2$ at $x_0 = 0$, one gets $S_N f(\pi/N) \to \frac{2}{\pi} \int_0^\pi \frac{\sin t}{t} \, dt \approx 1.179$.
Non-example: for a continuous piecewise smooth function such as $\abs{x}$ on $[-\pi, \pi]$, there is no jump, the Fourier series converges uniformly, and there is no overshoot of this kind.
The Fejér means of the Fourier series show no Gibbs phenomenon.
They are averages against a nonnegative kernel of mass $1$, so they stay between the infimum and supremum of $f$.
