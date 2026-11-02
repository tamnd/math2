---
tag: F3YMFK4S5J
kind: concept
name: Synthetic differential geometry
msc: [51K10, 18F40, 58A03]
sources:
  - url: https://en.wikipedia.org/wiki/Synthetic_differential_geometry
same_as:
  wikidata: Q7662747
  wikipedia: Synthetic differential geometry
---

## Summary

Synthetic differential geometry develops differential calculus and differential geometry with genuine infinitesimals, inside a [[topos|6837RS7N82]] instead of the category of sets.
Its basic object is a number line $R$ whose set $D$ of elements of square zero is not reduced to $0$.
By the Kock–Lawvere axiom, every function from $D$ to $R$ is affine.
Tangent vectors become maps from the infinitesimal set $D = \set{d : d^2 = 0}$ into a space, and derivatives are defined without limits.
Models built from [[C-infinity rings|4EJED0YZBB]] show that the theory is consistent and contains ordinary smooth manifolds.

## Explanations

### L1 human

Physicists and early analysts often computed with tiny quantities whose square is zero.
Synthetic differential geometry makes this rigorous.
In it, $f(x + d) = f(x) + d\, f'(x)$ holds exactly for every infinitesimal $d$, and this equation defines $f'(x)$.
The price is a different logic: one cannot assume that every number is either zero or not zero.
