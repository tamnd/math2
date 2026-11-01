---
tag: C31PYYPRGC
kind: concept
name: Faithfully flat module
msc: [13C11, 13B40]
specializes: [73RYYEVDKA]
sources:
  - url: https://en.wikipedia.org/wiki/Flat_module
---

## Summary

A faithfully flat module is a [[flat module|73RYYEVDKA]] $M$ such that tensoring with $M$ kills no nonzero module.
Then a sequence of modules is exact if and only if it stays exact after tensoring with $M$.
A ring map $R \to S$ is faithfully flat when $S$ is faithfully flat as an $R$-module; such maps are the setting of faithfully flat descent.
Examples are nonzero free modules, polynomial rings $R[x]$ over $R$, and the completion of a Noetherian local ring.

## Explanations

### L1 human

A flat module never destroys injectivity, but it can still make a whole module vanish.
For example, $\Q$ is flat over $\Z$, yet $\Z/2\Z \otimes_\Z \Q = 0$.
A faithfully flat module never does this: it reflects all the information.
So a statement can be checked after a faithfully flat change of rings, where it may be easier to prove.
