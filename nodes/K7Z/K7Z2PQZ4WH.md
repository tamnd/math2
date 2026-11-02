---
tag: K7Z2PQZ4WH
kind: statement
role: theorem
name: de Rham theorem
msc: [58A12, 55N10]
uses: [F45VQ47GPV, GX74C07T0G, 6N7BC70CX0, 0E3G0GRPZ6]
about: [GX74C07T0G, 6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/De_Rham_cohomology
---

## Statement

Let $M$ be a [[smooth manifold|F45VQ47GPV]].
Let $\omega$ be a closed $k$-form on $M$ and let $c$ be a smooth singular $k$-cycle in $M$.
Put $\langle [\omega], [c] \rangle = \int_c \omega$.
Let $H^k_{\mathrm{dR}}(M)$ be the [[de Rham cohomology|GX74C07T0G]] of $M$ and $H^k(M; \R)$ its [[singular cohomology|6N7BC70CX0]] with real coefficients.
For every $k \ge 0$, this pairing induces an isomorphism of real vector spaces
$$H^k_{\mathrm{dR}}(M) \cong H^k(M; \R).$$

## Remarks

The map is well defined by the [[generalised Stokes theorem|0HPHKCGEQ0]].
It gives that the integral of an exact form over a cycle is $0$, and so is the integral of a closed form over a boundary.
One proof shows that both sides satisfy the Mayer–Vietoris sequence and agree on convex open subsets of $\R^n$.
On such sets the Poincaré lemma gives the de Rham side.
Then one inducts over a good cover of $M$.
Another proof says that both sides compute the sheaf cohomology of the constant sheaf $\R$ on $M$.
The isomorphism also takes the wedge product of forms to the [[cup product|JX47MS1R1H]], so it is an isomorphism of graded rings.

Example: on the circle $S^1$ with angle coordinate $\theta$, the closed form $d\theta$ is not exact.
Its integral over the circle is $2\pi \neq 0$, so its class corresponds to a nonzero class in $H^1(S^1; \R) \cong \R$.

The coefficients must be real (or contain $\R$): differential forms do not see torsion, and $H^k(M; \Z)$ can have torsion, as for the real projective plane.

## Explanations

### L1 human

On a smooth space there are two ways to count holes.
One uses calculus: differential forms whose derivative is zero but which are not derivatives themselves.
The other uses topology: cycles that are not boundaries.
The de Rham theorem says that the two counts agree, and the matching is given by integration.

### L2 human

The theorem lets you compute topological invariants of a manifold with calculus, and conversely.
For example, it shows that the de Rham cohomology is a topological invariant, though it is defined with smooth structure.
It is the model for comparison theorems in other settings, such as the comparison between algebraic de Rham cohomology and singular cohomology of a complex variety.
Together with Poincaré duality and Hodge theory it is a basic tool of global analysis on manifolds.
