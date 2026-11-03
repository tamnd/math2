---
tag: KBJTFMZWSF
kind: definition
name: Plane wave
msc: [78A40, 35L05]
defines: NM024G378A
uses: [5EHD2XBQDG]
sources:
  - url: https://en.wikipedia.org/wiki/Plane_wave
---

## Definition

Let $V$ be a finite-dimensional real or complex vector space, for example $\R$, $\C$ or $\R^3$, and let $n \in \R^3$ be a unit vector.
A *plane wave* with direction $n$ is a function $u \colon \R^3 \times \R \to V$ of the form
$$u(x, t) = G(x \cdot n, \, t)$$
for some function $G \colon \R \times \R \to V$.
It is a *travelling plane wave* with speed $v > 0$ if $u(x, t) = F(x \cdot n - v t)$ for some function $F \colon \R \to V$.
It is a *sinusoidal plane wave* if $u(x, t) = a \cos(k \cdot x - \omega t + \phi)$ for some constants of the following kind.
Here $a \in V$ is the amplitude, $k = \abs{k} n \neq 0$ the wave vector, $\omega \in \R$ the angular frequency and $\phi \in \R$ the phase.

## Remarks

The planes $x \cdot n = \text{const}$ are the wavefronts.
A sinusoidal plane wave is travelling with speed $\omega / \abs{k}$ when $\omega > 0$; its wavelength is $2\pi / \abs{k}$.
Complex notation $u = \mathrm{Re}\big(a \, e^{i(k \cdot x - \omega t)}\big)$, with complex amplitude $a$, is standard.
Every twice differentiable travelling plane wave $F(x \cdot n - ct)$ solves the [[wave equation|5EHD2XBQDG]] $u_{tt} = c^2 \Delta u$, since both sides equal $c^2 F''$.

Example: $u(x, y, z, t) = \sin(2x - 3t)$ is a sinusoidal plane wave with direction $n = (1, 0, 0)$, wave vector $k = (2, 0, 0)$ and $\omega = 3$; it travels with speed $3/2$.

Non-example: the spherical wave $u(x, t) = \cos(\abs{x} - t) / \abs{x}$ on $x \neq 0$ is not a plane wave.
At $t = 0$ its values at $(1, 0, 0)$ and $(1, 1, 0)$ differ, though both points lie on the plane $x \cdot e_1 = 1$.
Similar pairs exist for every direction $n$.

## Explanations

### L1 human

A plane wave depends on position only through one coordinate, the distance along the direction $n$.
So it is really a one-dimensional wave, copied onto every plane across that direction.
Sinusoidal plane waves are the building blocks of wave analysis.
