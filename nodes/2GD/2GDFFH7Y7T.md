---
tag: 2GDFFH7Y7T
kind: concept
name: Lagrange resolvent
msc: [12F10, "12E12"]
sources:
  - url: https://en.wikipedia.org/wiki/Resolvent_(Galois_theory)
---

## Summary

A Lagrange resolvent is a sum $\alpha + \zeta \sigma(\alpha) + \cdots + \zeta^{n-1} \sigma^{n-1}(\alpha)$ built from an element $\alpha$, an automorphism $\sigma$ of order $n$ and an $n$-th [[root of unity|0YV2CKP2AV]] $\zeta$.
The automorphism $\sigma$ multiplies it by $\zeta^{-1}$, so its $n$-th power is fixed by $\sigma$.
This turns a [[cyclic extension|VFE5B71E7Y]] into an extension obtained by adjoining an $n$-th root, which is the key step in solving equations by radicals.
Lagrange used such sums of the roots to explain the formulas for cubic and quartic equations.

## Explanations

### L1 human

Suppose the roots of an equation are permuted in a cycle by a symmetry.
Mix the roots with weights $1, \zeta, \zeta^2, \ldots$ that are powers of a root of unity.
Turning the cycle once only multiplies this mix by a root of unity, so a suitable power of the mix does not change at all.
That power is then a known quantity, and the mix is one of its $n$-th roots.
For a quadratic with roots $r_1, r_2$ the resolvent is $r_1 - r_2$, and its square $(r_1 - r_2)^2$ is the discriminant, which is why the quadratic formula has a square root.
