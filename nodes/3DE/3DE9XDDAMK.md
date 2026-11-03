---
tag: 3DE9XDDAMK
kind: definition
name: Ashtekar variables
msc: [83C45, 83C05]
defines: SH0DEE8P6K
uses: [CFAFAPV7HB, FHZETS8QTT, NJ21PN5ZGJ, 5HDG31YEPW]
sources:
  - url: https://en.wikipedia.org/wiki/Ashtekar_variables
---

## Definition

Let $\Sigma$ be a three-manifold with a [[Riemannian metric|5HDG31YEPW]] $q_{ab}$ and extrinsic curvature $K_{ab}$, as in the [[ADM formalism|CFAFAPV7HB]].
Let $e^a_i$ ($i = 1, 2, 3$) be an orthonormal frame (triad) for $q_{ab}$, let $K^i_a = K_{ab} e^b_i$, and let $\Gamma^i_a$ be the [[spin connection|FHZETS8QTT]] of the triad.
Fix a constant $\gamma \ne 0$, the Barbero–Immirzi parameter.
The *Ashtekar–Barbero variables* are:

1. the densitized triad $E^a_i = \sqrt{\det q} \; e^a_i$;
2. the $\mathfrak{su}(2)$-valued [[connection|NJ21PN5ZGJ]] $A^i_a = \Gamma^i_a + \gamma K^i_a$.

Their Poisson brackets are $\set{A^i_a(x), E^b_j(y)} = 8 \pi G \gamma \, \delta^b_a \delta^i_j \delta^3(x, y)$, and all other brackets vanish.
Ashtekar's original variables are the complex choice $\gamma = i$ (self-dual variables).

## Remarks

The constraints of general relativity become: the Gauss constraint $D_a E^a_i = \partial_a E^a_i + \epsilon_{ijk} A^j_a E^{ak} = 0$, the diffeomorphism constraint $E^a_i F^i_{ab} = 0$, and the Hamiltonian constraint, where $F$ is the curvature of $A$.
For $\gamma = i$ and $\Lambda = 0$ the Hamiltonian constraint is the polynomial $\epsilon^{ijk} E^a_i E^b_j F_{kab} = 0$.
Example: on flat $\R^3$ at rest, with $q_{ab} = \delta_{ab}$, $K_{ab} = 0$ and the constant triad $e^a_i = \delta^a_i$, one gets $E^a_i = \delta^a_i$ and $A^i_a = 0$, which satisfies all constraints.
Non-example: the Levi-Civita connection of $q$ alone is not an Ashtekar–Barbero connection when $K_{ab} \ne 0$, since it carries no information on the extrinsic curvature.
