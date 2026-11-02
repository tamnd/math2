---
tag: 2SFM73YET0
kind: statement
role: theorem
name: Classification of surfaces
msc: [57K20, 57N99]
uses: [VGJJVBZ1MQ, Y0K0K5NGWW, RNDDWDAFJ5, 0TD904MG06, 03NM7DZXXC]
about: [VGJJVBZ1MQ]
sources:
  - url: https://en.wikipedia.org/wiki/Surface_(topology)
---

## Statement

Let $S$ be a closed [[surface|VGJJVBZ1MQ]], that is, a compact connected surface without boundary.

1. $S$ is homeomorphic to exactly one surface in the following list.
   - The sphere $S^2$.
   - The [[connected sum|Y0K0K5NGWW]] of $g \ge 1$ copies of the [[torus|03NM7DZXXC]] $T^2$.
   - The connected sum of $k \ge 1$ copies of the [[real projective plane|MWDB7RACWQ]] $\R P^2$.
2. Two closed surfaces are homeomorphic if and only if both are [[orientable|0TD904MG06]] or both are non-orientable, and they have the same [[Euler characteristic|RNDDWDAFJ5]].

The Euler characteristic of the connected sum of $g$ tori is $2 - 2g$, and that of the connected sum of $k$ projective planes is $2 - k$.

## Remarks

Idea of the proof: by Radó's theorem every surface has a triangulation, so $S$ is obtained from a polygon by gluing its edges in pairs.
Cutting and regluing the polygon brings the gluing word to a normal form: $aa^{-1}$ for the sphere, $a_1 b_1 a_1^{-1} b_1^{-1} \cdots a_g b_g a_g^{-1} b_g^{-1}$ for $g$ tori, or $c_1 c_1 \cdots c_k c_k$ for $k$ projective planes.
The surfaces in the list are different because orientability and Euler characteristic are topological invariants that take different values on them.

The theorem at work: the [[Klein bottle|6J4C2P3ZHC]] is a closed non-orientable surface with Euler characteristic $0$, so it is homeomorphic to $\R P^2 \# \R P^2$.
Also $T^2 \# \R P^2$ is non-orientable with Euler characteristic $-1$, so it is homeomorphic to $\R P^2 \# \R P^2 \# \R P^2$.
Compactness is needed: the open disc and the open annulus are connected surfaces without boundary that are not in the list.

## Explanations

### L1 human

Every closed surface is a sphere with some number of handles, or a sphere with some number of crosscaps.
To tell two closed surfaces apart, two pieces of information suffice: whether they have a consistent inside and outside, and their Euler characteristic.
So the infinite variety of possible shapes reduces to a simple list.

### L2 human

The classification is the model of what one hopes for in manifold topology: a complete list with computable invariants.
The orientable number $g$ is the [[genus|NJ787GZS1N]] of the surface.
The proof through polygons and gluing words also computes the fundamental group of each surface.
Every closed surface other than $S^2$ and $\R P^2$ is aspherical, and every closed surface carries a metric of constant curvature, with sign given by the Euler characteristic.
In dimension $3$ no list this simple exists, and the analogue is the [[geometrization conjecture|B27HB43K86]].
