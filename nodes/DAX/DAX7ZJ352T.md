---
tag: DAX7ZJ352T
kind: definition
name: Post-Newtonian expansion
msc: ["83C25", "83C10"]
defines: 7HC8RM1EH9
uses: [3MCZ97SW6V, 29WRN5J730, G49G4R1K04, DWK5N5SKTK, 6Y50T68WKY]
sources:
  - url: https://en.wikipedia.org/wiki/Post-Newtonian_expansion
---

## Definition

Consider a solution of the [[Einstein field equations|3MCZ97SW6V]] sourced by a bounded system of matter with typical mass $M$, size $r$ and internal speeds $v$.
Assume the system is weakly gravitating and slow: $\varepsilon^2 = \max\left(v^2/c^2, \, GM/(rc^2)\right) \ll 1$, where $G$ is the gravitational constant and $c$ the speed of light.
The *post-Newtonian expansion* is the formal expansion of the metric $g_{\mu\nu}$ and of the equations of motion of the matter in powers of $1/c$.
It is done in the near zone, in coordinates $(ct, x)$ close to [[Minkowski coordinates|G49G4R1K04]].
A term is of $n$-th post-Newtonian order (nPN) when its size relative to the Newtonian term is $\varepsilon^{2n}$.
At first post-Newtonian order (1PN), $g_{00}$ is computed through order $c^{-4}$, $g_{0i}$ through order $c^{-3}$ and $g_{ij}$ through order $c^{-2}$, with $g_{\mu\nu} \to \eta_{\mu\nu}$ as $c \to \infty$.

## Remarks

At 1PN in the harmonic gauge one finds $g_{00} = -1 - 2\Phi/c^2 - 2\Phi^2/c^4 + \dots$, where the extra terms of order $c^{-4}$ involve further potentials; $\Phi$ is the Newtonian potential solving [[Poisson's equation|DWK5N5SKTK]] $\nabla^2 \Phi = 4\pi G\rho$.
The leading order reproduces [[Newton's law of gravitation|29WRN5J730]].
Radiation reaction appears first at 2.5PN order, through odd powers of $1/c$.
The expansion is valid only in the near zone, at distances small compared with the wavelength of the emitted gravitational waves.
Far away it must be matched with a different expansion.

Example: the [[Schwarzschild metric|6Y50T68WKY]] of mass $M$ in harmonic coordinates has $g_{00} = -(r - m)/(r + m)$ with $m = GM/c^2$.
Expanding in $1/c$ gives $g_{00} = -1 + 2m/r - 2m^2/r^2 + O(c^{-6})$, which is the 1PN form above with $\Phi = -GM/r$.

Non-example: the late merger of two black holes has $v$ close to $c$ and $GM/(rc^2)$ of order one.
So $\varepsilon$ is not small and the expansion does not apply; numerical relativity is used instead.
