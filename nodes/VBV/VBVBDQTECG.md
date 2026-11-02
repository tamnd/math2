---
tag: VBVBDQTECG
kind: definition
name: Closed geodesic
msc: [53C22, "58E10"]
defines: 4MCCP8GG4J
uses: [7CBT4SM83Y, NSYMQMHPDN]
sources:
  - url: https://en.wikipedia.org/wiki/Closed_geodesic
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]].
A *closed geodesic* is a nonconstant [[geodesic|NSYMQMHPDN]] $\gamma \colon \R \to M$ that is periodic: there is $T > 0$ with $\gamma(t + T) = \gamma(t)$ for all $t \in \R$.
Two closed geodesics are *geometrically distinct* if their images are different sets.

## Remarks

Equivalently, a closed geodesic is a smooth map $\gamma \colon \R / T\Z \to M$ that satisfies the geodesic equation and is not constant.
A geodesic $\gamma$ is closed if and only if $\gamma(T) = \gamma(0)$ and $\dot\gamma(T) = \dot\gamma(0)$ for some $T > 0$, by uniqueness of geodesics with given initial point and velocity.
The closed geodesics are the critical points with positive energy of the energy functional $E(\gamma) = \frac{1}{2} \int_0^1 \abs{\dot\gamma}^2 \, dt$ on the [[free loop space|SGGXZ3TBSA]] of $M$.
Each closed geodesic of period $T$ gives infinitely many critical points, its iterates $t \mapsto \gamma(kt)$ for $k \ge 1$, which is why counting geometrically distinct ones is hard.

Example: on the unit sphere $S^2 \subset \R^3$, the great circle $\gamma(t) = (\cos t, \sin t, 0)$ is a geodesic with period $2\pi$, so it is a closed geodesic.

Non-example: on the flat torus $\R^2 / \Z^2$, the geodesic $\gamma(t) = (t, \sqrt{2}\, t) \bmod \Z^2$ is not periodic.
Indeed $\gamma(t + T) = \gamma(t)$ would need $T \in \Z$ and $\sqrt{2}\, T \in \Z$, which is impossible for $T > 0$.
