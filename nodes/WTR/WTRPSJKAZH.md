---
tag: WTRPSJKAZH
kind: definition
name: Cobordism
msc: [57R75, 55N22]
defines: T8BVGPPSZP
uses: [F45VQ47GPV, 7DS6B2BFK8, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Cobordism
---

## Definition

Let $n \ge 0$ and let $M$ and $N$ be closed (compact, without boundary) [[smooth manifolds|F45VQ47GPV]] of dimension $n$.
A *cobordism* between $M$ and $N$ is a compact smooth [[manifold with boundary|7DS6B2BFK8]] $W$ of dimension $n + 1$ with $\partial W$ diffeomorphic to $M \sqcup N$.
The manifolds $M$ and $N$ are *cobordant* if a cobordism between them exists.

## Remarks

Being cobordant is an [[equivalence relation|0G8VEZ3WTK]]: $M \times [0, 1]$ gives reflexivity, and two cobordisms can be glued along a common boundary component for transitivity.
The set of classes $\Omega_n^O$ is an abelian group under disjoint union, and every element has order $2$, since $M \sqcup M$ bounds $M \times [0, 1]$.
In the oriented version, $W$ is oriented and $\partial W \cong M \sqcup (-N)$, where $-N$ is $N$ with the opposite orientation; this gives the groups $\Omega_n^{SO}$.

Example: the circle $S^1$ bounds the disc $D^2$, so $S^1$ is cobordant to the empty manifold.
Every sphere $S^n = \partial D^{n+1}$ is likewise null-cobordant.

Non-example: the real projective plane $\R P^2$ is not the boundary of any compact $3$-manifold.
A closed manifold $M$ that bounds a compact manifold $W$ has even Euler characteristic, but $\chi(\R P^2) = 1$.

A manifold cobordant to the empty manifold is called null-cobordant.
