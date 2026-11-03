---
tag: PHW0E57MH3
kind: problem
name: Molodensky's problem
msc: [86A30, 31B20, 35R35]
uses: [5Y2BWNY6MF, 0DEB0JMN0W]
about: [5Y2BWNY6MF]
sources:
  - url: https://en.wikipedia.org/wiki/Physical_geodesy
history:
  posed_by: "Mikhail Molodensky"
  first_stated: "1945"
---

## Problem

Let $\omega > 0$ be the known angular velocity of the Earth about the $x_3$-axis, and let $\Phi(x) = \tfrac12 \omega^2 (x_1^2 + x_2^2)$ be the centrifugal potential.
Let $S^2$ be the unit sphere, used as a parameter set, and suppose the values $W^*(\xi) \in \R$ and $g^*(\xi) \in \R^3$ are given for every $\xi \in S^2$.
Find a closed surface $S$ in $\R^3$, given by an embedding $x \colon S^2 \to \R^3$, and a function $V$ [[harmonic|0DEB0JMN0W]] outside $S$ with $V(y) \to 0$ as $\norm{y} \to \infty$.
They must be such that the [[geopotential|5Y2BWNY6MF]] $W = V + \Phi$ satisfies
$$W(x(\xi)) = W^*(\xi) \quad \text{and} \quad \nabla W(x(\xi)) = g^*(\xi) \quad \text{for all } \xi \in S^2.$$
Here $W^*$ comes from levelling combined with gravity, and the direction of $g^*$ from astronomical latitude and longitude.

## Remarks

Unlike the [[geodetic boundary value problem|1F4S3G1R6J]] in Stokes' form, the boundary surface $S$ is an unknown, so this is a free boundary problem for the Laplace equation.
It avoids any hypothesis about the masses between the geoid and the surface, which Stokes' approach needs.
In practice it is linearised around a known approximate surface, and the linear problem is solved by series or integral equation methods.
Lars Hörmander proved in 1976 a local existence and uniqueness theorem for the nonlinear problem, for data close to those of a reference solution, using a Nash–Moser iteration.

## Explanations

### L1 human

Classical geodesy computes the geoid, a surface hidden under the continents, and this needs guesses about the density of the rock above it.
Molodensky asked instead to find the actual surface of the Earth and the gravity field outside it at the same time, from measurements made on that surface.
The shape of the surface is part of the answer, which makes the problem harder but removes the guesses about density.
