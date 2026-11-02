---
tag: CFHNV77ZMD
kind: object
name: Path space of a manifold
msc: [58D15, "58E10", 58B20]
instance_of: [R8DMMW0E9M]
uses: [F45VQ47GPV, 7CBT4SM83Y, M4CEZ5K9HP, NSYMQMHPDN, 2JFF5F3EGF]
sources:
  - url: https://en.wikipedia.org/wiki/Path_space_(algebraic_topology)
---

## Description

Let $M$ be a smooth manifold of dimension $n$ and fix points $p, q \in M$.
The *path space* $\Omega_{p,q} M$ is the set of paths $\gamma \colon [0, 1] \to M$ of [[Sobolev class|M4CEZ5K9HP]] $H^1$ with $\gamma(0) = p$ and $\gamma(1) = q$.
Here $H^1$ means that in local coordinates the path is absolutely continuous with square-integrable derivative.

## Remarks

The path space is a Hilbert manifold.
Choose a complete [[Riemannian metric|7CBT4SM83Y]] on $M$.
For a smooth path $\gamma$ from $p$ to $q$, let $T_\gamma$ be the Hilbert space of $H^1$ vector fields $\xi$ along $\gamma$ with $\xi(0) = \xi(1) = 0$.
Small $\xi \in T_\gamma$ give paths $t \mapsto \exp_{\gamma(t)}(\xi(t))$ from $p$ to $q$, and these maps are charts with smooth chart changes.
Every $H^1$ path is close to a smooth one, so these charts cover $\Omega_{p,q} M$, and each model space $T_\gamma$ is isomorphic to $H^1_0([0, 1]; \R^n)$.

On this Hilbert manifold the energy $E(\gamma) = \frac{1}{2} \int_0^1 \abs{\gamma'(t)}^2 \, dt$ is a smooth function whose critical points are the [[geodesics|NSYMQMHPDN]] from $p$ to $q$.
The inclusion of piecewise smooth or smooth paths into $\Omega_{p,q} M$ is a homotopy equivalence.
For connected $M$ the space is homotopy equivalent to the based [[loop space|2JFF5F3EGF]] of $M$.


## Explanations

### L1 human

The path space collects all routes from $p$ to $q$ in $M$, each route being one point of the space.
Using paths with square-integrable speed, rather than smooth ones, makes the space a Hilbert manifold, which is the right setting for calculus of variations.
The shortest and, more generally, the locally straightest routes are the geodesics, and they appear as the critical points of the energy on this space.
This is the starting point of Morse theory of geodesics.
