---
tag: MDBAAEAV2N
kind: definition
name: Orbital angular momentum of light
msc: [78A40, 78A60, 78A10]
defines: T6ER90YNEH
uses: [53DCTAEM5M, 8YGCTX64MT, 23MDMTZT5X]
sources:
  - url: https://en.wikipedia.org/wiki/Orbital_angular_momentum_of_light
---

## Definition

Let a monochromatic beam of angular frequency $\omega$ move along the $z$ axis and obey the [[paraxial wave equation|53DCTAEM5M]].
Let $u(x, y)$ be its transverse complex amplitude in a plane $z = \text{const}$, smooth and not identically zero, with $u$ and $\partial_\varphi u$ square integrable.
Here $\partial_\varphi = x \, \partial_y - y \, \partial_x$ is the derivative in the polar angle $\varphi$.
The *orbital angular momentum per photon* of the beam, in units of the reduced Planck constant $\hbar$, is
$$\bar\ell = \frac{\displaystyle\int_{\R^2} \overline{u} \, (-i \, \partial_\varphi u) \, dx \, dy}{\displaystyle\int_{\R^2} \abs{u}^2 \, dx \, dy}.$$
The *orbital angular momentum* of the beam about the $z$ axis is $\bar\ell / \omega$ times its energy, in the same section of beam.

## Remarks

The operator $-i\,\partial_\varphi$ is symmetric for the $L^2$ inner product, so $\bar\ell$ is real.
The *spin* angular momentum, from circular polarisation, is a separate term; in the paraxial regime the two add.
Beams with $\bar\ell \ne 0$ typically contain an [[optical vortex|23MDMTZT5X]].

Example: a [[Laguerre–Gaussian mode|8YGCTX64MT]] $\mathrm{LG}_{p\ell}$ depends on $\varphi$ only through $e^{i\ell\varphi}$, so $-i\,\partial_\varphi u = \ell u$.
Hence $\bar\ell = \ell$, and the beam carries $\ell\hbar$ of orbital angular momentum per photon.

Non-example: a Gaussian beam has a profile that does not depend on $\varphi$, so $\partial_\varphi u = 0$ and $\bar\ell = 0$.
If it is circularly polarised it carries spin angular momentum $\pm\hbar$ per photon, but still no orbital angular momentum.
