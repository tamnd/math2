---
tag: 7VPJWF0AZ7
kind: concept
name: Irreducible analytic germ
msc: [32B10, 32B05]
specializes: [Q9B74BYZ8C]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_analytic_variety
---

## Summary

An irreducible analytic germ is a nonempty [[germ of an analytic set|Q9B74BYZ8C]] that is not the union of two strictly smaller analytic germs.
Equivalently, its ideal in the ring of holomorphic germs is a prime ideal.
Since this ring is Noetherian, every analytic germ is a finite union of irreducible germs.
The irreducible germs are the building blocks of local analytic geometry.

## Explanations

### L1 human

Near a point, an analytic set may consist of several pieces that only meet at the point, like two lines crossing.
An irreducible germ is one that cannot be split in this way.
The cusp $\set{z_1^2 = z_2^3}$ is irreducible at the origin, although it is singular there.
The node $\set{z_2^2 = z_1^2(1 + z_1)}$ is irreducible as a global curve, but its germ at the origin is the union of two smooth branches, so it is reducible there.
