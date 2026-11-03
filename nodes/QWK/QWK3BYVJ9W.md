---
tag: QWK3BYVJ9W
kind: example
name: Lorentz group
msc: ["22E43", "83A05", "20G20"]
instance_of: [7JBRGCVJRB]
uses: [M2900DMEW6, J58ED1GV6N, 0CGYNDCWRR]
sources:
  - url: https://en.wikipedia.org/wiki/Lorentz_group
same_as:
  wikidata: Q1334417
  wikipedia: Lorentz group
---

## Example

Let $\eta = \operatorname{diag}(1, -1, -1, -1)$.
Give $\R^4$ with coordinates $(t, x, y, z)$ the quadratic form
$$Q(t, x, y, z) = t^2 - x^2 - y^2 - z^2,$$
which makes it [[Minkowski space|G49G4R1K04]] (in units where the speed of light is $1$).
The *Lorentz group* is the group of [[Lorentz transformations|WEVGN4C7PQ]], the linear maps of $\R^4$ preserving $Q$:
$$O(1, 3) = \set{\Lambda \in GL_4(\R) : \Lambda^T \eta \Lambda = \eta}.$$
It is the [[indefinite orthogonal group|M2900DMEW6]] of signature $(1, 3)$, a [[Lie group|7JBRGCVJRB]] of dimension $6$.

Check with a boost along the $x$-axis with rapidity $\phi \in \R$:
$$\Lambda = \begin{pmatrix} \cosh\phi & \sinh\phi & 0 & 0 \\ \sinh\phi & \cosh\phi & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$$
It sends $(t, x, y, z)$ to $(t \cosh\phi + x \sinh\phi, \ t \sinh\phi + x \cosh\phi, \ y, \ z)$, and
$$(t \cosh\phi + x \sinh\phi)^2 - (t \sinh\phi + x \cosh\phi)^2 = (t^2 - x^2)(\cosh^2\phi - \sinh^2\phi) = t^2 - x^2,$$
so $Q$ is preserved.

## Remarks

The rotations of space, $\Lambda = \operatorname{diag}(1, R)$ with $R \in$ [[SO(3)|0CGYNDCWRR]], form a compact subgroup, and the boosts make the group noncompact.
$O(1, 3)$ has four connected components, distinguished by the sign of $\det \Lambda$ and the sign of the entry $\Lambda_{00}$.
The identity component $SO^+(1, 3)$ is the *proper orthochronous* Lorentz group: it keeps the orientation of space-time and the direction of time.
The other components are reached from it by space inversion, time reversal, or both.
$SO^+(1, 3)$ is isomorphic to $PSL(2, \C)$, and [[SL(2,C)|J58ED1GV6N]] is its universal cover, a double cover.

## Explanations

### L1 human

The Lorentz group collects the changes of reference frame of special relativity that fix the origin of space-time.
These are the rotations of space and the boosts, which pass to an observer moving at constant velocity.
Because they preserve $t^2 - x^2 - y^2 - z^2$, they map the light cone $t^2 = x^2 + y^2 + z^2$ to itself, so every observer measures the same speed of light.
A boost mixes time with one space coordinate in the way a rotation mixes two space coordinates, but with hyperbolic functions in place of sines and cosines.
