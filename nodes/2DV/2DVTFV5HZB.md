---
tag: 2DVTFV5HZB
kind: definition
name: Compressibility factor
msc: [80A10, 76N15]
defines: 14V3D1ZHVY
uses: [5EKTEE00FZ, VXVGVDSJ0W, N7R0H2VNDJ, X576BQTPQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Compressibility_factor
---

## Definition

Consider a fluid in [[thermodynamic equilibrium|5EKTEE00FZ]] with pressure $p$, absolute temperature $T$ and molar volume $V_m$, the volume per mole.
Let $R$ be the molar gas constant.
The *compressibility factor* of the fluid in this state is
$$Z = \frac{p V_m}{R T}.$$

## Remarks

For an [[ideal gas|N7R0H2VNDJ]], the [[ideal gas law|VXVGVDSJ0W]] $p V_m = RT$ gives $Z = 1$ in every state.
For a gas that obeys the [[van der Waals equation|X576BQTPQ5]] $(p + a/V_m^2)(V_m - b) = RT$ with constants $a, b > 0$, solving for $p$ gives
$$Z = \frac{V_m}{V_m - b} - \frac{a}{R T V_m},$$
so $Z \ne 1$ in general, and $Z \to 1$ as $V_m \to \infty$.
A non-example: the ratio $pV/(RT)$ with the total volume $V$ in place of $V_m$ is not $Z$.
For $n$ moles it equals $nZ$, because it does not use the volume per mole.
The virial expansion writes $Z = 1 + B(T)/V_m + C(T)/V_m^2 + \cdots$.
By the law of corresponding states, $Z$ is approximately the same function of the reduced temperature and reduced pressure for many gases.
