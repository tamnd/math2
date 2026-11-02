---
tag: D44KAF8PNK
kind: problem
name: Second Cousin problem
msc: [32A20, "32E10", 32L10]
uses: [JSGWAN2RJV, W6FTSF57T1, 507C34W0ZT, QAC7BYK9KX]
about: [W6FTSF57T1]
sources:
  - url: https://en.wikipedia.org/wiki/Cousin_problems
history:
  posed_by: "Pierre Cousin"
  first_stated: "1895"
---

## Problem

Let $X$ be a connected [[complex manifold|JSGWAN2RJV]] and let $(U_i)_{i \in I}$ be an open cover of $X$.
For each $i$, let $f_i$ be a [[meromorphic function|W6FTSF57T1]] on $U_i$ that is not identically zero on any component of $U_i$.
Assume that $f_i / f_j$ is [[holomorphic|507C34W0ZT]] and nowhere zero on $U_i \cap U_j$ for all $i, j$.
Find a meromorphic function $f$ on $X$ such that $f / f_i$ is holomorphic and nowhere zero on $U_i$ for every $i$.

## Remarks

The data prescribe the zeros and poles of $f$ with multiplicities, that is, a divisor on $X$.
The problem asks whether this divisor is the divisor of a global meromorphic function.
The quotients $g_{ij} = f_i / f_j$ form a Čech $1$-cocycle with values in the sheaf $\mathcal{O}^*$ of nowhere-zero holomorphic functions, and they define a [[holomorphic line bundle|QAC7BYK9KX]].
The problem is solvable for these data if and only if this line bundle is holomorphically trivial.
So if $H^1(X, \mathcal{O}^*) = 0$, every second Cousin problem on $X$ is solvable.
On a Stein manifold, Cartan's theorem B and the exponential sequence $0 \to \Z \to \mathcal{O} \to \mathcal{O}^* \to 0$ give an isomorphism $H^1(X, \mathcal{O}^*) \cong H^2(X, \Z)$.
Hence on a Stein manifold the problem is solvable if and only if the line bundle is topologically trivial, a result of Oka.
In particular it is always solvable on a Stein manifold with $H^2(X, \Z) = 0$, for example on $\C^n$ or on a convex domain.
For a domain in $\C$ the problem is solved by the Weierstrass factorization theorem.
There are domains of holomorphy on which some second Cousin problem has no solution.
An example is $X = \set{(z, w) \in \C^2 : (\log \abs{z})^2 + (\log \abs{w})^2 < 1}$, a logarithmically convex Reinhardt domain that retracts onto the torus $\abs{z} = \abs{w} = 1$, so $H^2(X, \Z) \cong \Z$.
A holomorphic line bundle on $X$ with nonzero Chern class has a meromorphic section that is not identically zero, and its local expressions are second Cousin data without solution.

## Explanations

### L1 human

In one variable, Weierstrass showed how to build a holomorphic function with prescribed zeros and multiplicities.
The second Cousin problem asks the same in several variables, where zeros form hypersurfaces rather than isolated points.
Given local functions that define the wanted zeros and poles near each point, one wants one global function that defines them everywhere.
Unlike the first Cousin problem, this one can fail even on very nice domains, for a topological reason.
Oka showed that on Stein manifolds topology is the only obstruction.
