---
tag: F3GWY2CXBR
kind: definition
name: Polarization of light
msc: [78A10, 78A25]
defines: PJ8ZSJ0QDW
uses: [NM024G378A, YZ7Q9DP8RT, 0ZZRSX91QR]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_(waves)
---

## Definition

Let a monochromatic [[plane wave|NM024G378A]] of angular frequency $\omega$ and wave number $k$ travel along the $z$ axis.
Its [[electric field|YZ7Q9DP8RT]] is
$$\mathbf E(z, t) = \operatorname{Re}\bigl[(E_x \mathbf e_x + E_y \mathbf e_y) \, e^{i(kz - \omega t)}\bigr],$$
with complex amplitudes $(E_x, E_y) \ne (0, 0)$ and unit vectors $\mathbf e_x, \mathbf e_y$.
At fixed $z$, the tip of $\mathbf E$ traces an ellipse, possibly degenerate, called the *polarization ellipse*.
Let $\delta$ be the phase difference $\arg E_y - \arg E_x$ when both amplitudes are nonzero.
The *polarization* of the wave is:

1. *linear* if $E_x = 0$, or $E_y = 0$, or $\delta \in \pi\Z$;
2. *circular* if $\abs{E_x} = \abs{E_y}$ and $\delta \in \frac{\pi}{2} + \pi\Z$;
3. *elliptical* otherwise.

## Remarks

The pair $(E_x, E_y)$ is the Jones vector of the wave; multiplying it by a nonzero complex number changes only the amplitude and the time origin, not the polarization state.
In the circular case, the sign of $\sin\delta$ gives the sense of rotation; the names left and right for the two senses follow different conventions in different fields.
Light that is not monochromatic can be *unpolarized* or *partially polarized*, and is then described by [[Stokes parameters|1WA9ASC6NF]].

Example: $(E_x, E_y) = (1, i)$ gives, at $z = 0$, $\mathbf E = (\cos \omega t, \sin \omega t)$.
Its tip moves on the unit circle, and indeed $\abs{E_x} = \abs{E_y}$ and $\delta = \pi/2$, so the light is circularly polarized.

Non-example: $(E_x, E_y) = (1, 2i)$ gives $\mathbf E = (\cos\omega t, 2\sin\omega t)$, an ellipse with unequal axes.
It has $\delta = \pi/2$ but $\abs{E_x} \ne \abs{E_y}$, so it is not circular; it is elliptical.
