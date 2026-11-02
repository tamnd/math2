---
tag: FH2A1PCXNB
kind: definition
name: Telegrapher's equations
msc: [35L40, 35Q60, 35L05]
defines: 1HR9NZM8B2
uses: [92C3S03AQZ, GC5BDZ6QBC, 5EHD2XBQDG]
sources:
  - url: https://en.wikipedia.org/wiki/Telegrapher%27s_equations
---

## Definition

Let $L > 0$, $C > 0$, $R \ge 0$ and $G \ge 0$ be constants: the inductance, capacitance, resistance and conductance per unit length of a line.
The *telegrapher's equations* are the system of [[partial differential equations|GC5BDZ6QBC]] for the voltage $V(x, t)$ and the current $I(x, t)$, with $x \in \R$ and $t \in \R$:
$$\frac{\partial V}{\partial x} = -L \frac{\partial I}{\partial t} - R I, \qquad \frac{\partial I}{\partial x} = -C \frac{\partial V}{\partial t} - G V.$$
It is a first-order [[hyperbolic system|92C3S03AQZ]].

## Remarks

For $C^2$ solutions, differentiating the first equation in $x$ and using the second gives the telegraph equation
$$V_{xx} = L C\, V_{tt} + (R C + G L)\, V_t + R G\, V,$$
and the same equation holds for $I$.
Example: with $R = G = 0$, for any $F \in C^1(\R)$ the pair $V = F(x - ct)$, $I = \sqrt{C/L}\, F(x - ct)$ with $c = 1/\sqrt{LC}$ is a solution.
Indeed $V_x = F'$ and $-L I_t = L c \sqrt{C/L}\, F' = F'$, and $I_x = \sqrt{C/L}\, F'$ and $-C V_t = C c F' = \sqrt{C/L}\, F'$.
Non-example: with $R > 0$ and $G = 0$, this undamped pair fails the first equation, since the extra term $-R I$ is nonzero when $F \ne 0$.
When $R = G = 0$ the telegraph equation is the [[wave equation|5EHD2XBQDG]] with speed $1/\sqrt{LC}$.
