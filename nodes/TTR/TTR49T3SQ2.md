---
tag: TTR49T3SQ2
kind: definition
name: Darrieus–Landau instability
msc: ["76E17", 76V05, 80A25]
defines: 6R08PSWZJH
uses: [5P38MRV478, H028A17Z55, 2JZ0C15A9C, RW0JK9VDZE]
sources:
  - url: https://en.wikipedia.org/wiki/Darrieus–Landau_instability
---

## Definition

Model a planar [[premixed flame|5P38MRV478]] as a surface in $\R^3$ that separates fresh gas of density $\rho_u$ from burnt gas of density $\rho_b$.
Let $r = \rho_u / \rho_b$ be the expansion ratio.
Assume:

1. on each side the gas is [[incompressible|2JZ0C15A9C]] and inviscid and solves the [[Euler equations|RW0JK9VDZE]], and gravity is neglected;
2. the front moves at the constant normal speed $S_L$ relative to the fresh gas;
3. mass and normal momentum are conserved across the front.

Perturb the plane front by a small wrinkle of wavenumber $k > 0$ proportional to $e^{i k y + \sigma t}$.
The linearised problem gives the growth rate
$$\sigma = \frac{S_L k}{r + 1} \left( \sqrt{r^3 + r^2 - r} - r \right).$$
The *Darrieus–Landau instability* is the instability of the front expressed by $\sigma > 0$.

## Remarks

The growth rate is positive for every $k > 0$ exactly when $r > 1$: indeed $\sqrt{r^3 + r^2 - r} > r$ is equivalent to $r^3 > r$.
Example: for $r = 6$, a typical value for hydrocarbon flames, $\sigma = S_L k (\sqrt{246} - 6)/7 \approx 1.38 \, S_L k$.
Non-example: for $r = 1$ there is no density jump, the formula gives $\sigma = 0$, and the wrinkle neither grows nor decays.
Since $\sigma$ grows linearly in $k$ without bound, the thin-front model is ill-posed for short waves.
In a real flame, diffusion of heat and species stabilises wavelengths comparable to the flame thickness.
This is the subject of the Markstein correction to the flame speed.
