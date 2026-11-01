---
tag: MR9QCH1PNA
kind: concept
name: Projective dimension
msc: [13D05, 18G20]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_module
---

## Summary

The projective dimension of a module $M$ is the length of a shortest [[projective resolution|HK2AA1YSQ2]] of $M$.
It is $0$ exactly for the nonzero [[projective modules|BFFA03GE3V]], so it measures how far $M$ is from being projective.
Over a Noetherian local ring it is linked to the [[depth|M2RADBFW99]] by the [[Auslander–Buchsbaum formula|SQB74J5E8Q]].

## Explanations

### L1 human

Some modules are free or projective; they need no relations at all.
Others need relations, then relations among relations, and so on.
The projective dimension counts how many steps this takes in the best case, or is infinite if it never stops.
Over $\Z$, the module $\Z/6\Z$ has projective dimension $1$: one relation, $6 = 0$, and nothing more.
