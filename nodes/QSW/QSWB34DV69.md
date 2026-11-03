---
tag: QSWB34DV69
kind: definition
name: Teleparallelism
msc: [83D05]
defines: QR8ATA5C50
uses: [384JFR3K6X, KH9BG71N36, BY4QYYS788, JX65KSVHSJ, JZNQAN00ZJ, JA29ETCM02, ZHX2VYQDZ3, CAZYGE1T4E]
sources:
  - url: https://en.wikipedia.org/wiki/Teleparallelism
---

## Definition

Let $M$ be a four-dimensional manifold with a [[frame field|KH9BG71N36]] (tetrad) $e_a{}^\mu$, $a = 0, 1, 2, 3$, and dual coframe $e^a{}_\mu$, and let $\eta_{ab}$ be the Minkowski metric.
The tetrad defines the [[Lorentzian metric|BY4QYYS788]] $g_{\mu\nu} = \eta_{ab}\, e^a{}_\mu e^b{}_\nu$.
The *Weitzenböck connection* of the tetrad is the [[affine connection|JX65KSVHSJ]]
$$\Gamma^\lambda{}_{\mu\nu} = e_a{}^\lambda \, \partial_\mu e^a{}_\nu.$$
A *teleparallel* theory of gravity has the tetrad as gravitational field and uses the Weitzenböck connection as geometry.
The field is carried by its [[torsion tensor|JZNQAN00ZJ]]
$$T^\lambda{}_{\mu\nu} = e_a{}^\lambda \left(\partial_\mu e^a{}_\nu - \partial_\nu e^a{}_\mu\right).$$

## Remarks

The Weitzenböck connection is compatible with $g$ and has vanishing [[curvature|JA29ETCM02]], since the frame $e_a$ is parallel for it: parallel transport does not depend on the path.
Consider the torsion scalar
$$T = \frac14 T^{\rho\mu\nu}T_{\rho\mu\nu} + \frac12 T^{\rho\mu\nu}T_{\nu\mu\rho} - T^\rho{}_{\mu\rho}\,T^{\nu\mu}{}_\nu.$$
The *teleparallel equivalent of general relativity* takes $T \det(e^a{}_\mu)$ as Lagrangian.
The [[scalar curvature|ZHX2VYQDZ3]] of the [[Levi-Civita connection|CAZYGE1T4E]] of $g$ equals $-T$ plus a total divergence, so the field equations are those of general relativity.
Example: the constant tetrad $e^a{}_\mu = \delta^a_\mu$ on $\R^4$ gives $g = \eta$, $\Gamma = 0$ and $T^\lambda{}_{\mu\nu} = 0$.
Non-example: the Levi-Civita connection of a curved metric, such as the Schwarzschild metric, is torsion-free but has nonzero curvature, so it is not a teleparallel connection.
Sign conventions for $T^\lambda{}_{\mu\nu}$ and for the torsion scalar vary between authors.

## Explanations

### L1 human

A teleparallel theory gives every point of spacetime a set of four reference directions and declares that matching directions at different points are parallel.
Gravity is then encoded in how these reference directions twist from point to point.
