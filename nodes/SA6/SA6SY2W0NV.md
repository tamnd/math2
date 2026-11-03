---
tag: SA6SY2W0NV
kind: definition
name: Holography
msc: [78A10, 78A55]
defines: A97MM8JNKF
uses: [KX1EXRW47E, NM024G378A]
sources:
  - url: https://en.wikipedia.org/wiki/Holography
---

## Definition

Let $O(x)$ and $R(x)$ be the complex amplitudes of a monochromatic object wave and a reference wave on the plane of a recording medium.
The two waves have the same frequency.
*Recording*: the medium is exposed to the intensity of their [[interference|KX1EXRW47E]],
$$I = \abs{O + R}^2 = \abs{O}^2 + \abs{R}^2 + O \overline{R} + \overline{O} R.$$
The developed medium, the *hologram*, has amplitude transmittance $t = t_0 + \beta I$ with real constants $t_0$ and $\beta$, in the linear regime.
*Reconstruction*: the hologram is lit by the reference wave $R$, and the transmitted wave is
$$t R = \bigl(t_0 + \beta \abs{O}^2 + \beta \abs{R}^2\bigr) R + \beta \abs{R}^2 \, O + \beta R^2 \, \overline{O}.$$
*Holography* is this two-step process.

## Remarks

When $\abs{R}$ is constant on the plate, the term $\beta \abs{R}^2 O$ is a constant multiple of the object wave, so the object is seen as a virtual image.
The term $\beta R^2 \overline{O}$ is the conjugate wave and forms a real image.
The first term is the reference wave, modulated in amplitude.
With an off-axis reference wave, these three parts leave the hologram in different directions and can be separated.

Example: let $O$ and $R$ be [[plane waves|NM024G378A]] of equal amplitude $1$ with transverse wave vectors $k_O$ and $k_R$ in the plate.
Then $I(x) = 2 + 2\cos((k_O - k_R) \cdot x)$, so the hologram is a sinusoidal grating.
Lit by $R$, it diffracts a wave proportional to $O$ in the direction of the original object wave.

Non-example: a photograph records $\abs{O}^2$ alone, with no reference wave.
The phase of $O$ is lost, and lighting the photograph does not reconstruct the object wave.
