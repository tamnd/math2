---
tag: VK4FWH6CY0
kind: statement
role: proposition
name: Normal shock relations
msc: [76L05, 76N15]
uses: [FRVV0NHBXT, GFHJ858AN1, SN4J6KP03C, S4XMYJ3V42]
about: [FRVV0NHBXT]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_shock_tables
---

## Statement

Let a polytropic gas with adiabatic exponent $\gamma > 1$ flow steadily in one dimension through a stationary [[shock wave|FRVV0NHBXT]].
Let $\rho_1, u_1, p_1, T_1$ be the density, velocity, pressure and temperature upstream, with $u_1 > 0$.
Let $\rho_2, u_2, p_2, T_2$ be the same quantities downstream.
Let $M_1 = u_1 / c_1$ and $M_2 = u_2 / c_2$ be the upstream and downstream [[Mach numbers|GFHJ858AN1]], where $c_i = \sqrt{\gamma p_i / \rho_i}$.
Then $M_1 > 1$, and

1. $\dfrac{\rho_2}{\rho_1} = \dfrac{u_1}{u_2} = \dfrac{(\gamma + 1) M_1^2}{(\gamma - 1) M_1^2 + 2}$,
2. $\dfrac{p_2}{p_1} = \dfrac{2\gamma M_1^2 - (\gamma - 1)}{\gamma + 1}$,
3. $\dfrac{T_2}{T_1} = \dfrac{p_2}{p_1} \cdot \dfrac{\rho_1}{\rho_2}$,
4. $M_2^2 = \dfrac{(\gamma - 1) M_1^2 + 2}{2\gamma M_1^2 - (\gamma - 1)}$, and $M_2 < 1$.

## Remarks

The proof starts from the [[Rankine–Hugoniot conditions|S4XMYJ3V42]] $\rho_1 u_1 = \rho_2 u_2$, $p_1 + \rho_1 u_1^2 = p_2 + \rho_2 u_2^2$ and $h_1 + u_1^2/2 = h_2 + u_2^2/2$, with $h = \gamma p / ((\gamma - 1)\rho)$.
Eliminating $p_2$ and $\rho_2$ gives a quadratic equation for $u_2$.
One root is $u_2 = u_1$, the trivial solution without a jump, and the other root gives relation 1.
Relations 2 to 4 follow, and the condition that the gas is compressed across the shock is exactly $M_1 > 1$.

Example: for air, $\gamma = 1.4$, at $M_1 = 2$ the relations give $\rho_2/\rho_1 = 8/3$, $p_2/p_1 = 4.5$, $T_2/T_1 = 1.6875$ and $M_2 = 1/\sqrt{3} \approx 0.577$.

As $M_1 \to \infty$ the density ratio tends to $(\gamma + 1)/(\gamma - 1)$, which is $6$ for air, while the pressure ratio grows without bound.
The algebraic formulas also give a solution for $M_1 < 1$, but then $\rho_2 < \rho_1$ and the entropy would decrease, so that jump is not a shock wave.

## Explanations

### L1 human

When air crosses a shock that stands across the flow, it slows down suddenly and becomes denser, hotter and more compressed.
These formulas give all the jumps from one number, the Mach number of the incoming air.
At twice the speed of sound, the pressure jumps by a factor $4.5$ and the air leaves the shock slower than sound.
However strong the shock, air can be compressed at most six times by a single normal shock.

### L2 human

The relations are the Rankine–Hugoniot conditions solved explicitly for a polytropic gas, with the trivial solution removed.
They are tabulated in engineering as normal shock tables.
An [[oblique shock|DSYRY5HCDD]] obeys the same relations with $M_1$ replaced by the normal component $M_1 \sin\beta$, where $\beta$ is the shock angle.
In a moving frame they give the speed of a shock running into gas at rest, as in the [[shock tube problem|9F314R2K5Q]].
