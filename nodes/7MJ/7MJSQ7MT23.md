---
tag: 7MJSQ7MT23
kind: definition
name: Morse homology
msc: [57R70, 57R58, "58E05"]
defines: 94BWTKKGJM
uses: [F45VQ47GPV, KPQ96640ZJ, Q61VFHCH2J, A2PDZ8GA9C]
sources:
  - url: https://en.wikipedia.org/wiki/Morse_homology
---

## Definition

Let $M$ be a compact [[smooth manifold|F45VQ47GPV]] without boundary, let $f \colon M \to \R$ be a [[Morse function|KPQ96640ZJ]], and let $g$ be a [[Riemannian metric|Q61VFHCH2J]] on $M$.
Let $p$ be a critical point, and consider the flow lines of the vector field $-\nabla f$.
The *unstable manifold* $W^u(p)$ is the set of points whose flow line tends to $p$ as time goes to $-\infty$.
The *stable manifold* $W^s(p)$ is the set of points whose flow line tends to $p$ as time goes to $+\infty$.
Assume that the pair $(f, g)$ is *Morse–Smale*: $W^u(p)$ and $W^s(q)$ are [[transverse|A2PDZ8GA9C]] for all critical points $p, q$.
For $k \ge 0$, let $C_k$ be the $\Z/2$-vector space with basis the critical points of $f$ of index $k$.
Let $p$ be a critical point of index $k$ and $q$ one of index $k - 1$.
Let $n(p, q) \in \Z/2$ be the number, modulo $2$, of flow lines of $-\nabla f$ from $p$ to $q$, counted up to time shift; it is finite.
Let $\partial \colon C_k \to C_{k-1}$ be the linear map with $\partial p = \sum_q n(p, q) \, q$.
Then $\partial \circ \partial = 0$, and the *Morse homology* of $(f, g)$ is the homology of the chain complex $(C_*, \partial)$.

## Remarks

The Morse homology is isomorphic to $H_*(M; \Z/2)$, so it does not depend on $f$ or $g$.
With a choice of orientations of the unstable manifolds, one can count flow lines with signs and get a chain complex over $\Z$ whose homology is $H_*(M; \Z)$.
The identity $\partial^2 = 0$ comes from broken flow lines $p \to q \to r$ with index drop $2$.
They are exactly the ends of the one-dimensional spaces of flow lines from $p$ to $r$, and these ends come in pairs.
Example: the height function on the round sphere $S^n$, $n \ge 1$, has one critical point of index $0$ and one of index $n$.
For $n \ge 2$ the indices differ by more than one, so $\partial = 0$.
For $n = 1$ there are two flow lines from the maximum to the minimum, so again $\partial = 0$ modulo $2$.
In both cases the homology is $\Z/2$ in degrees $0$ and $n$.
Non-example: take a metric on the upright torus in which the flow line leaving the upper saddle runs straight into the lower saddle.
Then $W^u$ of the upper saddle and $W^s$ of the lower saddle meet along a curve, so they are not transverse.
The pair is not Morse–Smale and the definition does not apply; a small change of the metric removes the problem.
