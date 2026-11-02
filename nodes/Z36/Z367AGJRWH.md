---
tag: Z367AGJRWH
kind: definition
name: Lattice in a Lie group
msc: ["22E40"]
defines: BTYF5Y5PFY
uses: [7JBRGCVJRB, 5M7D1BSHVZ, VY0HXD3GC4]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_(discrete_subgroup)
    locator: Definition
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]] and let $\Gamma$ be a [[discrete subgroup|5M7D1BSHVZ]] of $G$.
The group $G$ acts on the coset space $G/\Gamma$ by left multiplication.
The subgroup $\Gamma$ is a *lattice* in $G$ if there is a nonzero finite Borel measure on $G/\Gamma$ that is invariant under this action.
A lattice $\Gamma$ is *uniform*, or *cocompact*, if $G/\Gamma$ is compact, and *non-uniform* otherwise.

## Remarks

When such a measure exists, it is unique up to a positive factor and is induced by a [[Haar measure|VY0HXD3GC4]] $\mu$ of $G$.
The total mass of $G/\Gamma$ for the measure induced by $\mu$ is the *covolume* of $\Gamma$.
A Lie group that contains a lattice is unimodular.
Example: $\Z^n$ is a uniform lattice in $\R^n$, because $\R^n/\Z^n$ is a compact torus whose Lebesgue measure is finite and invariant under translations.
Example: $\mathrm{SL}_2(\Z)$ is a non-uniform lattice in $\mathrm{SL}_2(\R)$; the modular surface has finite hyperbolic area $\pi/3$ but is not compact.
Non-example: $\Z \times \set{0}$ is discrete in $\R^2$, but $\R^2/(\Z \times \set{0})$ is an infinite cylinder, and any invariant measure is a multiple of its infinite area measure.
Non-example: the subgroup $\Z + \sqrt{2}\,\Z$ of $\R$ is dense, not discrete, so it is not a lattice.
