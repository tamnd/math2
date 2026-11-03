---
tag: 3PMZ8MDCYN
kind: statement
role: proposition
name: Bridgman's thermodynamic equations
msc: [80A10, 26B12]
uses: [0ZCSMYHTBP, 09EGC6F8PT, SPY89W0RJ7, 722RZK72P5, RBG5ZBM35Y, SYYGZ18FF5, MAHDE6JZYT]
about: [MKZW03Q590]
sources:
  - url: https://en.wikipedia.org/wiki/Bridgman%27s_thermodynamic_equations
same_as:
  wikidata: Q4966898
  wikipedia: Bridgman's thermodynamic equations
---

## Statement

Let a closed simple system have its equilibrium states described by temperature $T$ and pressure $p$.
Let every state quantity be a continuously differentiable function of $(T, p)$.
This applies to the volume $V$, the [[entropy|SPY89W0RJ7]] $S$, the [[enthalpy|722RZK72P5]] $H$ and the [[Gibbs free energy|RBG5ZBM35Y]] $G$.
For state quantities $x, z$ set
$$(\partial x)_z = \frac{\partial(x, z)}{\partial(T, p)},$$
the [[Jacobian determinant|0ZCSMYHTBP]] of $(x, z)$ with respect to $(T, p)$.
Then:

1. For state quantities $x, y, z$ with $(\partial y)_z \ne 0$, the [[partial derivative|09EGC6F8PT]] of $x$ with respect to $y$ at fixed $z$ is $\left(\dfrac{\partial x}{\partial y}\right)_z = \dfrac{(\partial x)_z}{(\partial y)_z}$.
2. $(\partial x)_z = -(\partial z)_x$ for all $x, z$.
3. With the [[heat capacity|SYYGZ18FF5]] $C_p = T (\partial S / \partial T)_p$ at constant pressure, the following hold: $(\partial T)_p = 1$, $(\partial V)_p = (\partial V / \partial T)_p$, $(\partial S)_p = C_p / T$, $(\partial H)_p = C_p$, $(\partial G)_p = -S$, $(\partial V)_T = -(\partial V / \partial p)_T$, $(\partial S)_T = (\partial V / \partial T)_p$, $(\partial G)_T = -V$.

## Remarks

Item 1 is the chain rule for Jacobians: $\partial(x, z)/\partial(y, z) = (\partial x / \partial y)_z$, and Jacobians multiply under change of variables.
Item 2 holds because swapping two rows changes the sign of a determinant.
In item 3, $(\partial H)_p = C_p$ uses $dH = T \, dS + V \, dp$, and $(\partial S)_T = -(\partial S / \partial p)_T = (\partial V / \partial T)_p$ uses a [[Maxwell relation|MAHDE6JZYT]].
The entries for $G$ use $dG = -S \, dT + V \, dp$.
Example: the cooling of a substance under adiabatic expansion.
One has $(\partial T / \partial p)_S = (\partial T)_S / (\partial p)_S = (\partial S)_T / (\partial S)_p = T (\partial V / \partial T)_p / C_p$.
Since $(\partial V / \partial T)_p > 0$ for most substances, reducing the pressure at constant entropy lowers the temperature.

## Explanations

### L1 human

Thermodynamics has a great many partial derivatives, such as the change of temperature with pressure at fixed entropy.
Bridgman's equations give a mechanical recipe to express any of them through a few measurable quantities.
One writes each derivative as a ratio of two table entries.

### L2 human

Percy Bridgman's table lists $(\partial x)_z$ for all pairs among $T, p, V, S, U, H, F, G$ in terms of $C_p$, $(\partial V / \partial T)_p$, $(\partial V / \partial p)_T$ and the state variables.
Every first derivative of one state quantity with respect to another at fixed third then follows from item 1.
The method is a systematic use of the Jacobian calculus together with the Maxwell relations.
