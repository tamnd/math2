---
tag: QAQE4A2QFZ
kind: definition
name: El Niño–Southern Oscillation models
msc: [86A08, 86A05, 34K13]
defines: 9AB46C771V
uses: [0NT64JV96A, 39PCDRDB01, QERM9Y9QSJ, 6N1MQMA9TM, 0AAQ73WRFB, F5H8GW1XYS]
sources:
  - url: https://en.wikipedia.org/wiki/El_Niño–Southern_Oscillation
---

## Definition

An *El Niño–Southern Oscillation model* (ENSO model) is a dynamical model of the coupled ocean and atmosphere of the tropical Pacific.
Its state includes the sea surface temperature anomaly $T$ of the eastern equatorial Pacific, and it is built from:

1. a positive feedback, in which a warm anomaly $T > 0$ weakens the easterly winds and the weaker winds increase $T$;
2. a negative feedback, delayed or slower, carried by the adjustment of the ocean thermocline through equatorial [[Kelvin waves|QERM9Y9QSJ]] and [[Rossby waves|6N1MQMA9TM]].

Two standard conceptual ENSO models are the following.
The *delayed oscillator* is the [[delay differential equation|39PCDRDB01]]
$$\frac{dT}{dt} = T - T^3 - \alpha \, T(t - \delta), \qquad 0 < \alpha < 1, \ \delta > 0.$$
It is in nondimensional form, and the delayed term is the effect of waves reflected at the western boundary.
The *recharge oscillator* is the linear system of [[ordinary differential equations|0NT64JV96A]]
$$\frac{dT}{dt} = R T + \gamma h, \qquad \frac{dh}{dt} = -r h - a T.$$
Here $h$ is the depth anomaly of the thermocline in the western Pacific, and $\gamma, r, a > 0$.
The constant $R$ is the net growth rate of $T$ from clause 1 and damping.

## Remarks

Example: the recharge oscillator has the matrix $\begin{pmatrix} R & \gamma \\ -a & -r \end{pmatrix}$, with trace $R - r$ and determinant $a \gamma - R r$.
Its eigenvalues are complex when $(R + r)^2 < 4 a \gamma$, and then the solutions oscillate with growth rate $(R - r)/2$.
So the model oscillates, and the oscillation is neutral when $R = r$.
In nonlinear versions of the model, the loss of stability as $R$ crosses $r$ is a [[Hopf bifurcation|F5H8GW1XYS]], and the growing oscillation can saturate in a [[limit cycle|0AAQ73WRFB]].

Non-example: the equation $dT/dt = T - T^3$ has clause 1 but not clause 2.
Each solution tends to one of the equilibria $T = -1, 0, 1$ and never oscillates, so it is not an ENSO model.

The delayed oscillator was studied by Suarez and Schopf, and the recharge oscillator by Jin.
Intermediate models, such as the Zebiak–Cane model, solve shallow-water equations for the ocean and a simple atmosphere on the equatorial beta plane.
