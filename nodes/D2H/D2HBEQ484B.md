---
tag: D2HBEQ484B
kind: definition
name: Pancharatnam–Berry phase
msc: [78A10, 81Q70]
defines: VKEYXGFS6E
uses: [PJ8ZSJ0QDW, D3XTQ5Z2QA, J1T8NZCVTB, WHDZ3MK56B]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_phase
---

## Definition

Describe a state of full [[polarization|PJ8ZSJ0QDW]] by a unit [[Jones vector|D3XTQ5Z2QA]] $u \in \C^2$, where $u$ and $e^{i\alpha} u$ give the same state.
Let $\ip{u}{v} = \overline{u_1} v_1 + \overline{u_2} v_2$.
Let $u \colon [0, 1] \to \C^2$ be a smooth curve of unit vectors such that $u(1) = e^{i\gamma} u(0)$ for some real $\gamma$, so that the curve of states is closed.
Assume that $\mathrm{Im}\, \ip{u(t)}{u'(t)} = 0$ for all $t$, that is, each state is in phase with its neighbours in the sense of Pancharatnam.
The number $\gamma$ modulo $2\pi$ is the *Pancharatnam–Berry phase* of the closed curve of states.

## Remarks

The phase depends only on the closed curve $C$ traced on the [[Poincaré sphere|J1T8NZCVTB]].
If $C$ bounds a region of solid angle $\Omega$, then $\gamma \equiv \pm \Omega/2 \pmod{2\pi}$, where the sign depends on the orientation of $C$ and on the conventions.
Geometrically, $\gamma$ is the [[holonomy|WHDZ3MK56B]] of the natural connection on the bundle of unit Jones vectors over the sphere.

Example: take the state along a loop that goes from horizontal to $45^\circ$ linear along the equator, then to a circular pole, then back to horizontal.
This geodesic triangle encloses one eighth of the sphere, so $\Omega = \pi/2$ and $\abs{\gamma} = \pi/4$.

Non-example: a curve that goes from horizontal to $45^\circ$ along the equator and comes back the same way encloses no area.
Its Pancharatnam–Berry phase is $0$.

For a discrete cycle of states $u_1, u_2, u_3$, no two orthogonal, the phase equals $\arg\big(\ip{u_1}{u_2} \ip{u_2}{u_3} \ip{u_3}{u_1}\big)$ up to the same sign convention.
