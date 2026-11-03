---
tag: FNYD87Y8AK
kind: definition
name: Koiter shell model
msc: [74K25, 74B05, 74G65]
defines: F91VK64QRZ
uses: [DF7RPJHHY1, MAJ3DH7MZS, 9KHQR16P1B, T8ENJX1905, NWYZ9QBA84]
sources:
  - url: https://en.wikipedia.org/wiki/Plate_theory
---

## Definition

Let $S$ be the middle surface of a shell of thickness $h$, with metric $a_{\alpha\beta}$ (the [[first fundamental form|MAJ3DH7MZS]]) and [[second fundamental form|9KHQR16P1B]] $b_{\alpha\beta}$.
Let the material be isotropic and linearly elastic, with [[Young's modulus|T8ENJX1905]] $E$ and [[Poisson's ratio|NWYZ9QBA84]] $\nu$.
For a displacement $u$ of $S$, let $a(u)$ and $b(u)$ be the two fundamental forms of the deformed surface.
The change of metric is $\gamma_{\alpha\beta}(u) = \frac{1}{2}(a_{\alpha\beta}(u) - a_{\alpha\beta})$, and the change of curvature is $\rho_{\alpha\beta}(u) = b_{\alpha\beta}(u) - b_{\alpha\beta}$.
For a symmetric tensor $e_{\alpha\beta}$ on $S$ put
$$\mathcal{C}(e) = \frac{E}{1 - \nu^2} \left[ \nu \, (\operatorname{tr} e)^2 + (1 - \nu) \, e^{\alpha\beta} e_{\alpha\beta} \right],$$
with traces and raised indices taken with $a_{\alpha\beta}$.
Let $f$ be the load per unit area.
The *Koiter energy* is
$$J(u) = \frac{1}{2} \int_S \left[ h \, \mathcal{C}(\gamma(u)) + \frac{h^3}{12} \, \mathcal{C}(\rho(u)) \right] dS - \int_S f \cdot u \, dS.$$
Admissible displacements are those that satisfy the support conditions.
The *Koiter shell model* takes the displacement of the shell to be a stationary point of $J$ among them, in the stable case a minimiser.
In the *linear* Koiter model, $\gamma$ and $\rho$ are replaced by their linear parts in $u$.

## Remarks

Example: for a flat plate, $b_{\alpha\beta} = 0$, and the linear change of curvature of a transverse displacement $w$ is $\rho_{\alpha\beta} = \partial_\alpha \partial_\beta w$.
Then the bending term is $\frac{D}{2} \int [ (\Delta w)^2 - 2(1 - \nu)(\partial_1^2 w \, \partial_2^2 w - (\partial_1 \partial_2 w)^2) ]$ with $D = Eh^3/(12(1 - \nu^2))$, the energy of [[Kirchhoff–Love plate theory|9E6E0SCEYA]].

Non-example: an energy with only the membrane term $h\,\mathcal{C}(\gamma)$ is the membrane model; it fails to control bending and gives no unique answer for surfaces that admit inextensional deformations.

For the linear model on a clamped shell, existence and uniqueness of the minimiser in a suitable Sobolev space hold, by Korn-type inequalities on surfaces.
