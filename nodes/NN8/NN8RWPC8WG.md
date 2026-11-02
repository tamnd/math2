---
tag: NN8RWPC8WG
kind: concept
name: Reflexive space
msc: [46B10]
specializes: [06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Reflexive_space
same_as:
  wikidata: Q2032198
  wikipedia: Reflexive space
---

## Summary

A normed space is reflexive when the [[canonical embedding into its bidual|QKR3D65TTH]] is onto.
Reflexive spaces are always [[Banach spaces|06GZ956657]].
They are the Banach spaces whose closed unit ball is weakly compact.
So bounded sequences have weakly convergent subsequences, which makes them the natural setting for existence proofs by minimization.
Hilbert spaces, $L^p$ spaces for $1 < p < \infty$ and finite-dimensional spaces are reflexive.

## Explanations

### L1 human

Every normed space sits inside its double dual, the dual of the dual.
In a reflexive space the double dual has nothing more: going to the dual twice brings you back to where you started.
For example, the dual of $\ell^2$ is $\ell^2$ again, so $\ell^2$ is reflexive.
The space $c_0$ of null sequences is not reflexive: its double dual is the bigger space $\ell^\infty$ of all bounded sequences.
