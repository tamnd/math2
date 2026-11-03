---
tag: 3WBDE9GV3M
kind: definition
name: Chandrasekhar's white dwarf equation
msc: [85A15, 34A34]
defines: F1ZPTWW5SA
uses: [0NT64JV96A, 4FC5XQA2RK, ANRZZMH2Q0]
sources:
  - url: https://en.wikipedia.org/wiki/Chandrasekhar%27s_white_dwarf_equation
---

## Definition

Let $C$ be a real number with $0 < C < 1$.
Let $\varphi$ be a real function of $\eta > 0$.
*Chandrasekhar's white dwarf equation* with parameter $C$ is the [[ordinary differential equation|0NT64JV96A]]
$$\frac{1}{\eta^2} \frac{d}{d\eta} \left( \eta^2 \frac{d\varphi}{d\eta} \right) + \left( \varphi^2 - C \right)^{3/2} = 0,$$
with the initial conditions $\varphi(0) = 1$ and $\varphi'(0) = 0$.
It is considered on the interval where $\varphi^2 \ge C$, and the surface of the star is the first point $\eta_1$ where $\varphi(\eta_1) = \sqrt{C}$.

## Remarks

It expresses [[hydrostatic equilibrium|4FC5XQA2RK]] for a spherical ball of cold, fully degenerate electron gas.
Let $x$ be the Fermi momentum of the electrons in units of $m_e c$, with $m_e$ the electron mass and $c$ the speed of light.
Let $x_0$ be the central value of $x$.
Then $\varphi = \sqrt{1 + x^2} / \sqrt{1 + x_0^2}$ and $C = 1/(1 + x_0^2)$.
So $C$ near $1$ means a low central density and $C$ near $0$ a very high one.
Example: take $C = 1/2$.
The central value $\varphi(0) = 1$ satisfies $\varphi^2 \ge C$, and the solution decreases from $1$ until it reaches $\sqrt{1/2}$ at a finite radius $\eta_1$.
It describes a white dwarf whose central electrons have Fermi momentum $x_0 = 1$.
Limit case: for $C = 0$ the equation becomes $\eta^{-2} (\eta^2 \varphi')' + \varphi^3 = 0$, the [[Lane–Emden equation|ANRZZMH2Q0]] of index $3$, which governs the mass limit.
Non-example: the constant $\varphi = 1$ is not a solution, since the left side equals $(1 - C)^{3/2} > 0$.
For $C$ close to $1$, writing $\varphi^2 - C = (1 - C) \theta$ and rescaling $\eta$ turns the equation, to leading order in $1 - C$, into the Lane–Emden equation of index $3/2$.
