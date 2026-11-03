---
tag: RWZ4JG3RE1
kind: definition
name: Premixed flame
msc: [80A25, 76V05]
defines: 5P38MRV478
uses: [SXSCYXH068, M37M411KP7, TAAHWE917M]
sources:
  - url: https://en.wikipedia.org/wiki/Premixed_flame
---

## Definition

Take the reacting flow model of [[combustion theory|SXSCYXH068]] in one space variable $x$, for a gas at rest.
Let $T(x, t)$ be the temperature, $Y(x, t)$ the fuel mass fraction and $\omega(T, Y)$ the reaction rate.
Let $(T_u, Y_u)$ with $Y_u > 0$ be the state of the fresh mixture, and $(T_b, 0)$ the state of the burnt gas, with $T_b = T_u + q Y_u / c_p$.
A *planar premixed flame* is a [[travelling wave|M37M411KP7]] solution
$$T(x, t) = \Theta(x + S_L t), \qquad Y(x, t) = \Phi(x + S_L t)$$
with speed $S_L > 0$ such that:

1. $(\Theta(\xi), \Phi(\xi)) \to (T_u, Y_u)$ as $\xi \to -\infty$;
2. $(\Theta(\xi), \Phi(\xi)) \to (T_b, 0)$ as $\xi \to +\infty$.

The flame moves towards $x = -\infty$, into the fresh mixture, and $S_L$ is the *laminar burning velocity*.
A premixed flame in general is a reaction zone separating fresh premixed gas from burnt gas and moving into the fresh gas.

## Remarks

The Arrhenius rate is positive at $T_u$, so the fresh state is not exactly at rest and no exact travelling wave exists.
The standard fix sets $\omega = 0$ below an ignition temperature between $T_u$ and $T_b$.
With this cut-off, the travelling wave exists and its speed is unique, as for other ignition-type [[reaction–diffusion systems|TAAHWE917M]].
Scaling: if $\kappa$ is the thermal diffusivity and $\tau$ the reaction time, then $S_L$ is of order $\sqrt{\kappa / \tau}$ and the flame thickness is of order $\kappa / S_L$.
Check of the burnt state: when $\kappa = D$, the quantity $H = T + qY/c_p$ solves the heat equation with no source.
A bounded travelling wave keeps $H$ equal to its value $T_u + q Y_u / c_p = T_b$ in the fresh gas, so $Y = 0$ gives $T = T_b$.
Non-example: in a diffusion flame, fuel and oxidiser arrive from opposite sides, and the flame does not propagate into a fresh mixture.
