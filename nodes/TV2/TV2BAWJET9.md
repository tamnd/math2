---
tag: TV2BAWJET9
kind: definition
name: Shock wave in gases
msc: [76L05, 76N15, 35L67]
defines: FRVV0NHBXT
uses: [JSDMGGTG7G, RW0JK9VDZE, S4XMYJ3V42, SN4J6KP03C]
sources:
  - url: https://en.wikipedia.org/wiki/Shock_wave
---

## Definition

Consider one-dimensional flow of a polytropic gas with adiabatic exponent $\gamma > 1$.
The state is given by the density $\rho > 0$, the velocity $u$ and the pressure $p > 0$, and the specific enthalpy is $h = \dfrac{\gamma p}{(\gamma - 1)\rho}$.
Let a weak solution of the [[Euler equations|RW0JK9VDZE]] have a jump along the line $x = \sigma t$.
On one side it has the constant state $(\rho_1, u_1, p_1)$, and on the other the constant state $(\rho_2, u_2, p_2) \ne (\rho_1, u_1, p_1)$.
Let $w_i = u_i - \sigma$ be the velocities relative to the jump, for $i = 1, 2$.
The jump is a *shock wave* if the following hold.

1. The mass flux $m = \rho_1 w_1 = \rho_2 w_2$ across the jump is not zero.
2. The momentum balance $p_1 + \rho_1 w_1^2 = p_2 + \rho_2 w_2^2$ holds.
3. The energy balance $h_1 + \tfrac12 w_1^2 = h_2 + \tfrac12 w_2^2$ holds.
4. The gas is compressed when it crosses the jump. So the density is larger on the downstream side, towards which the gas moves relative to the jump.

## Remarks

Clauses 1 to 3 are the [[Rankine–Hugoniot conditions|S4XMYJ3V42]] for the Euler equations, written in the frame of the jump.
Clause 4 is the admissibility condition.
For a polytropic gas it is equivalent to an increase of the entropy across the jump.
It is also equivalent to supersonic relative flow upstream and subsonic relative flow downstream, measured with the local [[speed of sound|SN4J6KP03C]].
A jump with $m = 0$ is a contact discontinuity: then $w_1 = w_2 = 0$ and $p_1 = p_2$, and only the density may jump.

Example: take $\gamma = 1.4$, $\sigma = 0$, side $1$ on the left and upstream, with state $\rho_1 = 1$, $p_1 = 1$, $u_1 = 2\sqrt{1.4}$, so the upstream Mach number is $2$.
The downstream state $\rho_2 = 8/3$, $u_2 = 3\sqrt{1.4}/4$, $p_2 = 4.5$ gives $m = 2\sqrt{1.4}$ on both sides, both sides of clause 2 equal $6.6$, and both sides of clause 3 equal $6.3$.
Since $\rho_2 > \rho_1$, it is a shock wave.

Non-example: the same two states with the roles of upstream and downstream exchanged satisfy clauses 1 to 3, but the gas would expand across the jump.
This expansion shock fails clause 4 and does not occur in nature.
