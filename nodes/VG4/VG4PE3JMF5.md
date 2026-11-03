---
tag: VG4PE3JMF5
kind: definition
name: Redlich–Kwong equation of state
msc: [80A10, 82D05]
defines: GYK0D2FNSR
uses: [YPT3SJSS5T, X576BQTPQ5, AJ8M9MGZGF]
sources:
  - url: https://en.wikipedia.org/wiki/Redlich–Kwong_equation_of_state
---

## Definition

Let $R$ be the molar gas constant, and let $T_c$ and $p_c$ be the critical temperature and pressure of a substance.
Put
$$a = \Omega_a \frac{R^2 T_c^{5/2}}{p_c}, \qquad b = \Omega_b \frac{R T_c}{p_c}, \qquad \Omega_a = \frac{1}{9(2^{1/3} - 1)} \approx 0.42748, \qquad \Omega_b = \frac{2^{1/3} - 1}{3} \approx 0.08664.$$
The *Redlich–Kwong equation of state* is the [[equation of state|YPT3SJSS5T]] relating the pressure $p$, the [[thermodynamic temperature|AJ8M9MGZGF]] $T > 0$ and the molar volume $V_m > b$:
$$p = \frac{R T}{V_m - b} - \frac{a}{\sqrt{T}\, V_m (V_m + b)}.$$

## Remarks

The values of $\Omega_a$ and $\Omega_b$ are the ones for which the critical point of the equation is exactly at $T_c$ and $p_c$, that is $\partial p / \partial V_m = \partial^2 p / \partial V_m^2 = 0$ there.
Then the critical compressibility factor is $p_c V_c / (R T_c) = 1/3$ for every substance.
Multiplied out, the equation is a cubic in $V_m$, so it can be solved in closed form for the volume.

Example: at large $V_m$ the attraction term behaves like $a / (\sqrt{T}\, V_m^2)$.
So the equation looks like the [[van der Waals equation|X576BQTPQ5]] with the temperature-dependent constant $a/\sqrt{T}$.
As $V_m \to \infty$ it gives $p V_m / (RT) \to 1$, the ideal gas limit.
Its second virial coefficient is $B(T) = b - a/(R T^{3/2})$.

Non-example: the van der Waals equation $p = RT/(V_m - b) - a/V_m^2$ has an attraction term that does not depend on $T$ and lacks the factor $V_m + b$, so it is not of the Redlich–Kwong form.
