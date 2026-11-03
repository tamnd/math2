---
tag: TV0GX7AQWT
kind: concept
name: NK groups
msc: [19D35]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebraic_K-theory
---

## Summary

The groups $NK_n(R)$ measure how far the K-theory of a polynomial ring $R[t]$ differs from the K-theory of $R$.
The group $K_n(R[t])$ splits as $K_n(R) \oplus NK_n(R)$.
They vanish when $R$ is regular Noetherian, which is the homotopy invariance of K-theory.
They appear twice in the fundamental theorem for Laurent polynomial rings, and they are often large when they are not zero.

## Explanations

### L1 human

Adding a variable $t$ to a nice ring does not change its K-theory.
For rings with nilpotent elements this fails, and $NK_n(R)$ is exactly the new part.
For example, if $\varepsilon^2 = 0$ in $R$, then $1 + \varepsilon t$ is an invertible polynomial, with inverse $1 - \varepsilon t$.
It gives a new element of $K_1(R[t])$ that disappears when $t$ is set to $0$, so it lies in $NK_1(R)$.
