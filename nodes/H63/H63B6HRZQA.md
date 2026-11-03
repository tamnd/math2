---
tag: H63B6HRZQA
kind: statement
role: theorem
name: Wigner rotation
msc: [83A05, "22E43"]
uses: [WEVGN4C7PQ, QWK3BYVJ9W, 0HFREYRSZP, HQQM0TRV4N]
about: [WEVGN4C7PQ]
sources:
  - url: https://en.wikipedia.org/wiki/Wigner_rotation
same_as:
  wikidata: Q25303636
  wikipedia: Wigner rotation
---

## Statement

For a velocity $\mathbf{v} \in \R^3$ with $\abs{\mathbf{v}} < c$, let $B(\mathbf{v})$ be the pure boost with velocity $\mathbf{v}$.
This is the [[Lorentz transformation|WEVGN4C7PQ]] to a frame moving with velocity $\mathbf{v}$ without rotation of the spatial axes.
Let $\mathbf{u}, \mathbf{v} \in \R^3$ with $\abs{\mathbf{u}} < c$ and $\abs{\mathbf{v}} < c$.
Then there are a unique velocity $\mathbf{w}$ with $\abs{\mathbf{w}} < c$ and a unique [[rotation|0HFREYRSZP]] $R$ of the spatial axes such that
$$B(\mathbf{u}) \, B(\mathbf{v}) = R \, B(\mathbf{w}).$$
The rotation $R$, the *Wigner rotation*, is the identity if and only if $\mathbf{u}$ and $\mathbf{v}$ are parallel or one of them is $0$.
Otherwise $R$ is a rotation about the axis $\mathbf{u} \times \mathbf{v}$ by a non-zero angle.

## Remarks

Proof idea: every proper orthochronous Lorentz transformation $\Lambda$ factors uniquely as a rotation times a pure boost.
This is the polar decomposition of the matrix of $\Lambda$ into an orthogonal part and a positive definite symmetric part.
Apply this to $\Lambda = B(\mathbf{u}) B(\mathbf{v})$; the velocity $\mathbf{w}$ is given by the [[velocity-addition formula|HQQM0TRV4N]].
If $\mathbf{u}$ and $\mathbf{v}$ are parallel, both boosts act in one plane and commute, and their product is the boost with the added rapidity.
Consequence: the pure boosts do not form a subgroup of the [[Lorentz group|QWK3BYVJ9W]]; the commutator of two non-collinear boosts contains a rotation.

## Explanations

### L1 human

Changing to a moving frame and then to another moving frame is the same as one change of frame, plus a turn of the axes.
The turn appears only when the two motions are in different directions.
It is a purely relativistic effect: in Newtonian physics, adding velocities never turns the axes.

### L2 human

Wigner rotation shows that velocity addition in relativity is neither commutative nor associative when the velocities are not collinear.
In the theory of representations of the Poincaré group, it describes how the spin of a moving particle transforms under Lorentz transformations.
Applied to a sequence of infinitesimal boosts along a curved path, it gives Thomas precession.
