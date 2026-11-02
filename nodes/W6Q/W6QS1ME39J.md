---
tag: W6QS1ME39J
kind: definition
name: Schrödinger operator
msc: [34L40, 35J10, 81Q10]
defines: 89AA6XJY5K
uses: [0E0B6RA8K0, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Schrödinger_equation
---

## Definition

Let $I \subseteq \R$ be an open interval and let $V \colon I \to \R$ be locally integrable.
The one-dimensional Schrödinger operator with potential $V$ is the differential expression
$$H y = -y'' + V y,$$
acting on functions $y \colon I \to \C$ such that $y$ and $y'$ are locally absolutely continuous.
More generally, for an open set $\Omega \subseteq \R^d$ and a real function $V$ on $\Omega$, the Schrödinger operator is $H = -\Delta + V$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
The equation $H y = \lambda y$ with $\lambda \in \C$ is the time-independent Schrödinger equation.

## Remarks

Example: for $I = \R$ and $V(x) = x^2$, the function $y(x) = e^{-x^2/2}$ has $y'' = (x^2 - 1) e^{-x^2/2}$.
So $H y = -y'' + x^2 y = y$, and $y$ solves the Schrödinger equation with $\lambda = 1$.
Non-example: $-y'' + i x y$ is not a Schrödinger operator in this sense, because the potential $i x$ is not real.
In units where Planck's constant and the mass are normalised, $H$ is the energy operator of a quantum particle.
To get a self-adjoint operator on $L^2(I)$ one must also fix boundary conditions at the ends of $I$ when they are needed.

## Explanations

### L1 human

A Schrödinger operator is minus the second derivative plus multiplication by a real function.
It is the energy of a quantum particle that moves in a landscape of height $V$.
