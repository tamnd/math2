---
tag: G30CMRM06T
kind: statement
role: proposition
name: Curzon–Ahlborn efficiency
msc: [80A10, 80A05]
uses: [QYK995DD21, S7XFW04T3V, Z686C32X8S, F3DHZ45H6A]
about: [QYK995DD21, S7XFW04T3V]
sources:
  - url: https://en.wikipedia.org/wiki/Endoreversible_thermodynamics
---

## Statement

Let a hot reservoir have temperature $T_h$ and a cold reservoir temperature $T_c$, with $0 < T_c < T_h$.
Consider a steady [[heat engine|S7XFW04T3V]] whose working fluid takes in heat at temperature $T_1$ and gives off heat at temperature $T_2$, with $T_c < T_2 < T_1 < T_h$.
Assume the heat flow rates obey linear transfer laws
$$q_h = \kappa_h (T_h - T_1), \qquad q_c = \kappa_c (T_2 - T_c),$$
with constants $\kappa_h, \kappa_c > 0$.
Assume the engine is [[reversible|F3DHZ45H6A]] inside, so that $q_h / T_1 = q_c / T_2$.
Let $P = q_h - q_c$ be the power.
Then the maximum of $P$ over the admissible $T_1, T_2$ is
$$P_{\max} = \frac{\kappa_h \kappa_c}{\kappa_h + \kappa_c} \left( \sqrt{T_h} - \sqrt{T_c} \right)^2,$$
and at this maximum the [[thermal efficiency|Z686C32X8S]] $P / q_h$ equals
$$\eta_{CA} = 1 - \sqrt{\frac{T_c}{T_h}}.$$

## Remarks

The internal reversibility condition expresses $q_c$ through $q_h$ and the ratio $T_2 / T_1$.
Eliminating one temperature with the transfer laws leaves a function of one variable, and setting its derivative to $0$ gives the optimum.
The efficiency at maximum power does not depend on $\kappa_h$ and $\kappa_c$.
For $T_h = 1200$ K and $T_c = 300$ K, the Carnot efficiency is $0.75$ and $\eta_{CA} = 1 - 1/2 = 0.5$.
The linear transfer law is needed: other laws, such as radiative heat transfer, give other values of the efficiency at maximum power.

## Explanations

### L1 human

A Carnot engine has the best possible efficiency, but it runs infinitely slowly and so gives no power.
A real engine must take in heat quickly, and heat flows quickly only across a temperature gap.
Running the engine for the most power, rather than the best efficiency, gives the efficiency $1 - \sqrt{T_c/T_h}$.
This value is often close to the efficiency of real power plants.

### L2 human

This is the basic result of [[finite-time thermodynamics|QYK995DD21]].
The model is endoreversible: all losses sit in the heat transfer to and from the reservoirs, and the engine inside is reversible.
The result shows a trade-off between power and efficiency that classical thermodynamics, which studies only reversible limits, cannot see.
Since $\sqrt{T_c/T_h} > T_c/T_h$, the value $\eta_{CA}$ is always below the Carnot efficiency, as it must be.
