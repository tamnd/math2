---
tag: 3C73HND6XA
kind: concept
name: Automorphic form
msc: [11F70, 11F12, "22E55"]
sources:
  - url: https://en.wikipedia.org/wiki/Automorphic_form
same_as:
  wikidata: Q1134435
  wikipedia: Automorphic form
---

## Summary

An automorphic form is a function on a Lie group $G$ that is invariant under a discrete subgroup $\Gamma$.
It must also satisfy strong finiteness and growth conditions.
[[Modular forms|GWKN5VG78A]] and [[Maass wave forms|3R959YSNYP]] give the basic examples, for the group $\mathrm{SL}_2(\R)$ and $\Gamma = \mathrm{SL}_2(\Z)$ or a congruence subgroup.
Automorphic forms carry deep arithmetic information, and they are one side of the correspondences predicted by the [[Langlands program|J9T2M084W5]].

## Explanations

### L1 human

A periodic function on the line repeats under the group of integer shifts.
An automorphic form is the same idea for a much richer group of symmetries.
An example is the group of real $2 \times 2$ matrices of determinant one, with its subgroup of integer matrices.
Because so many symmetries are imposed, only special functions survive, and the space of such functions with given extra conditions is finite-dimensional.
For example, the discriminant function $\Delta(z) = q \prod_{n \ge 1} (1 - q^n)^{24}$ with $q = e^{2\pi i z}$ is a modular form, and so gives an automorphic form on $\mathrm{SL}_2(\R)$.
Its coefficients encode facts about primes, which is why number theorists care about these functions.
