---
tag: 2DYR4C5Q5V
kind: example
name: Index of the de Rham complex
msc: [58J20, 58A12]
illustrates: [44GBFZ16SG, QDCD33CS21]
uses: [44GBFZ16SG, QDCD33CS21, A127WFVYKW, RNDDWDAFJ5, GG6NYPKMHX, ST71ZV3FES]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Singer_index_theorem
---

## Example

Let $M$ be a closed oriented Riemannian manifold of dimension $n$, and let $\Omega^k(M)$ be the space of smooth real $k$-forms.
Let $d^*$ be the formal adjoint of the exterior derivative $d$.
The operator
$$D = d + d^* \colon \Omega^{\mathrm{even}}(M) \to \Omega^{\mathrm{odd}}(M)$$
is elliptic, since $D^* D$ is the Hodge Laplacian on even forms.
Its kernel is the space of harmonic even forms, and its cokernel is isomorphic to $\ker D^*$, the space of harmonic odd forms.
By the [[Hodge theorem|A127WFVYKW]], the harmonic $k$-forms form a space of dimension $b_k$, the $k$-th [[Betti number|ST71ZV3FES]].
So the [[analytic index|44GBFZ16SG]] is
$$\operatorname{ind} D = \sum_{k = 0}^{n} (-1)^k b_k = \chi(M),$$
the [[Euler characteristic|RNDDWDAFJ5]] of $M$.

## Remarks

For $n$ odd, $\chi(M) = 0$ by Poincaré duality, and the index is $0$.
For $n$ even, the [[topological index|QDCD33CS21]] of $D$ is the Euler number $\langle e(TM), [M] \rangle$.
So the Atiyah–Singer index theorem gives $\chi(M) = \langle e(TM), [M] \rangle$, and with the Chern–Weil form of the Euler class this is the [[Chern–Gauss–Bonnet theorem|GG6NYPKMHX]].
For the round sphere $S^2$: $b_0 = b_2 = 1$ and $b_1 = 0$, so the index is $2$.

## Explanations

### L1 human

The de Rham operator $d + d^*$ sends forms of even degree to forms of odd degree.
Its solutions are the harmonic forms, which by Hodge theory count the holes of the manifold in each dimension.
So its index is the alternating count of holes, the Euler characteristic.
This is the simplest case where the index theorem recovers a classical theorem, here Gauss–Bonnet.
