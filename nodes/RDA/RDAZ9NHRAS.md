---
tag: RDAZ9NHRAS
kind: definition
name: Transmission line
msc: [78A50, 94C05]
defines: YS0P4Z5Y4X
uses: [1HR9NZM8B2, 1T9MVT21YB]
sources:
  - url: https://en.wikipedia.org/wiki/Transmission_line
---

## Definition

A *transmission line* is a two-conductor structure, uniform along an axis with coordinate $z$, that carries a [[TEM or quasi-TEM mode|1T9MVT21YB]].
It is modelled by four constants per unit length.
They are the series resistance $R \ge 0$, series inductance $L > 0$, shunt conductance $G \ge 0$ and shunt capacitance $C > 0$.
The voltage $V(z, t)$ between the conductors and the current $I(z, t)$ along them satisfy the [[telegrapher's equations|1HR9NZM8B2]]
$$\frac{\partial V}{\partial z} = -R I - L \frac{\partial I}{\partial t}, \qquad \frac{\partial I}{\partial z} = -G V - C \frac{\partial V}{\partial t}.$$
Consider time-harmonic signals with time factor $e^{j\omega t}$.
The *propagation constant* of the line is $\gamma = \sqrt{(R + j\omega L)(G + j\omega C)}$.
Its *characteristic impedance* is $Z_0 = \sqrt{(R + j\omega L)/(G + j\omega C)}$.
Both square roots are taken with positive real part.

## Remarks

Every time-harmonic solution is $V(z) = V^+ e^{-\gamma z} + V^- e^{\gamma z}$ and $I(z) = (V^+ e^{-\gamma z} - V^- e^{\gamma z})/Z_0$, a forward and a backward wave.
A lossless line ($R = G = 0$) has $Z_0 = \sqrt{L/C}$, $\gamma = j\omega\sqrt{LC}$ and wave speed $1/\sqrt{LC}$.
A lossless line of length $\ell$ terminated by a load $Z_L$ has input impedance $Z_{\mathrm{in}} = Z_0 \dfrac{Z_L + j Z_0 \tan(\beta\ell)}{Z_0 + j Z_L \tan(\beta\ell)}$ with $\beta = \omega\sqrt{LC}$.
Example: a quarter-wave line, $\beta\ell = \pi/2$, gives $Z_{\mathrm{in}} = Z_0^2 / Z_L$, which is used for impedance matching.
Non-example: a hollow rectangular metal pipe has a single conductor and no TEM mode, so it is a waveguide but not a transmission line in this sense.
