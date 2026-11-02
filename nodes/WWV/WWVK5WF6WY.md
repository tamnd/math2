---
tag: WWVK5WF6WY
kind: definition
name: Parabolic and hyperbolic Riemann surfaces
msc: [30F20, 30F15, 31C12]
defines: RHNJECZ9WR
uses: [5K0N8QMV6Q, P214QJ0S3B, Z1MHMGFNFW, T12FSF2J2V, C95QJ7YH5T, M36SD56MWQ, Y1YPE6PM52]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_surface
---

## Definition

Let $X$ be a connected [[Riemann surface|5K0N8QMV6Q]].
A function on $X$ is subharmonic if it is a [[subharmonic function|Z1MHMGFNFW]] in every holomorphic chart, as for [[harmonic functions on Riemann surfaces|P214QJ0S3B]].

1. $X$ is *hyperbolic* if there is a nonconstant subharmonic function $u$ on $X$ with $u < 0$ on $X$.
2. $X$ is *parabolic* if $X$ is not compact and not hyperbolic.

## Remarks

Equivalently, $X$ is hyperbolic if and only if it has a Green's function.
This is the smallest positive harmonic function on $X \setminus \set{a}$ with a logarithmic pole at $a$.
A compact Riemann surface is never hyperbolic, because a subharmonic function on it attains its maximum and is therefore constant; such surfaces are sometimes called elliptic.
Example: the unit disc $\mathbb{D}$ is hyperbolic, since $u(z) = \abs{z}^2 - 1$ is subharmonic, nonconstant and negative on $\mathbb{D}$.
Non-example: the plane $\C$ is not hyperbolic.
By the subharmonic form of [[Liouville's theorem|T12FSF2J2V]], a subharmonic function on $\C$ that is bounded above is constant.
As $\C$ is not compact, it is parabolic.
A domain $\Omega \subseteq \C$ is hyperbolic if and only if its boundary is not a [[polar set|C95QJ7YH5T]].
Its Green's function is then the classical [[Green's function|M36SD56MWQ]] of $\Omega$.
This notion differs from the one in the uniformization theorem, which classifies $X$ by its [[universal cover|Y1YPE6PM52]].
For example, $\C \setminus \set{0, 1}$ has the disc as universal cover, but it is parabolic, because a subharmonic function bounded above extends across the two punctures to all of $\C$.
