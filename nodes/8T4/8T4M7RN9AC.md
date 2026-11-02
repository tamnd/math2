---
tag: 8T4M7RN9AC
kind: concept
name: MV-algebra
msc: ["06D35", "03G20", "03B50"]
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
same_as:
  wikidata: Q6719122
  wikipedia: MV-algebra
---

## Summary

An MV-algebra is an algebraic structure with a truncated addition $\oplus$, a negation $\neg$ and a constant $0$.
It is modelled on the unit interval $[0, 1]$ with $x \oplus y = \min(1, x + y)$ and $\neg x = 1 - x$.
Chen Chung Chang introduced MV-algebras in 1958 to give an algebraic proof of the completeness of Łukasiewicz infinite-valued logic, a [[many-valued logic|DWYCKAKXZD]].
Every [[Boolean algebra|0XADJKM699]] is an MV-algebra, and MV-algebras play for Łukasiewicz logic the role that Boolean algebras play for classical logic.
Daniele Mundici showed that MV-algebras correspond to lattice-ordered abelian groups with a strong unit.

## Explanations

### L1 human

In Łukasiewicz logic a statement can be partly true, with a truth value anywhere between $0$ (false) and $1$ (true).
"Not $x$" has truth value $1 - x$, and a kind of "or" adds the truth values but stops at $1$.
For example, $0.3 \oplus 0.5 = 0.8$, while $0.7 \oplus 0.5 = 1$.
An MV-algebra is any structure that obeys the same equations as these operations on $[0, 1]$.
