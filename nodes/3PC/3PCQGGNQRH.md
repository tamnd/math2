---
tag: 3PCQGGNQRH
kind: example
name: Gödel metric
msc: [83C15, 83C55]
instance_of: [BY4QYYS788]
illustrates: [DCM7BJ25R8]
uses: [3MCZ97SW6V, WVKKDY9V61, 4GTNM0WHDH]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel_metric
same_as:
  wikidata: Q1559192
  wikipedia: Gödel metric
---

## Example

Use units where the gravitational constant and the speed of light equal $1$.
Fix $a > 0$.
On $\R^4$ with coordinates $(t, x, y, z)$, the *Gödel metric* is
$$g = a^2\left(-\left(dt + e^x dz\right)^2 + dx^2 + dy^2 + \frac{1}{2} e^{2x} dz^2\right).$$
Check of the signature: the $(t, z)$ block of $g$ has determinant $-\frac12 a^4 e^{2x} < 0$, so it has one negative and one positive direction.
With $dx^2$ and $dy^2$ positive, $g$ has signature $(-, +, +, +)$.

Let $u = a\,(dt + e^x dz)$, a unit timelike covector.
A computation of the [[Ricci curvature|4GTNM0WHDH]] gives
$$R_{ab} = \frac{1}{a^2} u_a u_b, \qquad R = -\frac{1}{a^2}.$$
Hence $G_{ab} + \Lambda g_{ab} = 8\pi\rho\, u_a u_b$ with
$$\Lambda = -\frac{1}{2a^2}, \qquad 8\pi\rho = \frac{1}{a^2}.$$
So $g$ solves the [[Einstein field equations|3MCZ97SW6V]] with pressureless dust of constant density $\rho$, moving along $u$, and a negative [[cosmological constant|WVKKDY9V61]].

The metric is homogeneous: the isometry group acts transitively on spacetime.
The dust rotates: the vorticity of $u$ is nonzero.
Through every point there pass [[closed timelike curves|DCM7BJ25R8]].

## Explanations

### L1 human

Kurt Gödel found this solution in 1949 as a model of a rotating universe filled with dust.
Its striking feature is that one could travel into one's own past by moving on a large circle, without ever going faster than light locally.
So general relativity alone does not forbid time travel.
The universe it describes does not match ours, since it rotates and does not expand, but it showed that causality must be imposed as an extra condition.
