---
tag: M4DMBVS16M
kind: statement
role: proposition
name: Stefan's law of ice growth
msc: [86A40, 80A22]
uses: [3B0HB3DHW1, VP2HN86VAG]
about: [3B0HB3DHW1]
sources:
  - url: https://en.wikipedia.org/wiki/Stefan_problem
---

## Statement

Consider a layer of ice of thickness $h(t)$ on calm water that stays at the freezing temperature $T_f$.
Let the ice have density $\rho$, thermal conductivity $k$ and latent heat of fusion $L$ per unit mass.
Let its upper surface be held at a temperature $T_s(t) < T_f$.
Assume that the temperature in the ice is linear in depth at each time.
Assume also that no heat flows from the water into the ice.
So all heat conducted up through the ice comes from freezing at the ice–water interface.
Then
$$h(t)^2 = h(0)^2 + \frac{2k}{\rho L} \int_0^t \big(T_f - T_s(\tau)\big)\, d\tau.$$

## Remarks

The energy balance at the interface is $\rho L \, dh/dt = k (T_f - T_s)/h$.
Its left side is the latent heat released per unit area and time, and its right side is the heat flux conducted through a linear profile.
Writing it as $\tfrac12 \, d(h^2)/dt = (k/\rho L)(T_f - T_s)$ and integrating gives the result.
So the thickness grows like the square root of the accumulated freezing degree-days.
For constant $T_s$ and $h(0) = 0$, $h(t) = \sqrt{2k(T_f - T_s)t/(\rho L)}$, and four times as long a cold spell gives only twice the ice.
The linear profile is the quasi-steady limit of the one-phase [[Stefan problem|3B0HB3DHW1]], in which the temperature solves the [[heat equation|VP2HN86VAG]].
For constant $T_s$, its exact similarity solution is $h = 2\lambda\sqrt{\kappa t}$, where $\kappa$ is the thermal diffusivity of ice and $\lambda$ is a constant.
It reduces to the formula above when the Stefan number $c(T_f - T_s)/L$ is small, where $c$ is the specific heat of ice.
In practice snow cover and heat from the water slow the growth, so the law gives an upper bound and is often used with an empirical correction factor.

## Explanations

### L1 human

When a lake freezes, the new ice forms at the bottom of the existing ice.
The heat released by freezing must escape upward through the ice, and thicker ice lets heat out more slowly.
So ice grows quickly at first and then more and more slowly, with thickness proportional to the square root of how long and how hard it has been freezing.

### L2 human

Stefan's law is the simplest worked case of a moving boundary problem: the position of the ice–water interface is unknown and is fixed by an energy balance there.
The full model is the Stefan problem for the heat equation with a free boundary, and the law is its leading-order solution for small Stefan number.
The same square-root-of-time growth appears in many diffusion-controlled phase changes, such as solidification of metals and freezing of soil.
