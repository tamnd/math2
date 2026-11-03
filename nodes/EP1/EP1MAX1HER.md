---
tag: EP1MAX1HER
kind: definition
name: FitzHugh–Nagumo model
msc: [92C20, 34C60, 37N25]
defines: A52DRX0HNC
uses: [0NT64JV96A, RMWR3MDW0T, 02HR4C0B04, 0AAQ73WRFB, F5H8GW1XYS]
sources:
  - url: https://en.wikipedia.org/wiki/FitzHugh–Nagumo_model
---

## Definition

Let $a, b \in \R$, $\varepsilon > 0$ and $I \in \R$.
The *FitzHugh–Nagumo model* is the following planar system of [[ordinary differential equations|0NT64JV96A]].
$$\frac{dv}{dt} = v - \frac{v^3}{3} - w + I, \qquad \frac{dw}{dt} = \varepsilon (v + a - b w).$$
Here $v(t)$ is a voltage-like variable, $w(t)$ is a recovery variable and $I$ is the input current.

## Remarks

Usually $\varepsilon$ is small, so $v$ is fast and $w$ is slow.
The $v$-[[nullcline|02HR4C0B04]] is the cubic $w = v - v^3/3 + I$ and the $w$-nullcline is the line $v + a - b w = 0$.
Example: $a = 0.7$, $b = 0.8$, $\varepsilon = 0.08$, $I = 0$ give one equilibrium near $(v, w) = (-1.20, -0.62)$.
There the Jacobian $\begin{pmatrix} 1 - v^2 & -1 \\ \varepsilon & -\varepsilon b \end{pmatrix}$ has negative trace and positive determinant, so the rest state is stable, and the system is excitable.
For these values of $a$, $b$ and $\varepsilon$, as $I$ increases, the equilibrium moves onto the middle branch of the cubic.
There it loses stability through a [[Hopf bifurcation|F5H8GW1XYS]], and a stable [[limit cycle|0AAQ73WRFB]] of relaxation type appears.
Non-example: with the cubic term removed, the system is linear and cannot have a limit cycle.
