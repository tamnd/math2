---
tag: 5ZYRRVE8BW
kind: concept
name: Connection on a vector bundle
msc: [53C05]
sources:
  - url: https://en.wikipedia.org/wiki/Connection_(vector_bundle)
same_as:
  wikidata: Q521075
  wikipedia: Connection (vector bundle)
---

## Summary

A connection on a vector bundle is a rule for differentiating [[sections|WWX7H5W1RP]] of the bundle in the direction of tangent vectors.
It is needed because the fibres over different points are different vector spaces.
So there is no built-in way to compare a section at nearby points.
A connection gives covariant derivatives, parallel transport, curvature and holonomy.
Connections on the tangent bundle are the affine connections, such as the Levi-Civita connection.
Connections on other bundles are the gauge fields of physics.

## Explanations

### L1 human

A section of a vector bundle puts a vector in a separate vector space above each point.
To say whether such a section is "constant" you must compare vectors in different spaces, and nothing tells you how.
A connection is the extra data that says how to differentiate the section, and so how to compare nearby fibres.
On the trivial bundle $\R^n \times \R^r$ one can just differentiate each component, and this is the simplest connection.
On a twisted bundle, such as the tangent bundle of a sphere, there is no such obvious choice.
