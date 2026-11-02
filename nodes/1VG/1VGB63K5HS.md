---
tag: 1VGB63K5HS
kind: statement
role: proposition
name: Conformal invariance of harmonic functions
msc: [31A05, 30C35]
uses: [0DEB0JMN0W, 0NAHXR1FRH, 0YYT36R4YD, CVDGP7DKZ3, 0E0B6RA8K0]
about: [0DEB0JMN0W, 0YYT36R4YD]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_map
---

## Statement

Let $U, V \subseteq \C$ be open sets and let $\varphi \colon U \to V$ be a [[holomorphic function|0NAHXR1FRH]].
Let $h \colon V \to \R$ be a [[harmonic function|0DEB0JMN0W]].
Then $h \circ \varphi$ is harmonic on $U$.
In particular, let $\varphi$ be a [[conformal map|0YYT36R4YD]] of $U$ onto $V$.
Then $h$ is harmonic on $V$ if and only if $h \circ \varphi$ is harmonic on $U$.

## Remarks

Proof idea: near a point $\varphi(z_0)$, [[harmonic conjugates exist locally|CVDGP7DKZ3]], so $h = \operatorname{Re} F$ for a holomorphic $F$ on a disc around $\varphi(z_0)$.
Then $h \circ \varphi = \operatorname{Re}(F \circ \varphi)$ near $z_0$, and $F \circ \varphi$ is holomorphic.
A direct computation gives $\Delta (h \circ \varphi) = \abs{\varphi'}^2 \, (\Delta h) \circ \varphi$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
Example: $h(w) = \log\abs{w}$ is harmonic on $\C \setminus \set{0}$, and with $\varphi(z) = z^2$ one gets $h(\varphi(z)) = 2 \log\abs{z}$, again harmonic.
Holomorphy of $\varphi$ is needed: for the smooth map $\varphi(x, y) = (x, y^2)$ and $h(s, t) = s^2 - t^2$, the function $h \circ \varphi = x^2 - y^4$ has Laplacian $2 - 12 y^2 \ne 0$.
The statement also holds for antiholomorphic $\varphi$, because $h \circ \bar\varphi$ equals $\tilde h \circ \varphi$ with $\tilde h(w) = h(\bar w)$, which is harmonic.

## Explanations

### L1 human

Harmonic functions in the plane survive a change of coordinates by a holomorphic map.
So one may move a problem about harmonic functions from a complicated region to a simple one, such as a disc, solve it there, and move the answer back.

### L2 human

This is the basis of conformal methods in planar potential theory.
With the Riemann mapping theorem, the Dirichlet problem on a simply connected domain reduces to the disc, where the Poisson integral solves it.
The same invariance makes harmonic measure and Green's functions conformally invariant.
It also shows that harmonicity makes sense on a Riemann surface, since the transition maps between charts are holomorphic.
