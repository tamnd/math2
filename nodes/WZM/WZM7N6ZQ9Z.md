---
tag: WZM7N6ZQ9Z
kind: statement
role: proposition
name: Pendry's perfect lens
msc: [78A48, 78A10]
uses: [F768YN0P2V, 5MJQ5J5H8Z, 9VGK0SP6EQ, NM024G378A, VT8YK4WC0H]
about: [8EW2R66GXS, GAM6ADR3ZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Superlens
  - url: https://doi.org/10.1103/PhysRevLett.85.3966
---

## Statement

Let the slab $0 < z < d$ be filled with a homogeneous, isotropic and lossless medium.
Let $\varepsilon$ and $\mu$ be its relative [[permittivity|F768YN0P2V]] and relative [[permeability|5MJQ5J5H8Z]], and let vacuum fill the rest of space.
Consider time-harmonic fields of angular frequency $\omega$, and let $k_0 = \omega / c$, where $c$ is the speed of light in vacuum.
Decompose the field into [[plane-wave|NM024G378A]] components with transverse wave number $k_x$, and let $k_z = \sqrt{k_0^2 - k_x^2}$, with the root chosen so that $\operatorname{Im} k_z > 0$ when $k_x^2 > k_0^2$.
Let the transmission coefficient of the slab be the ratio of the transmitted amplitude at $z = d$ to the incident amplitude at $z = 0$.
Then for each $k_x$ with $k_x^2 \ne k_0^2$ and each polarization, as $\varepsilon \to -1$ and $\mu \to -1$:

1. the reflection coefficient of the slab tends to $0$;
2. the transmission coefficient of the slab tends to $e^{-i k_z d}$.

Consequently, let a source lie at distance $a < d$ in front of the slab.
In this limit, its field is reproduced at distance $d - a$ behind the slab, with all its propagating and [[evanescent|VT8YK4WC0H]] components.

## Remarks

The proof sums the multiple reflections inside the slab, using the Fresnel coefficients of the two faces.
For $\varepsilon = \mu = -1$ the slab has the same impedance as vacuum, so each face reflects nothing, and the normal wave number inside the slab is $-k_z$ instead of $k_z$.
So the slab undoes the phase $e^{i k_z d}$ gained by a propagating wave over a distance $d$ of vacuum.
For an evanescent wave, $k_z = i\kappa$ with $\kappa > 0$, and the slab multiplies the amplitude by $e^{\kappa d}$: it amplifies the wave by exactly the factor that vacuum removes.
From the source to the image the wave crosses a total vacuum thickness $a + (d - a) = d$, and the slab compensates it, so every Fourier component arrives with its original amplitude and phase.

An ordinary lens loses the evanescent components, which carry the details smaller than the wavelength; this is the [[diffraction limit|GAM6ADR3ZJ]].
The perfect lens would beat that limit, since it restores them.

The hypotheses matter.
With losses, or with $\varepsilon$ and $\mu$ only close to $-1$, the amplification fails for large $k_x$, so the image has a finite resolution.
Exactly at $\varepsilon = \mu = -1$ the slab supports surface waves at every $k_x$, which is why the result is stated as a limit.
For $p$-polarized waves in the near field, where $k_x \gg k_0$, the permittivity $\varepsilon = -1$ alone is enough to amplify evanescent waves; a thin silver film is used for this.

## Explanations

### L1 human

A slab made of a material with [[negative refraction|8EW2R66GXS]] can focus light that comes out of a point.
Pendry showed that an ideal slab of this kind would also rebuild the fine details of an object, which normal lenses lose.
These details are carried by waves that die out quickly away from the object; the slab makes them grow back.
So such a lens would have no limit on resolution, in the ideal lossless case.

### L2 human

The result is a computation with plane waves and the Fresnel coefficients of a slab, followed by a limit.
It shows that the diffraction limit is a property of propagation in ordinary media, not a law of optics.
In practice, losses and the dispersion of metamaterials make the gain of evanescent waves saturate, and real superlenses only improve the resolution by a finite factor.
The slab is the simplest case of complementary media, which transformation optics describes with folded coordinate maps.
