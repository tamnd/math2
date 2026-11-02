---
tag: 3B0HB3DHW1
kind: problem
name: Stefan problem
msc: [35R35, "80A22", 35R37]
uses: [VP2HN86VAG, GC5BDZ6QBC]
about: [VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Stefan_problem
    locator: Mathematical formulation
same_as:
  wikidata: Q3775789
  wikipedia: Stefan problem
history:
  posed_by: "Josef Stefan"
  first_stated: "around 1890"
---

## Problem

The one-dimensional one-phase Stefan problem describes a solid at its melting temperature $0$ that occupies the half-line $x > 0$ and melts when heat enters at $x = 0$.
Let $a > 0$ be the thermal diffusivity of the liquid, $k > 0$ its thermal conductivity and $L > 0$ the latent heat per unit volume.
Let $g \colon [0, \infty) \to [0, \infty)$ be a given boundary temperature.
Find a function $s \colon [0, \infty) \to [0, \infty)$ with $s(0) = 0$, the position of the interface, and a temperature $u(x, t)$ defined for $0 \le x \le s(t)$, such that:

1. $\partial_t u = a \, \partial_x^2 u$ for $0 < x < s(t)$ and $t > 0$;
2. $u(0, t) = g(t)$ for $t > 0$;
3. $u(s(t), t) = 0$ for $t > 0$;
4. $L \, s'(t) = -k \, \partial_x u(s(t), t)$ for $t > 0$.

The unknown interface $s$ is the free boundary.
Condition 4, the Stefan condition, says that the heat flux arriving at the interface is used to melt the solid.

## Remarks

The problem is nonlinear, although the [[heat equation|VP2HN86VAG]] in clause 1 is linear, because the domain where it holds depends on the solution.
For a constant boundary temperature $g = T > 0$ there is an explicit similarity solution, due to Neumann.
In units where $a = k = L = 1$, it is $s(t) = 2 \lambda \sqrt{t}$ and $u(x, t) = T \left(1 - \operatorname{erf}\left(x / (2 \sqrt{t})\right) / \operatorname{erf}(\lambda)\right)$.
Here $\lambda > 0$ is the unique root of $\lambda e^{\lambda^2} \operatorname{erf}(\lambda) = T / \sqrt{\pi}$, which comes from inserting $u$ and $s$ into the Stefan condition.
The interface thus moves like $\sqrt{t}$, as is typical for diffusion.
Two-phase versions, in which the temperature of the solid also evolves, and versions in several space dimensions are studied as well.
Lamé and Clapeyron had studied an equivalent problem in 1831.

## Explanations

### L1 human

A block of ice is heated from one side.
Inside the water the heat spreads by diffusion, and at the boundary between water and ice the heat is used up to melt more ice.
The position of this boundary is not known in advance: it is part of the answer.
The Stefan problem asks for both the temperature in the water and the motion of the melting front.
