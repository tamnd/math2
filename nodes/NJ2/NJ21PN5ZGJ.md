---
tag: NJ21PN5ZGJ
kind: concept
name: Connection on a principal bundle
msc: [53C05]
specializes: [TD6VEP3SCE]
sources:
  - url: https://en.wikipedia.org/wiki/Connection_(principal_bundle)
same_as:
  wikidata: Q2920850
  wikipedia: Connection (principal bundle)
---

## Summary

A connection on a [[principal bundle|8E37E74XVP]] with structure group $G$ is an [[Ehresmann connection|TD6VEP3SCE]] that is invariant under the action of $G$.
It is usually given by a connection form, a $1$-form on the total space with values in the Lie algebra of $G$.
A principal connection induces connections on all associated vector bundles, so it is the universal form of a connection.
In physics these connections are the gauge fields, and their curvature is the field strength.

## Explanations

### L1 human

A principal bundle has, above each point of the base, a copy of a symmetry group whose origin has not been fixed.
A connection tells how to move from one fibre to a nearby one, and it must respect the symmetry.
The connection form does this by reading off, from each tangent vector, how fast it moves along the group direction.
For the trivial bundle $M \times G$ there is a flat choice: moving in $M$ while staying at the same group element.
