---
tag: 5WKBCMW1BC
kind: concept
name: Faddeev–Popov ghost
msc: [81T13, 81T70]
sources:
  - url: https://en.wikipedia.org/wiki/Faddeev%E2%80%93Popov_ghost
same_as:
  wikidata: Q1391812
  wikipedia: Faddeev–Popov ghost
---

## Summary

Faddeev–Popov ghosts are auxiliary anticommuting fields introduced in the [[path integral|1NYTFT5NPE]] of a gauge theory.
[[Gauge fixing|TXD7MTYQYS]] picks one field configuration from each gauge orbit, and it brings in a Jacobian determinant, the Faddeev–Popov determinant.
Writing this determinant as a [[Berezin integral|CYWSMK47CN]] over a ghost field $c$ and an antighost field $\bar c$ turns it into a term of the action.
Ghosts have no physical states of their own, but non-abelian gauge theories need them for correct results.
They are the starting point of [[BRST quantization|DCHKJBKCMR]].

## Explanations

### L1 human

In a gauge theory many field configurations describe the same physical situation, and the path integral counts each situation infinitely often.
To fix this one chooses one representative per class, for instance by requiring a condition such as $\partial^\mu A_\mu = 0$.
The change of variables that does this produces a determinant, much as polar coordinates produce a factor $r$.
A determinant can be written as a Gaussian integral over anticommuting variables, and these variables are the ghosts.
They behave like particles with the wrong relation between spin and statistics, which is why they are called ghosts.
