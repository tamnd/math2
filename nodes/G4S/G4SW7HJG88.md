---
tag: G4SW7HJG88
kind: concept
name: Hurwitz zeta function
msc: [11M35, 11M06]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz_zeta_function
same_as:
  wikidata: Q1638777
  wikipedia: Hurwitz zeta function
---

## Summary

The Hurwitz zeta function $\zeta(s, a)$ is the sum of $(n + a)^{-s}$ over all integers $n \ge 0$.
It is a shifted version of the [[Riemann zeta function|1XWBY4N0VT]], which is the case $a = 1$.
Every [[Dirichlet L-function|9D2Z543EJQ]] modulo $q$ is $q^{-s}$ times a finite linear combination of the functions $\zeta(s, r/q)$, so their analytic properties follow from those of $\zeta(s, a)$.

## Explanations

### L1 human

The Riemann zeta function adds up $1/n^s$ for $n = 1, 2, 3, \ldots$.
The Hurwitz zeta function does the same, but starts the counting at a point $a$ instead of at $1$: it adds $1/a^s$, $1/(a+1)^s$, $1/(a+2)^s$, and so on.
For $a = 1$ you get back the Riemann zeta function.
For $a = 1/2$ you add the $s$-th powers of $2, 2/3, 2/5, \ldots$, and this sum equals $(2^s - 1)\zeta(s)$.
Sums over an arithmetic progression, such as $1/1^s + 1/4^s + 1/7^s + \cdots$, are Hurwitz zeta values up to a factor.
