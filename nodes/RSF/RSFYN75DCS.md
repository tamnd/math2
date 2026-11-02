---
tag: RSFYN75DCS
kind: concept
name: Eilenberg swindle
msc: [16D40, "16E20", 19A13]
sources:
  - url: https://en.wikipedia.org/wiki/Eilenberg%E2%80%93Mazur_swindle
same_as:
  wikidata: Q5349491
  wikipedia: Eilenberg–Mazur swindle
---

## Summary

The Eilenberg swindle is an argument with infinite direct sums that cancels an object by regrouping an infinite sum.
Its basic form shows that every [[projective module|BFFA03GE3V]] $P$ becomes free after adding a large enough [[free module|0DZ9DKAKZR]]: $P \oplus F \cong F$ for some free $F$.
It explains why the Grothendieck group is built only from finitely generated modules: with infinite sums allowed, every class would be zero.
The same trick, used by Mazur in topology, shows that no nontrivial knot has an inverse under connected sum.

## Explanations

### L1 human

The swindle is the old joke $1 = 1 + (-1 + 1) + (-1 + 1) + \cdots = (1 - 1) + (1 - 1) + \cdots = 0$, made correct.
With numbers the regrouping is not allowed, but with infinite direct sums of modules it is.
If $P \oplus Q$ is free, then adding infinitely many copies of $P \oplus Q$ to $P$ gives the same as infinitely many copies of $Q \oplus P$.
So $P$ disappears into an infinite free module.
