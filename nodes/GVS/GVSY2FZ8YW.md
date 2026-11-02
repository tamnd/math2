---
tag: GVSY2FZ8YW
kind: definition
name: Floquet multiplier
msc: [34C25, 34A30]
defines: FPS7YFGX32
uses: [0H1GN6P9R5, 0BQAA2BK3Q, 0ATF6Q0633]
sources:
  - url: https://en.wikipedia.org/wiki/Floquet_theory
---

## Definition

Let $T > 0$ and let $A \colon \R \to \R^{n \times n}$ be continuous and [[periodic|0ATF6Q0633]] of period $T$.
Consider the linear system $x' = A(t)\, x$ on $\R^n$.
Let $\Phi$ be its [[fundamental matrix|0H1GN6P9R5]] with $\Phi(0) = I$.
The *monodromy matrix* of the system is $M = \Phi(T)$.
A *Floquet multiplier* of the system is an [[eigenvalue|0BQAA2BK3Q]] of $M$, counted with its algebraic multiplicity.

## Remarks

A complex number $\rho$ is a Floquet multiplier if and only if the system has a nonzero solution with $x(t + T) = \rho\, x(t)$ for all $t$.
Every multiplier is nonzero, and by Liouville's formula their product is $\det M = \exp\left(\int_0^T \tr A(t)\, dt\right)$.
A number $\lambda$ with $e^{\lambda T} = \rho$ is called a Floquet exponent.
All solutions tend to $0$ if and only if every multiplier has absolute value less than $1$.

Example: for a constant matrix $A$, one has $\Phi(t) = e^{tA}$, so $M = e^{TA}$ and the multipliers are $e^{\lambda T}$ for the eigenvalues $\lambda$ of $A$.
For the scalar equation $x' = (1 + \cos t)\, x$ with $T = 2\pi$, one has $\Phi(t) = e^{t + \sin t}$, and the only multiplier is $e^{2\pi}$.

Non-example: for $x' = t\, x$, the coefficient is not periodic, so the definition does not apply; the ratio $x(t + T)/x(t) = e^{tT + T^2/2}$ depends on $t$.

For a $T$-periodic orbit $\gamma$ of an autonomous system $x' = f(x)$, the multipliers of $\gamma$ are those of the linear system $y' = Df(\gamma(t))\, y$.
One of them is always $1$, with the eigenvector $f(\gamma(0))$.
