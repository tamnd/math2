---
tag: WHME2NGANG
kind: concept
name: Filtration of a module
msc: [13A30, 13C05]
sources:
  - url: https://en.wikipedia.org/wiki/Filtration_(mathematics)
---

## Summary

A filtration of a [[module|0NZ8JA25WK]] $M$ is a decreasing sequence of [[submodules|05WDSN597C]] $M = M_0 \supseteq M_1 \supseteq M_2 \supseteq \cdots$.
For an ideal $I$, an $I$-filtration is one with $I M_n \subseteq M_{n+1}$, and it is stable when equality holds from some point on.
The basic example is the $I$-adic filtration $M_n = I^n M$; filtrations lead to the [[associated graded ring|8HFAEGFQT1]], the [[$I$-adic topology|2VF2TSJ3PY]] and the [[Artin–Rees lemma|30H6B0G2FT]].

## Explanations

### L1 human

A filtration sorts the elements of a module by how small they are.
The deeper the submodule $M_n$, the smaller its elements are thought to be.
For the integers with the prime $p$, the submodule $p^n \Z$ contains the integers divisible by $p^n$, and these count as small when $n$ is large.
The [[definition|GEJYZEY7Y0]] makes this precise.
