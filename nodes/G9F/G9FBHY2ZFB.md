---
tag: G9FBHY2ZFB
kind: definition
name: Stokes parameters
msc: [78A10, 78A40]
defines: 1WA9ASC6NF
uses: [PJ8ZSJ0QDW, D3XTQ5Z2QA, NM024G378A]
sources:
  - url: https://en.wikipedia.org/wiki/Stokes_parameters
---

## Definition

Consider a quasi-monochromatic [[plane wave|NM024G378A]] that travels along the $z$-axis.
Write its transverse electric field as $\mathrm{Re}\big((E_x \mathbf{e}_x + E_y \mathbf{e}_y) e^{-i\omega t}\big)$, where the complex amplitudes $E_x$ and $E_y$ may vary slowly and randomly in time.
Let $\langle \cdot \rangle$ denote the time average.
The *Stokes parameters* of the wave are the real numbers
$$S_0 = \langle \abs{E_x}^2 + \abs{E_y}^2 \rangle, \qquad S_1 = \langle \abs{E_x}^2 - \abs{E_y}^2 \rangle,$$
$$S_2 = 2\,\mathrm{Re}\,\langle E_x \overline{E_y} \rangle, \qquad S_3 = -2\,\mathrm{Im}\,\langle E_x \overline{E_y} \rangle.$$
The vector $S = (S_0, S_1, S_2, S_3)$ is the *Stokes vector*.

## Remarks

Every Stokes vector satisfies $S_0^2 \ge S_1^2 + S_2^2 + S_3^2$, by the Cauchy–Schwarz inequality for time averages.
Equality holds exactly for fully polarized light.
The ratio $p = \sqrt{S_1^2 + S_2^2 + S_3^2} / S_0$ is the *degree of polarization*, with $0 \le p \le 1$.

Example: light polarized at $45^\circ$ has constant amplitudes $E_x = E_y = 1/\sqrt{2}$.
Then $S_0 = 1$, $S_1 = 0$, $E_x \overline{E_y} = 1/2$, so $S_2 = 1$ and $S_3 = 0$.
The equality $S_0^2 = S_1^2 + S_2^2 + S_3^2$ holds, as it must for fully polarized light.

Non-example: the vector $(1, 1, 1, 0)$ is not the Stokes vector of any light.
It fails the inequality, since $1^2 < 1^2 + 1^2$.

The sign of $S_3$, and thus which circular state counts as right-handed, depends on the convention for the time factor; texts differ on this point.
Some texts write $I, Q, U, V$ for $S_0, S_1, S_2, S_3$.
