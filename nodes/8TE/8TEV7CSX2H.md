---
tag: 8TEV7CSX2H
kind: example
name: Standard map
msc: ["37E40", 37J11, 70K55]
instance_of: [A8TS2SNX9Z]
uses: [060W5CBZP6, 3ZZSXKM16Z, DBKXCGDKTD]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_map
same_as:
  wikidata: Q2257676
  wikipedia: Standard map
---

## Example

Let $K \in \R$ be a parameter.
The *standard map*, or Chirikov–Taylor map, acts on points $(\theta, p)$ of the cylinder, where $\theta$ is taken modulo $2\pi$.
On the torus, $p$ is also taken modulo $2\pi$.
The map is
$$p_{n+1} = p_n + K \sin \theta_n, \qquad \theta_{n+1} = \theta_n + p_{n+1}.$$
Its Jacobian matrix with respect to $(p_n, \theta_n)$ is
$$\begin{pmatrix} 1 & K \cos \theta_n \\ 1 & 1 + K \cos \theta_n \end{pmatrix},$$
whose determinant is $1 + K \cos \theta_n - K \cos \theta_n = 1$.
So the map preserves area and orientation, and it is a [[symplectomorphism|A8TS2SNX9Z]] of the plane form $dp \wedge d\theta$.

## Remarks

For $K = 0$ the map is integrable: $p$ is constant and each [[circle|060W5CBZP6]] $p = c$ is invariant, with rotation by the angle $c$.
For small $K \ne 0$, [[KAM theory|3ZZSXKM16Z]] for twist maps shows that the invariant circles with sufficiently irrational rotation numbers survive, slightly deformed.
These circles wrap around the cylinder and prevent $p$ from growing without bound.
As $K$ grows the circles break; numerically, the last one disappears near $K \approx 0.9716$, found by Greene, and beyond that $p$ can drift without bound.
For large $K$ most orbits look [[chaotic|DBKXCGDKTD]], with islands of stable motion around periodic orbits.

The map models a kicked rotor: a rotor that receives a periodic kick whose strength depends on its angle.

## Explanations

### L1 human

The standard map is a simple rule that takes a point of a cylinder to a new point, with one parameter $K$.
For $K = 0$ nothing interesting happens: each point slides along its circle.
As $K$ grows, the picture of its orbits changes from neat curves to a mixture of curves, islands and chaotic seas.
It is the standard laboratory for seeing the transition from order to chaos in Hamiltonian systems.
