---
tag: R45FHBE15X
kind: concept
name: Kummer–Artin–Schreier–Witt theory
msc: [12F10, 13F35, 12G05]
sources:
  - url: https://en.wikipedia.org/wiki/Witt_vector
---

## Summary

Kummer–Artin–Schreier–Witt theory describes the [[abelian extensions|EQDEXBWGJH]] of bounded exponent of a [[field|04C5ZBG1WT]] by explicit equations.
For an exponent $m$ prime to the [[characteristic|1ZB13N78XW]], this is [[Kummer theory|XZQENYV15Y]].
It uses $m$-th roots and needs the $m$-th [[roots of unity|0YV2CKP2AV]] in the base field.
For an exponent $p^n$ in characteristic $p > 0$, this is Artin–Schreier–Witt theory.
It uses equations $F(x) - x = a$ in the ring of [[Witt vectors|6N3X2QX4W9]] of length $n$.
For $n = 1$ it reduces to [[Artin–Schreier theory|7YNMNRGH3T]].
Together the two parts describe all finite cyclic extensions of a field that contains enough roots of unity.

## Explanations

### L1 human

Kummer theory builds extensions by adjoining roots such as $\sqrt[m]{a}$.
In characteristic $p$ this fails for $m = p$, because $x^p - a$ has only one root, repeated.
Artin and Schreier replaced $x^p = a$ by $x^p - x = a$, which gives the cyclic extensions of degree $p$.
Witt found that to reach cyclic extensions of degree $p^2, p^3, \ldots$ one must solve the same kind of equation with Witt vectors in place of field elements.
For example, over the finite field $\F_p$ the Frobenius map fixes every Witt vector, because $c^p = c$ for each $c \in \F_p$.
From this the theory recovers that $\F_p$ has exactly one extension of each degree $p^n$, and that it is cyclic.
