---
tag: 3EWGE3V4BK
kind: definition
name: Einstein–Cartan theory
msc: [83D05]
defines: 2S4S07Z33K
uses: [384JFR3K6X, BY4QYYS788, JX65KSVHSJ, JZNQAN00ZJ, CAZYGE1T4E, ZHX2VYQDZ3, JPE3A1SN7V, 3MCZ97SW6V]
sources:
  - url: https://en.wikipedia.org/wiki/Einstein%E2%80%93Cartan_theory
---

## Definition

Let $\kappa = 8\pi G/c^4$, where $G$ is the gravitational constant and $c$ the speed of light.
Let $g$ be a [[Lorentzian metric|BY4QYYS788]] on a four-dimensional manifold and $\Gamma$ an [[affine connection|JX65KSVHSJ]].
*Einstein–Cartan theory* is the [[alternative to general relativity|384JFR3K6X]] with fields $g$ and $\Gamma$ subject to the following conditions:

1. $\Gamma$ is compatible with $g$, that is $\nabla g = 0$, but its [[torsion tensor|JZNQAN00ZJ]] need not vanish;
2. the action is
$$S = \frac{1}{2\kappa} \int R(\Gamma) \sqrt{-g}\, d^4x + S_m[g, \Gamma, \psi],$$
where $R(\Gamma)$ is the scalar curvature of $\Gamma$ and $S_m$ is the action of the matter fields $\psi$;
3. the field equations are obtained by varying $S$ independently with respect to $g$ and to $\Gamma$ (equivalently, to the torsion).

## Remarks

Variation with respect to the metric gives an Einstein-type equation $G_{ab}(\Gamma) = \kappa\, \Sigma_{ab}$.
Here $G_{ab}(\Gamma)$ is the Einstein tensor of $\Gamma$, which need not be symmetric, and $\Sigma_{ab}$ is the canonical energy–momentum tensor of matter.
Variation with respect to the torsion gives an algebraic, linear equation that expresses the torsion through the spin tensor of matter, times $\kappa$.
So torsion does not propagate: it vanishes wherever the spin density of matter vanishes.
Example: in vacuum, or for matter without spin, the torsion is zero and $\Gamma$ is the [[Levi-Civita connection|CAZYGE1T4E]].
Then the equations reduce to the [[Einstein field equations|3MCZ97SW6V]].
Non-example: a connection with $\nabla g \ne 0$ fails clause 1; such non-metric connections are allowed in the wider class of metric-affine theories of gravity.
When $\Gamma$ is the Levi-Civita connection, $R(\Gamma)$ is the usual [[scalar curvature|ZHX2VYQDZ3]] and the action is the [[Einstein–Hilbert action|JPE3A1SN7V]].

## Explanations

### L1 human

Einstein–Cartan theory uses the same action as general relativity but lets the connection twist.
The twist, or torsion, is fixed at each point by the spin of the matter at that point.
