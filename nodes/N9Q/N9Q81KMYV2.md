---
tag: N9Q81KMYV2
kind: definition
name: Frank-Kamenetskii theory of thermal explosion
msc: ["80A25", 35J61, 35B32]
defines: S8BJBSH8KW
uses: [Q3M9H7YSYZ, 9MS4X2KC1H, T7WBVDBHKE, 0XQ2ZVN1PZ, G3XFT0MWKH, XBQBT9E7JT]
sources:
  - url: https://en.wikipedia.org/wiki/Frank-Kamenetskii_theory
---

## Definition

Let $\Omega \subseteq \R^n$, $n \in \set{1, 2, 3}$, be a bounded domain that contains a reacting material, and let $a > 0$ be a characteristic length of $\Omega$.
The material has [[thermal conductivity|XBQBT9E7JT]] $k > 0$, and its boundary is held at temperature $T_0 > 0$.
The reaction releases heat at the Arrhenius rate $Q A e^{-E/(RT)}$ per unit volume.
Here $Q, A > 0$ are constants, $E > 0$ is the activation energy and $R$ is the gas constant; consumption of the reactant is neglected.
Put $\theta = E (T - T_0)/(R T_0^2)$, use the coordinates $\xi = x / a$, and replace $e^{-E/(RT)}$ by $e^{-E/(RT_0)} e^{\theta}$.
*Frank-Kamenetskii theory* is the study of the steady states of this model.
They are the solutions of
$$\Delta \theta + \delta e^{\theta} = 0 \text{ in } \Omega_a, \qquad \theta = 0 \text{ on } \partial \Omega_a,$$
where $\Omega_a = \set{x / a : x \in \Omega}$, $\Delta$ is the [[Laplacian|0XQ2ZVN1PZ]] in $\xi$, and
$$\delta = \frac{Q A E a^2}{k R T_0^2} e^{-E/(RT_0)}$$
is the *Frank-Kamenetskii parameter*.
The *critical value* $\delta_c$ is the supremum of the $\delta > 0$ for which a solution exists.

## Remarks

This is the [[Gelfand–Bratu problem|Q3M9H7YSYZ]] with $\lambda = \delta$ and [[Dirichlet boundary condition|G3XFT0MWKH]].
For $\delta > \delta_c$ there is no steady state, and the body undergoes [[thermal runaway|9MS4X2KC1H]].
Example: for the slab $\Omega_a = (-1, 1)$, with $a$ the half-thickness, the solutions are $\theta(\xi) = -2 \ln\big(\cosh(c \xi) / \cosh c\big)$ with $c > 0$ and $\delta = 2 c^2 / \cosh^2 c$.
Check: $\theta'' = -2 c^2 \operatorname{sech}^2(c\xi)$ and $\delta e^{\theta} = 2 c^2 \operatorname{sech}^2 c \cdot \cosh^2 c / \cosh^2(c\xi)$, so the two terms cancel, and $\theta(\pm 1) = 0$.
The maximum of $2 c^2 / \cosh^2 c$ over $c > 0$ gives $\delta_c \approx 0.878$.
For an infinite cylinder of radius $a$ one has $\delta_c = 2$, and for a sphere of radius $a$ one has $\delta_c \approx 3.32$.
Non-example: with heat loss through the boundary by a heat transfer coefficient instead of a fixed boundary temperature, the boundary condition is of Robin type, and the critical values change.
In the limit of small conductive resistance inside the body, the Robin version reduces to [[Semenov's theory|T7WBVDBHKE]].
