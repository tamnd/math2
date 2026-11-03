---
tag: HGX0T0XPJ7
kind: definition
name: Interference
msc: [78A10, 78A40]
defines: KX1EXRW47E
uses: [0KW2X0TFBX, 0ZZRSX91QR]
sources:
  - url: https://en.wikipedia.org/wiki/Wave_interference
---

## Definition

Let $U_1$ and $U_2$ be complex amplitudes of two monochromatic scalar waves of the same frequency at a point.
Write $U_j = \sqrt{I_j} \, e^{i \varphi_j}$ with $I_j = \abs{U_j}^2$ the intensity and $\varphi_j$ the phase.
The intensity of the superposition is
$$I = \abs{U_1 + U_2}^2 = I_1 + I_2 + 2 \sqrt{I_1 I_2} \cos(\Delta\varphi), \qquad \Delta\varphi = \varphi_2 - \varphi_1.$$
*Interference* is the presence of the term $2 \sqrt{I_1 I_2} \cos(\Delta\varphi)$, the *interference term*.
The interference is *constructive* when $\Delta\varphi \in 2\pi\Z$ and *destructive* when $\Delta\varphi \in \pi + 2\pi\Z$.

## Remarks

The formula follows from $\abs{a + b}^2 = \abs{a}^2 + \abs{b}^2 + 2 \operatorname{Re}(a \bar b)$, using the [[modulus|0KW2X0TFBX]] and [[argument|0ZZRSX91QR]] of complex numbers.
Over a region where $\Delta\varphi$ varies, the intensity oscillates between $I_{\max} = (\sqrt{I_1} + \sqrt{I_2})^2$ and $I_{\min} = (\sqrt{I_1} - \sqrt{I_2})^2$.
The *visibility* of the fringes is $V = (I_{\max} - I_{\min}) / (I_{\max} + I_{\min}) = 2\sqrt{I_1 I_2} / (I_1 + I_2)$.

Example: two waves of equal intensity $I_0$ give $I = 2 I_0 (1 + \cos \Delta\varphi) = 4 I_0 \cos^2(\Delta\varphi / 2)$.
This is $4 I_0$ at constructive points and $0$ at destructive points, with visibility $1$.

Non-example: for vector fields $E_1, E_2$ the interference term is $2 \operatorname{Re}(E_1 \cdot \overline{E_2})$.
Two waves with orthogonal linear polarisations have $E_1 \cdot \overline{E_2} = 0$, so their intensities simply add and there are no fringes.
