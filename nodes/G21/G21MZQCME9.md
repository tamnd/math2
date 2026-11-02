---
tag: G21MZQCME9
kind: concept
name: Crossed product algebra
msc: [16S35, 16K50]
specializes: [5HRKJBAY2V]
sources:
  - url: https://en.wikipedia.org/wiki/Crossed_product
---

## Summary

A crossed product algebra is a central simple algebra built from a finite [[Galois extension|0QMZAQ6QQ4]] $L/K$.
The extra datum is a $2$-cocycle of its [[Galois group|0XTY86BZKY]] with values in $L^\times$.
It contains $L$ as a maximal subfield, and each Galois automorphism is realized as conjugation by an invertible element.
Every central simple algebra is Brauer equivalent to a crossed product, which gives the isomorphism between the [[Brauer group|BEW48TA9WZ]] and a second [[Galois cohomology|9MPCZ3EAJM]] group.
This algebraic notion is distinct from the [[crossed product|8HG8TS46A6]] of operator algebras, although both twist a ring by a group action.

## Explanations

### L1 human

Start with a Galois extension $L$ of $K$ and its group of symmetries $G$.
Add to $L$ one new symbol $u_\sigma$ for each symmetry $\sigma$, and declare that moving a number past $u_\sigma$ applies $\sigma$ to it.
The products $u_\sigma u_\tau$ are allowed to differ from $u_{\sigma\tau}$ by a nonzero number of $L$, chosen by a rule called a factor set.
For $L = \C$ over $K = \R$ and the right choice of factor set, the result is Hamilton's quaternions, with $u_\sigma = j$.
