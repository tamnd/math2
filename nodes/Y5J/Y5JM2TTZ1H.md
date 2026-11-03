---
tag: Y5JM2TTZ1H
kind: definition
name: Zoeppritz equations
msc: [74J20, 86A15, 74J05]
defines: QQQJM3SA2C
uses: [QR6R18G406, KBJTFMZWSF, EEPJJHC5JZ, GZ7E9GHQYB, KG2XWEMJ30]
sources:
  - url: https://en.wikipedia.org/wiki/Zoeppritz_equations
---

## Definition

Let two homogeneous isotropic elastic half-spaces $z < 0$ and $z > 0$ be welded along the plane $z = 0$.
Let medium $j \in \set{1, 2}$ have density $\rho_j$, P-speed $\alpha_j$ and S-speed $\beta_j$.
Let a [[plane|KBJTFMZWSF]] [[P-wave|EEPJJHC5JZ]] of unit amplitude travel in medium 1 in the $xz$-plane and hit the interface at the angle $\theta_1$ from the normal.
It produces a reflected P-wave at angle $\theta_1$ and a reflected SV-wave at angle $\varphi_1$.
It also produces a transmitted P-wave at angle $\theta_2$ and a transmitted SV-wave at angle $\varphi_2$, with
$$\frac{\sin\theta_1}{\alpha_1} = \frac{\sin\varphi_1}{\beta_1} = \frac{\sin\theta_2}{\alpha_2} = \frac{\sin\varphi_2}{\beta_2}$$
by [[Snell's law|QR6R18G406]].
Let $R_P, R_S, T_P, T_S$ be their displacement amplitudes.
The *Zoeppritz equations* are the four linear equations in $R_P, R_S, T_P, T_S$ stating that, at $z = 0$:

1. the horizontal displacement $u_x$ is continuous;
2. the vertical displacement $u_z$ is continuous;
3. the normal stress $\sigma_{zz}$ is continuous;
4. the shear stress $\sigma_{xz}$ is continuous.

Here $\sigma$ is the [[Cauchy stress|KG2XWEMJ30]], given by Hooke's law in each medium.

## Remarks

The coefficients of the system are trigonometric functions of the four angles times $\rho_j$, $\alpha_j$ and $\beta_j$; their exact signs depend on the chosen polarity conventions.
There is a similar system for an incident [[S-wave|GZ7E9GHQYB]].
Example: at normal incidence, $\theta_1 = 0$, no S-waves are produced, and with impedances $Z_j = \rho_j \alpha_j$ the system reduces to $1 + R = T$ and $Z_1(1 - R) = Z_2 T$ for displacements along the $z$-axis.
So $R = (Z_1 - Z_2)/(Z_1 + Z_2)$ and $T = 2Z_1/(Z_1 + Z_2)$; the pressure amplitude is reflected with the coefficient $(Z_2 - Z_1)/(Z_1 + Z_2)$, the form common in exploration seismology.
Non-example: for a liquid over a solid, the Zoeppritz system in this form does not apply.
A non-viscous liquid can slip along the interface, so clause 1 is dropped and clause 4 is replaced by $\sigma_{xz} = 0$.
Linear approximations for small contrasts, such as the Aki–Richards formula, are used in practice.
