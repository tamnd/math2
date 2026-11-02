---
tag: AZPKCHND9T
kind: statement
role: theorem
name: Smoothness and analyticity of harmonic functions
msc: [31B05, 35B65]
uses: [0DEB0JMN0W, 0V33BNKZ9S, 081WKEDK6C, 0HYPR64JM2, N76R7JWMNJ]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_function
---

## Statement

Let $U \subseteq \R^n$ be an open set and let $u \colon U \to \R$ be [[harmonic|0DEB0JMN0W]].

1. The function $u$ is [[infinitely differentiable|0V33BNKZ9S]] on $U$, and every partial derivative of $u$ is harmonic on $U$.
2. The function $u$ is real [[analytic|081WKEDK6C]] on $U$: each $a \in U$ has a neighbourhood on which $u$ is a convergent power series in $x - a$.

## Remarks

Proof idea for part 1: by the [[mean value property|0HYPR64JM2]], $u$ equals its convolution with a smooth radial mollifier away from the boundary of $U$.
A convolution with a smooth function is smooth.
Since $\Delta$ commutes with partial derivatives, $\Delta(\partial^\alpha u) = \partial^\alpha(\Delta u) = 0$.
Proof idea for part 2: the [[gradient estimates|N76R7JWMNJ]] give $\abs{\partial^\alpha u(a)} \le C^{k+1} k^k \sup_{B(a, r)} \abs{u} / r^{k}$ for $\abs{\alpha} = k$, with $C$ depending only on $n$.
This growth makes the Taylor remainder tend to $0$ on a small ball.
Example: $u(x, y) = e^x \cos y$ is harmonic on $\R^2$, and its Taylor series at $0$ converges to it everywhere.
Harmonicity is needed and $C^2$ is not enough: $\abs{x}^3$ on $\R$ is twice continuously differentiable but not three times differentiable at $0$.
In contrast, a merely continuous function with the mean value property is already harmonic, hence analytic.

## Explanations

### L1 human

Laplace's equation forces its solutions to be extremely smooth.
Even if one only asks for two derivatives, a harmonic function automatically has derivatives of all orders, and it is given locally by a power series.
So a harmonic function cannot have a hidden corner or kink anywhere.

### L2 human

This is the simplest case of elliptic regularity: solutions of elliptic equations with smooth or analytic coefficients are as regular as the coefficients allow.
Analyticity implies a unique continuation property: a harmonic function on a connected open set that vanishes on a nonempty open subset vanishes everywhere.
The heat equation shares smoothness but not analyticity in time, and the wave equation has neither, so this property marks the elliptic case.
