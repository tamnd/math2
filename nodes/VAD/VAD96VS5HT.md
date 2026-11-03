---
tag: VAD96VS5HT
kind: statement
role: theorem
name: Petrov classification
msc: ["83C20", "53B30"]
uses: [SBHY31HESP, BY4QYYS788, JZ9ADDZX8D, 0N6960W0BV, 6Y50T68WKY]
about: [SBHY31HESP]
sources:
  - url: https://en.wikipedia.org/wiki/Petrov_classification
same_as:
  wikidata: Q4223027
  wikipedia: Petrov classification
---

## Statement

Let $(M, g)$ be a four-dimensional [[Lorentzian manifold|BY4QYYS788]], let $p \in M$, and let $C_{abcd}$ be the [[Weyl tensor|SBHY31HESP]] of $g$ at $p$.
A null vector $k \in T_pM$ (see [[light cone|JZ9ADDZX8D]]) is a *principal null direction* of $C$ if $k_{[e} C_{a]bc[d} k_{f]} k^b k^c = 0$.
Assume $C \ne 0$.
Then $C$ has exactly four principal null directions counted with multiplicity.
Their multiplicities form exactly one of the following patterns, which define the *Petrov type* of $g$ at $p$:

1. type I: four distinct directions, multiplicities $(1, 1, 1, 1)$;
2. type II: multiplicities $(2, 1, 1)$;
3. type D: multiplicities $(2, 2)$;
4. type III: multiplicities $(3, 1)$;
5. type N: multiplicity $(4)$.

If $C = 0$, the point is of type O.

## Remarks

The proof is simplest with two-component spinors: the Weyl tensor corresponds to a totally symmetric spinor $\Psi_{ABCD}$, that is, a complex binary quartic form.
By the fundamental theorem of algebra it factors as $\Psi_{ABCD} = \alpha_{(A} \beta_B \gamma_C \delta_{D)}$, and each factor gives a principal null direction; the patterns of coinciding factors are the five types.
Equivalently, $C$ defines a traceless complex symmetric linear map on the three-dimensional space of self-dual bivectors at $p$.
The types then correspond to the possible numbers of independent [[eigenvectors|0N6960W0BV]] and the coincidences among its eigenvalues.

A principal null direction $k$ is repeated (multiplicity at least $2$) if and only if $C_{abc[d} k_{e]} k^b k^c = 0$.
It has multiplicity at least $3$ if and only if $C_{abc[d} k_{e]} k^c = 0$, and multiplicity $4$ if and only if $C_{abcd} k^d = 0$.

Examples: the [[Schwarzschild metric|6Y50T68WKY]] and the Kerr metric are of type D at every point outside the singularity.
Plane gravitational waves have type N, the most degenerate nonzero type.
Minkowski space and the conformally flat Friedmann–Lemaître–Robertson–Walker metrics have type O, since their Weyl tensor vanishes.
The type can change from point to point; a spacetime is called algebraically special at $p$ if its type there is not I.

## Explanations

### L1 human

The Weyl tensor describes the part of spacetime curvature that is due to gravity at a distance, such as tidal forces and gravitational waves.
At each point it singles out up to four special light-ray directions.
The Petrov classification sorts spacetimes by how many of these directions coincide.
Black holes have two directions each counted twice, while a pure gravitational wave far from its source has all four in one direction.

### L2 human

The Petrov type is a coordinate-free invariant, so it helps to recognise and compare exact solutions of the Einstein equations.
Many exact solutions were found by assuming an algebraically special type, which simplifies the field equations a lot.
The Goldberg–Sachs theorem links repeated principal null directions in vacuum to shear-free null geodesic congruences.
The peeling theorem says that the Weyl tensor of an outgoing wave in an asymptotically flat spacetime has, in successive orders of $1/r$, types N, III, II and I.
