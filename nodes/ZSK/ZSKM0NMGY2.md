---
tag: ZSKM0NMGY2
kind: definition
name: Inductance
msc: [78A30, 78A55]
defines: K1STN67XQ0
uses: [XRED3C547P, 2K5D5HH89T, 026J1MG2NW]
sources:
  - url: https://en.wikipedia.org/wiki/Inductance
---

## Definition

Let $C_1, \dots, C_n$ be disjoint closed circuits in a linear medium, and let $C_j$ carry a steady current $I_j$.
For each $i$, let $S_i$ be an oriented surface with boundary $C_i$, and let $\Phi_i$ be the [[flux|026J1MG2NW]] of the total [[magnetic field|XRED3C547P]] through $S_i$.
Then there are constants $L_{ij}$, depending only on the geometry of the circuits and on the medium, such that
$$\Phi_i = \sum_{j=1}^{n} L_{ij} I_j \quad \text{for all currents } I_1, \dots, I_n.$$
The number $L_{ij}$ for $i \neq j$ is the *mutual inductance* of $C_i$ and $C_j$.
The number $L_{ii}$ is the *self-inductance* of $C_i$.
The unit of inductance is the henry, equal to one weber per ampere.

## Remarks

The flux $\Phi_i$ does not depend on the choice of $S_i$, because $\nabla \cdot B = 0$ by [[Gauss's law for magnetism|2K5D5HH89T]].
The constants exist because the magnetic field of steady currents in a linear medium depends linearly on the currents.
The mutual inductances are symmetric, $L_{ij} = L_{ji}$.

For an infinitely thin wire the flux of its own field through itself diverges near the wire.
So the self-inductance needs a wire of positive thickness, and it then depends on how the current is spread over the cross-section.

Example: a long solenoid of length $\ell$, cross-section area $A$ and $N$ turns in vacuum has inside it the nearly uniform field $B = \mu_0 N I / \ell$.
Each turn links the flux $B A$, so the total linked flux is $N B A$, and the self-inductance is approximately $L = \mu_0 N^2 A / \ell$, neglecting end effects.

Non-example: a coil wound on an iron core is not a linear system, since the magnetization of iron is not proportional to the field.
The ratio of flux to current then changes with the current, and no constant inductance describes the coil over a wide range of currents.
