---
tag: DDQS2ZEEAG
kind: definition
name: Cable equation
msc: [92C20, 35Q92]
defines: FZ7ND8S1QV
uses: [GC5BDZ6QBC, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Cable_theory
---

## Definition

Consider a cylindrical fibre with passive membrane, with position $x$ along the fibre and time $t$.
Let $r_m > 0$ be the membrane resistance times unit length, $r_l > 0$ the axial resistance per unit length, and $c_m > 0$ the membrane capacitance per unit length.
Let $V(x, t)$ be the deviation of the membrane potential from its resting value.
The *cable equation* is the [[partial differential equation|GC5BDZ6QBC]]
$$\lambda^2 \frac{\partial^2 V}{\partial x^2} = \tau \frac{\partial V}{\partial t} + V,$$
where $\lambda = \sqrt{r_m / r_l}$ is the *length constant* and $\tau = r_m c_m$ is the *time constant*.

## Remarks

Example: in an infinite fibre held at $V(0) = V_0$, the bounded steady solution is $V(x) = V_0 e^{-\abs{x}/\lambda}$; indeed $\lambda^2 V'' = V$ for $x \ne 0$.
Substituting $V = e^{-t/\tau} u$ gives $\tau\, \partial_t u = \lambda^2\, \partial_x^2 u$, a [[heat equation|VP2HN86VAG]], so every solution of the cable equation is $e^{-t/\tau}$ times a solution of the heat equation.
Non-example: the Hodgkin–Huxley equations for a propagating action potential add nonlinear ionic currents to this equation, so the membrane is not passive and the equation is not the cable equation.
Branched dendritic trees are handled by solving the cable equation on each branch with matching conditions at the branch points.
