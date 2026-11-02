---
tag: TY7Y32MCH1
kind: concept
name: Banach analytic space
msc: [32K05, 46G20]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite-dimensional_holomorphy
---

## Summary

A Banach analytic space is an infinite-dimensional analogue of a [[complex analytic space|HXSZA44J5J]].
It is modelled locally on the zero set of a [[holomorphic map|E8N3EC0YH5]] from an open subset of a complex [[Banach space|06GZ956657]] to another one.
The notion was introduced by Douady to construct the space of compact complex subspaces of a given complex space.
Complex analytic spaces and [[Banach manifolds|9K15AMGBV9]] over $\C$ are Banach analytic spaces.
They are used in deformation theory.
Spaces of maps or of subspaces are first built as Banach analytic spaces, and then shown to be finite-dimensional.

## Explanations

### L1 human

A finite-dimensional complex space is cut out locally by finitely many holomorphic equations in $\C^n$.
In a Banach analytic space the ambient space $\C^n$ is replaced by an infinite-dimensional Banach space, and the equations take values in another Banach space.
For example, any open subset of a complex Banach space is a Banach analytic space with no equations at all.
The equation $\ip{x}{x} = 1$ of the unit sphere in a complex Hilbert space $H$ is not allowed, because $x \mapsto \ip{x}{x}$ is not holomorphic.
But the zero set of any holomorphic map from $H$ to another Banach space is.
