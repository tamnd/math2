---
tag: 37TNNBQ4PK
kind: concept
name: Hasse–Weil zeta function
msc: [14G10, 11G40, 11M41]
sources:
  - url: https://en.wikipedia.org/wiki/Hasse%E2%80%93Weil_zeta_function
same_as:
  wikidata: Q2372257
  wikipedia: Hasse–Weil zeta function
---

## Summary

The Hasse–Weil zeta function of a variety over a number field is an Euler product.
It packs together the numbers of points of the variety modulo all primes.
For a point it is the [[Riemann zeta function|1XWBY4N0VT]] or the [[Dedekind zeta function|KXS5DQDFYD]].
For an [[elliptic curve|427N6S6QQW]] it is built from the $L$-function of the [[Birch and Swinnerton-Dyer conjecture|ZWEFBG40H9]].
Its analytic continuation, functional equation and special values are the subject of deep conjectures, some of them proved through the [[modularity theorem|CS1NVJBZMH]].

## Explanations

### L1 human

Riemann's zeta function can be written as a product over all primes $p$ of the factors $(1 - p^{-s})^{-1}$.
The Hasse–Weil zeta function does the same for a system of polynomial equations with integer coefficients.
For each prime $p$, one counts the solutions modulo $p$ and in the finite fields of order $p^2, p^3, \ldots$, and turns these counts into a local factor.
The product of the local factors over all primes is the Hasse–Weil zeta function.
For an elliptic curve $E$ over $\Q$, it equals $\zeta(s)\zeta(s-1)/L(E, s)$, up to finitely many factors at the bad primes.
