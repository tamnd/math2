---
tag: 44Z5GQTCXW
kind: statement
role: theorem
name: Goldberg–Sachs theorem
msc: ["83C20", "83C60", "53B30"]
uses: [BY4QYYS788, SBHY31HESP, VAD96VS5HT, CWHM6AV4G3, TTZYRV72HN, JRV1T69FYJ]
about: [SBHY31HESP, VAD96VS5HT]
sources:
  - url: https://en.wikipedia.org/wiki/Goldberg%E2%80%93Sachs_theorem
same_as:
  wikidata: Q5579030
  wikipedia: Goldberg–Sachs theorem
---

## Statement

Let $(M, g)$ be a four-dimensional [[Lorentzian manifold|BY4QYYS788]] that is a [[vacuum solution|JRV1T69FYJ]], so that its Ricci tensor vanishes.
Let $U \subseteq M$ be an open set on which the [[Weyl tensor|SBHY31HESP]] is nowhere zero, and let $l$ be a null vector field on $U$.
Then the following are equivalent.

1. $l$ is tangent to a congruence of null geodesics that is shear-free.
2. $l$ is at each point a repeated principal null direction of the Weyl tensor.

In particular, the Weyl tensor is algebraically special on $U$ if and only if $U$ carries a shear-free [[congruence of null geodesics|CWHM6AV4G3]].
Here algebraically special refers to the [[Petrov classification|VAD96VS5HT]].

## Remarks

In the [[Newman–Penrose formalism|TTZYRV72HN]] with $l$ as first tetrad vector, clause 1 reads $\kappa = \sigma = 0$ and clause 2 reads $\Psi_0 = \Psi_1 = 0$.
The proof uses the Bianchi identities written in this formalism.
In vacuum they link the derivatives of $\Psi_0$ and $\Psi_1$ to $\kappa$ and $\sigma$ multiplied by the Weyl scalars, and this forces the two conditions to hold together.
For example, in the Schwarzschild spacetime the radial ingoing and outgoing light rays form two shear-free geodesic congruences.
The Weyl tensor there is of type D, with these two repeated principal null directions.
The vacuum hypothesis is needed in this form; there are generalisations that only ask for weaker conditions on the Ricci tensor.

## Explanations

### L1 human

The Weyl tensor describes the part of gravity that can travel as waves and stretch objects.
At each point it singles out up to four special light-like directions.
The theorem says that, in empty space, two of these directions coincide exactly when there is a family of light rays that travels without being sheared.

### L2 human

The theorem turns an algebraic condition on the curvature into a geometric condition on a family of light rays.
It is a main tool to find algebraically special exact solutions, because one can start from an ansatz with a shear-free null geodesic congruence.
The Kerr metric and the Robinson–Trautman metrics belong to this class.
