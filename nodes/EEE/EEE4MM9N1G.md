---
tag: EEE4MM9N1G
kind: definition
name: Wave front of a Legendrian map
msc: [53D10, 58K05]
defines: 824SSQ3SQN
uses: [F45VQ47GPV, HBQ8BZ7XB5, Q2DMSTWZYZ, GCS702QT54, 6RW68JGBHC]
sources:
  - url: https://en.wikipedia.org/wiki/Contact_geometry
---

## Definition

Let $(E, \xi)$ be a [[contact manifold|HBQ8BZ7XB5]] of dimension $2n + 1$ and let $\rho \colon E \to B$ be a smooth fibre bundle over a [[smooth manifold|F45VQ47GPV]] $B$ of dimension $n + 1$.
The bundle $\rho$ is a *Legendrian fibration* if each fibre is a [[Legendrian submanifold|Q2DMSTWZYZ]] of $E$.
Let $\iota \colon L \to E$ be a Legendrian [[immersion|6RW68JGBHC]], that is, $\dim L = n$ and $d\iota$ maps each tangent space of $L$ into $\xi$.
The composition $\rho \circ \iota \colon L \to B$ is a *Legendrian map*.
Its *wave front* (or *front*) is the image $\rho(\iota(L)) \subset B$.

## Remarks

The model case is the [[contact structure on the jet space|GCS702QT54]] $J^1(Q) = T^*Q \times \R$ of a manifold $Q$ of dimension $n$, with coordinates $(q, p, z)$, contact form $dz - \sum_i p_i \, dq_i$, and $\rho(q, p, z) = (q, z) \in Q \times \R$.
The fibres $\set{(q, z)} \times T_q^* Q$ are Legendrian, since $dq = 0$ and $dz = 0$ along them.

Example: $Q = \R$ and $\iota(t) = (t^2, t, \tfrac23 t^3)$.
Along $\iota$, $dz = 2t^2 \, dt$ and $p \, dq = t \cdot 2t \, dt = 2t^2 \, dt$, so $\iota^*(dz - p\,dq) = 0$ and $\iota$ is a Legendrian embedding.
Its front is the curve $(t^2, \tfrac23 t^3)$ in the $(q, z)$-plane, a semicubical parabola with a cusp at the origin, although $\iota$ itself is smooth with nonzero velocity.

Non-example: the curve $\gamma(t) = (t, 0, t)$ in $J^1(\R)$ is not Legendrian, since $\gamma^*(dz - p\,dq) = dt \ne 0$; so its projection $(t, t)$ is not a front in this sense.

For the $1$-jet lift $q \mapsto (q, df(q), f(q))$ of a smooth function $f$, the front is the graph of $f$.
Where the front is a smooth hypersurface not tangent to the $z$-direction, the Legendrian submanifold is recovered from it by $p = \partial z / \partial q$.
