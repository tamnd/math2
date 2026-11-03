---
tag: JHXNTZCYQ1
kind: definition
name: Wick rotation
msc: [81T08, 81S40, 81T05]
defines: G686S8SEK0
uses: [0M3YQJ81NB, 0NEGN5CRSC, 18KPYRRPZY]
sources:
  - url: https://en.wikipedia.org/wiki/Wick_rotation
---

## Definition

Let $d \ge 1$ and let $(t, \mathbf{x}) \in \R \times \R^d$ be coordinates on Minkowski space with quadratic form $t^2 - \abs{\mathbf{x}}^2$.
The *Wick rotation* is the substitution $t = -i\tau$ with $\tau \in \R$.
It sends the Minkowski form to $-(\tau^2 + \abs{\mathbf{x}}^2)$, the negative of the Euclidean form on $\R^{d+1}$.
Let $F(t, \mathbf{x})$ be the boundary value on the real $t$-axis of a function analytic in $t$ in the open lower half-plane.
Its Wick rotation is the [[analytic continuation|0M3YQJ81NB]] evaluated on the negative imaginary axis $t = -i\tau$, $\tau > 0$.

## Remarks

Example: let $H \ge 0$ be a [[self-adjoint operator|0NEGN5CRSC]] on a Hilbert space.
By the [[spectral theorem|18KPYRRPZY]], $z \mapsto e^{-izH}$ is defined and bounded by $1$ in norm for $\operatorname{Im} z \le 0$, strongly continuous there, and analytic in the open lower half-plane.
At $z = -i\tau$ it gives the contraction semigroup $e^{-\tau H}$.
So the Wick rotation of the unitary group $e^{-itH}$ is the semigroup $e^{-\tau H}$.

Non-example: let $H$ be self-adjoint but not bounded below.
For $\operatorname{Im} z < 0$, the function $\abs{e^{-izE}} = e^{E \operatorname{Im} z}$ is unbounded on the spectrum, and $e^{-\tau H}$ is an unbounded operator.
So the continuation into the lower half-plane fails as a bounded family.

The sign is a convention: with $t = i\tau$ one continues into the upper half-plane and uses negative energies.
Under the rotation, the Lorentz group of the Minkowski form is traded for the rotation group of Euclidean space.
