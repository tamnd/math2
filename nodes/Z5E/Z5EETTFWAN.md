---
tag: Z5EETTFWAN
kind: concept
name: Duality in category theory
msc: [18A05]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_(category_theory)
same_as:
  wikidata: Q2361385
  wikipedia: Dual (category theory)
---

## Summary

Duality in category theory is the correspondence between a statement about a [[category|A2DE66937D]] and the statement obtained by reversing all arrows.
A statement holds in the [[opposite category|DAMK8XE1FR]] $\mathcal{C}^{\mathrm{op}}$ exactly when its dual holds in $\mathcal{C}$.
So a theorem proved for all categories gives, for free, its dual theorem.
Pairs of dual notions include [[monomorphism|Y2NP1JFR86]] and [[epimorphism|RVXDSY04KG]], [[initial and terminal objects|EK85VSSRMR]], [[product|S5744QZV4N]] and [[coproduct|4FJ0S71P58]], and [[limit|CHS5AFJGWE]] and [[colimit|BJS1CGTKQ5]].

## Explanations

### L1 human

Many notions in category theory come in pairs that are mirror images of each other.
To pass from one to the other, turn every arrow around and read every composite in the opposite order.
For example, "every arrow out of $X$ is unique" becomes "every arrow into $X$ is unique".
The first describes an initial object, such as the empty set among sets; the second describes a terminal object, such as a one-point set.
Each proof about one notion turns into a proof about its mirror image, so each theorem comes with a second, dual theorem at no extra cost.
