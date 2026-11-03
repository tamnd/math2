---
tag: 9SJ4SC9FQX
kind: statement
role: theorem
name: Kuiper's theorem
msc: [58B05, 57N20, 46C05]
uses: [HM2HHE3J51, BMDG4JQPEH, 06EKW1AKXF, R5WP8Z69Q8, MM0EJ2GDE4, 0FCHE902D7, 0R9R0Y1HDK]
about: [BMDG4JQPEH]
sources:
  - url: https://en.wikipedia.org/wiki/Kuiper%27s_theorem
same_as:
  wikidata: Q6442276
  wikipedia: Kuiper's theorem
---

## Statement

Let $H$ be an infinite-dimensional real or complex [[Hilbert space|HM2HHE3J51]].
Let $GL(H)$ be the group of invertible bounded linear operators on $H$.
Let $U(H)$ be the group of [[unitary operators|MM0EJ2GDE4]] on $H$.
Give both groups the [[operator norm|06EKW1AKXF]] topology.
Then $GL(H)$ and $U(H)$ are [[contractible|R5WP8Z69Q8]].

## Remarks

The polar decomposition $T = U \abs{T}$ gives a deformation retraction of $GL(H)$ onto $U(H)$, since the positive invertible operators form a convex set.
For $U(H)$, one first deforms a compact family of unitaries to a family that is the identity on an infinite-dimensional subspace.
A rotation argument in the spirit of the Eilenberg swindle, using a decomposition of $H$ as an infinite sum of copies of itself, then deforms the family to the identity.

Infinite dimension is necessary.
For $H = \C^n$, the group $GL_n(\C)$ is not contractible: the determinant gives a map to $\C^\times$ that induces an isomorphism $\pi_1(GL_n(\C)) \cong \Z$.
More generally the finite [[unitary groups|0R9R0Y1HDK]] have many nonzero homotopy groups.

Consequence: every Hilbert bundle with structure group $U(H)$ over a paracompact space is trivial.

## Explanations

### L1 human

In finite dimensions the group of invertible matrices has holes: for example, a loop of complex numbers around $0$ cannot be shrunk without passing through $0$.
Kuiper's theorem says that in an infinite-dimensional Hilbert space all such holes disappear.
Every loop, sphere, or other family of invertible operators can be deformed to the identity through invertible operators.

### L2 human

The theorem is a basic input to the Atiyah–Jänich theorem, which identifies homotopy classes of maps into Fredholm operators with K-theory.
It also implies that the projective unitary group $PU(H)$ is an Eilenberg–MacLane space $K(\Z, 2)$, so that principal $PU(H)$-bundles over a space $X$ are classified by $H^3(X; \Z)$.
This is the classification of twists in twisted K-theory.
