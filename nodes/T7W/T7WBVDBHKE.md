---
tag: T7WBVDBHKE
kind: definition
name: Semenov's theory of thermal explosion
msc: ["80A25", 34C23]
defines: 7ZES3H0JJG
uses: [9MS4X2KC1H, 0P97V20RW7, TB7NBCCXJ1]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_runaway
---

## Definition

Consider a vessel of volume $V$ and wall area $S$ that contains a reacting mixture of uniform temperature $T(t)$, density $\rho$ and specific heat $c$.
The walls are held at temperature $T_0 > 0$, and $h > 0$ is the heat transfer coefficient at the walls.
The reaction releases heat at the Arrhenius rate $Q A e^{-E/(RT)}$ per unit volume, with constants $Q, A > 0$.
Here $E > 0$ is the activation energy and $R$ is the gas constant.
Consumption of the reactant is neglected.
*Semenov's theory* is the study of the [[ordinary differential equation|0P97V20RW7]]
$$\rho c V \frac{dT}{dt} = V Q A\, e^{-E/(RT)} - h S (T - T_0)$$
and of its dimensionless form, obtained with $\theta = E (T - T_0) / (R T_0^2)$ and the approximation $e^{-E/(RT)} \approx e^{-E/(RT_0)} e^{\theta}$:
$$\tau \frac{d\theta}{dt} = \psi e^{\theta} - \theta, \qquad \tau = \frac{\rho c V}{h S}, \qquad \psi = \frac{V Q A E}{h S R T_0^2} e^{-E/(RT_0)}.$$
The number $\psi$ is the *Semenov number*.

## Remarks

The approximation of the exponent is the first-order Taylor expansion of $-E/(RT)$ about $T_0$, and it is accurate when $E/(RT_0)$ is large and $T - T_0$ is small compared with $T_0$.
Steady states are the solutions of $\psi e^{\theta} = \theta$.
The curve and the line touch where $\psi e^{\theta} = \theta$ and $\psi e^{\theta} = 1$, that is at $\theta = 1$ and $\psi = 1/e$.
Hence for $\psi < 1/e$ there are two steady states, the lower one stable, and the temperature started at $\theta = 0$ tends to the lower one.
For $\psi > 1/e$ there is none, and the system is in [[thermal runaway|9MS4X2KC1H]] from $\theta = 0$.
Example: $\psi = 1/(2e)$ satisfies $\psi < 1/e$, and indeed $\psi e^{\theta} - \theta$ equals $1/(2e) > 0$ at $\theta = 0$ and $1/2 - 1 < 0$ at $\theta = 1$, so a steady state lies in $(0, 1)$.
Non-example: $\psi = 1$ gives no steady state, since $e^{\theta} > \theta$ for all real $\theta$.
At $\psi = 1/e$ the two steady states merge in a [[saddle-node bifurcation|TB7NBCCXJ1]].
The critical temperature rise is $\theta = 1$, that is $T - T_0 = R T_0^2 / E$.
