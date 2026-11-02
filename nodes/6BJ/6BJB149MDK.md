---
tag: 6BJB149MDK
kind: statement
role: theorem
name: Oka's solution of the Levi problem
msc: ["32E40", 32T05]
uses: [4487CSC0MB, AHYZMSBBNH, FGSKR6ZS3Q, FF2P7ER3QT, 1XCBCB3MD7, 80MTNXWW80]
about: [47CVS9RJ9D, 4487CSC0MB, AHYZMSBBNH]
sources:
  - url: https://en.wikipedia.org/wiki/Stein_manifold
---

## Statement

Let $\Omega \subseteq \C^n$ be a domain.
The following are equivalent:

1. $\Omega$ is a [[domain of holomorphy|4487CSC0MB]].
2. $\Omega$ is [[pseudoconvex|AHYZMSBBNH]].
3. $\Omega$ has a continuous [[plurisubharmonic exhaustion function|FGSKR6ZS3Q]].

## Remarks

The implication from 1 to 3 is the easy one.
Let $d(z)$ be the distance from $z$ to $\partial\Omega$; on a domain of holomorphy $\Omega \ne \C^n$, the function $-\log d$ is [[plurisubharmonic|FF2P7ER3QT]].
Then $\max(-\log d(z), \abs{z}^2)$ is a continuous plurisubharmonic exhaustion function.
The hard implication, from 3 to 1, is the solution of the [[Levi problem|47CVS9RJ9D]].
For each boundary point one needs a holomorphic function on $\Omega$ that cannot be continued past it.
Oka built such functions with his own methods; his proof for general $n$ used his theory of coherent ideal sheaves.
Hörmander later obtained them by solving $\bar\partial u = f$ with $L^2$ estimates for weights $e^{-k\varphi}$, where $\varphi$ is the exhaustion function.
Example: any convex domain $\Omega$ is pseudoconvex, so it is a domain of holomorphy.
For convex domains this can also be seen directly with the functions $1/\ell$.
Here $\ell$ is an affine complex-linear function that vanishes at a given boundary point and nowhere on $\Omega$.
The same equivalence holds for unramified Riemann domains over $\C^n$.

## Explanations

### L1 human

A domain of holomorphy is a domain that is the natural home of some holomorphic function, one that cannot be pushed past any boundary point.
Pseudoconvexity is a convexity condition on the shape of the domain.
The theorem says that the two notions are the same.
So an analytic question, whether every holomorphic function extends, becomes a geometric question about the boundary.

### L2 human

The theorem completes the [[Cartan–Thullen theorem|1XCBCB3MD7]], which says that domains of holomorphy are the holomorphically convex domains.
Together they give four equivalent conditions on a domain in $\C^n$: domain of holomorphy, holomorphically convex, pseudoconvex, and Stein.
For domains with $C^2$ boundary, pseudoconvexity can be checked with the [[Levi form|80MTNXWW80]], so this gives a computable test.
Grauert's theorem extends the result from domains to complex manifolds.
