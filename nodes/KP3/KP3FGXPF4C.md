---
tag: KP3FGXPF4C
kind: example
name: Pp-wave spacetime
msc: [83C35, 83C15, 83C20]
instance_of: [BY4QYYS788]
illustrates: [SJ0A4TZTFR]
uses: [4GTNM0WHDH, 0DEB0JMN0W, JRV1T69FYJ]
sources:
  - url: https://en.wikipedia.org/wiki/Pp-wave_spacetime
same_as:
  wikidata: Q3966083
  wikipedia: Pp-wave spacetime
---

## Example

Let $H \colon \R^3 \to \R$ be a smooth function of $(u, x, y)$.
On $\R^4$ with coordinates $(u, v, x, y)$, the *pp-wave* metric in Brinkmann form is
$$g = H(u, x, y)\, du^2 + 2\, du\, dv + dx^2 + dy^2.$$
Check that $g$ is Lorentzian: the $(u, v)$ block has determinant $-1$, and $dx^2 + dy^2$ is positive, so the signature is $(-, +, +, +)$.

The vector field $k = \partial_v$ is null, since $g_{vv} = 0$, and it is covariantly constant, $\nabla k = 0$.
The only nonzero component of the [[Ricci curvature|4GTNM0WHDH]] is
$$R_{uu} = -\frac{1}{2}\left(\frac{\partial^2 H}{\partial x^2} + \frac{\partial^2 H}{\partial y^2}\right).$$
So $g$ is a [[vacuum solution|JRV1T69FYJ]] exactly when $H$ is [[harmonic|0DEB0JMN0W]] in $(x, y)$ for each $u$.
For example $H = f(u)\,(x^2 - y^2)$, with any smooth $f$, gives a vacuum plane gravitational wave of the $+$ polarization and profile $f$.
If $H$ is not harmonic but $\Delta H \le 0$, then $R_{ab}$ is a nonnegative multiple of $k_a k_b$.
This is the stress–energy of null dust or of a null electromagnetic wave.

## Explanations

### L1 human

A pp-wave is a spacetime that carries a single wave travelling at the speed of light in a fixed direction, with flat wave fronts.
The letters pp stand for plane-fronted waves with parallel rays.
The function $H$ sets the shape and strength of the wave; for $H = 0$ the spacetime is flat.
These are among the simplest exact gravitational waves, and they solve Einstein's equations exactly rather than in a weak-field approximation.
