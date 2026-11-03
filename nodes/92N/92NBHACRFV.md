---
tag: 92NBHACRFV
kind: definition
name: Stoneley wave
msc: [74J15, 86A15]
defines: 833VFEDN1F
uses: [T1PYEBKBAJ, GZ7E9GHQYB, X32RRM7ATM]
sources:
  - url: https://en.wikipedia.org/wiki/Stoneley_wave
---

## Definition

Let two homogeneous isotropic linear elastic solids fill the half-spaces $x_3 < 0$ and $x_3 > 0$.
Let them be in welded contact along the plane $x_3 = 0$, so that displacement and traction are continuous there.
Let $c_{S,1}$ and $c_{S,2}$ be their [[S-wave|GZ7E9GHQYB]] speeds.
A *Stoneley wave* is a nonzero [[elastodynamic|T1PYEBKBAJ]] solution without body force of the form
$$u(x, t) = \operatorname{Re} \left[ \left( U_1(x_3), \, 0, \, U_3(x_3) \right) e^{i k (x_1 - c t)} \right], \qquad k > 0,$$
whose amplitude tends to $0$ as $x_3 \to -\infty$ and as $x_3 \to +\infty$.

## Remarks

Decay on both sides forces $c < \min(c_{S,1}, c_{S,2})$, since otherwise one of the shear parts would oscillate instead of decay away from the interface.
The four interface conditions give a $4 \times 4$ linear system for the amplitudes, and a Stoneley wave exists when its determinant vanishes for some such $c$.
As for the Rayleigh wave, $c$ does not depend on $k$.

Existence holds only for a restricted range of the ratios of the densities and elastic constants of the two solids.
Non-example: when the two solids have the same density and the same elastic constants, the body is one homogeneous space, and no wave tied to the plane $x_3 = 0$ exists.

Another non-example: a [[Rayleigh wave|X32RRM7ATM]] on the free surface of a single half-space decays only on one side; it has no second medium, so it is not a Stoneley wave.
