---
tag: R56VTW55SG
kind: definition
name: Normal scheme
msc: [14A15, 13B22]
defines: EK261G1XP9
uses: [5A35TYZD02, JTAKAPTT8H, H20P600HQS, KR7SWBYHRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_scheme
---

## Definition

A [[scheme|5A35TYZD02]] $X$ is *normal* if for every point $x \in X$ the [[stalk|JTAKAPTT8H]] $\mathcal{O}_{X,x}$ is an [[integrally closed domain|H20P600HQS]].

## Remarks

An affine scheme $\operatorname{Spec} A$ is normal if and only if $A_{\mathfrak p}$ is an integrally closed domain for every prime $\mathfrak{p}$, that is, $A$ is a [[normal ring|KR7SWBYHRQ]].
For an integral domain $A$, this holds if and only if $A$ is integrally closed.
Example: $\operatorname{Spec} \Z$ is normal, since $\Z$ is a unique factorization domain and hence integrally closed.
Non-example: let $A = k[x, y]/(y^2 - x^3)$ for a field $k$; it is a domain.
The element $t = y/x$ of its field of fractions satisfies $t^2 - x = 0$, which is monic over $A$, but $t \notin A$.
So $A$ is not integrally closed, and the cusp $\operatorname{Spec} A$ is not normal; the failure is at the origin.
A normal scheme is reduced, but it need not be irreducible: a disjoint union of two normal schemes is normal.
