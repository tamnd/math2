---
tag: 0SS1P1YC9A
kind: definition
name: First integral
msc: [34A05, 34C14]
defines: 0262JP0NV9
uses: [07BNRFQ0PJ, 04SW7WECS8, 0BVT6VSB3S]
sources:
  - url: https://en.wikipedia.org/wiki/Constant_of_motion
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Constant_of_motion
    locator: Methods for identifying constants of motion
---

## Definition

Let $U$ be an open subset of $\mathbb{R}^n$ and let $f : U \to \mathbb{R}^n$ be a function.
A first integral of the [[autonomous system|07BNRFQ0PJ]] $x' = f(x)$ is a continuously differentiable function $H : U \to \mathbb{R}$ such that
$$\nabla H(x) \cdot f(x) = 0 \quad \text{for each } x \in U,$$
and such that $H$ is not constant on any non-empty open subset of $U$.

## Remarks

The condition means that $\frac{d}{dt} H(\gamma(t)) = 0$ for each [[solution|04SW7WECS8]] $\gamma$. So $H$ is constant along each solution.
Each [[trajectory|0BVT6VSB3S]] lies in a level set $\{x : H(x) = c\}$. In the plane, the level curves of $H$ give the phase portrait.
For the [[harmonic oscillator|0YG0ZJPTWG]] $x' = y$, $y' = -x$, the function $H(x, y) = x^2 + y^2$ is a first integral.
The Hamiltonian of a time-independent [[Hamiltonian system|0C2AKPDCD9]] is a first integral.

## Explanations

### L1 human

A first integral is a quantity that does not change while the system moves, such as the energy of a system without friction.
Knowing it tells us that each motion stays on one level set of this quantity.
