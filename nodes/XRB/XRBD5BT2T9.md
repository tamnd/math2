---
tag: XRBD5BT2T9
kind: statement
role: theorem
name: Schwarz reflection principle for harmonic functions
msc: [31B05, 31A05]
uses: [0DEB0JMN0W, 02BH3MCBQB, 0X3WGX95FE]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarz_reflection_principle
---

## Statement

Let $n \ge 2$ and write points of $\R^n$ as $x = (x', x_n)$ with $x' \in \R^{n-1}$ and $x_n \in \R$.
Let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]] that is symmetric in the hyperplane $x_n = 0$: if $(x', x_n) \in \Omega$, then $(x', -x_n) \in \Omega$.
Let $\Omega^+ = \set{x \in \Omega : x_n > 0}$ and $\sigma = \set{x \in \Omega : x_n = 0}$.
Let $u$ be a [[continuous function|0X3WGX95FE]] on $\Omega^+ \cup \sigma$ that is [[harmonic|0DEB0JMN0W]] on $\Omega^+$ and equal to $0$ on $\sigma$.
Define $U(x', x_n) = u(x', x_n)$ for $x_n \ge 0$ and $U(x', x_n) = -u(x', -x_n)$ for $x_n < 0$.
Then $U$ is harmonic on $\Omega$.

## Remarks

Proof idea: $U$ is continuous on $\Omega$ and harmonic off $\sigma$, so only points of $\sigma$ need care.
Take a closed ball centred at a point of $\sigma$ inside $\Omega$, and let $v$ be the Poisson integral of $U$ over its boundary sphere.
The boundary data are odd in $x_n$, so $v$ is odd in $x_n$ and vanishes on the hyperplane.
On each half ball, $U - v$ is harmonic and has boundary values $0$, so $U = v$ by the maximum principle.
Example: $u(x) = x_n$ on the upper half-space vanishes on $x_n = 0$, and its reflection is $U(x) = x_n$ on all of $\R^n$, which is harmonic.
The hypothesis $u = 0$ on $\sigma$ is needed: for $u \equiv 1$ the odd reflection jumps from $1$ to $-1$ across the hyperplane and is not continuous.
For the plane, this principle and the [[Schwarz reflection principle|P0R6YEGNB5]] for holomorphic functions imply each other through harmonic conjugates.

## Explanations

### L1 human

A harmonic function on one side of a flat wall that is zero on the wall can be continued through the wall.
On the other side it takes the mirror value with the opposite sign.
The two pieces fit together into one harmonic function.

### L2 human

The reflection principle is a tool to extend harmonic functions across flat pieces of the boundary.
It shows, for example, that a harmonic function on a half-ball that vanishes on the flat part is real analytic up to that flat part.
Combined with the Kelvin transform, the same idea works for reflection in a sphere.
The method of images for half-spaces rests on the same odd reflection.
