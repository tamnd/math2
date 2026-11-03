---
tag: SGQGR3VN5M
kind: definition
name: van der Waals equation
msc: [80A10, 82D05, 82B26]
defines: X576BQTPQ5
uses: [YPT3SJSS5T, N7R0H2VNDJ, AJ8M9MGZGF]
sources:
  - url: https://en.wikipedia.org/wiki/Van_der_Waals_equation
---

## Definition

Let $R$ be the molar gas constant and let $a > 0$ and $b > 0$ be constants of a substance.
The *van der Waals equation* is the following [[equation of state|YPT3SJSS5T]].
It relates the pressure $p$, the volume $V > nb$, the [[thermodynamic temperature|AJ8M9MGZGF]] $T$ and the amount $n$ in moles:
$$\left( p + \frac{a n^2}{V^2} \right) (V - n b) = n R T.$$
A fluid that satisfies it is a *van der Waals fluid*.

## Remarks

Solved for the pressure and written with the molar volume $V_m = V/n > b$, it reads
$$p = \frac{RT}{V_m - b} - \frac{a}{V_m^2}.$$
The constant $b$ is the excluded volume per mole, and $a/V_m^2$ is the reduction of pressure by the attraction between molecules.
The critical point, where $\partial p / \partial V_m = \partial^2 p / \partial V_m^2 = 0$, is at $V_c = 3b$, $T_c = 8a/(27Rb)$ and $p_c = a/(27 b^2)$.
Below $T_c$ the isotherms are not monotone, and the part with $\partial p / \partial V_m > 0$ is unstable.

Example: for carbon dioxide, approximate values are $a \approx 0.364\,\mathrm{Pa\,m^6\,mol^{-2}}$ and $b \approx 4.27 \times 10^{-5}\,\mathrm{m^3\,mol^{-1}}$.
They give $T_c = 8a/(27Rb) \approx 304\,\mathrm{K}$, close to the measured critical temperature of about $304\,\mathrm{K}$, because they are usually fitted to the critical data.
In the limit $a, b \to 0$, or at large $V_m$, the equation becomes $pV = nRT$, the equation of the [[ideal gas|N7R0H2VNDJ]].

Non-example: the Redlich–Kwong equation of state $p = RT/(V_m - b) - a/(\sqrt{T}\, V_m (V_m + b))$ is not a van der Waals equation.
Its attraction term depends on $T$ and is not of the form $a/V_m^2$ with constant $a$.

The equation predicts the critical compressibility factor $p_c V_c / (R T_c) = 3/8$ for every fluid, while measured values are mostly between $0.23$ and $0.30$; it is qualitatively right but not quantitatively accurate.
