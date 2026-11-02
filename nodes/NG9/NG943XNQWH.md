---
tag: NG943XNQWH
kind: concept
name: Heyting algebra
msc: ["06D20", "03G10", "03B20"]
specializes: [0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/Heyting_algebra
same_as:
  wikidata: Q1617044
  wikipedia: Heyting algebra
---

## Summary

A Heyting algebra is a bounded lattice with an implication operation $a \to b$, the largest element whose meet with $a$ lies below $b$.
Every Heyting algebra is a [[distributive lattice|0HM0HQCK6N]], and every [[Boolean algebra|0XADJKM699]] is a Heyting algebra.
Heyting algebras are the algebraic models of [[intuitionistic logic|Q11N8X99FK]], in the same way that Boolean algebras are the models of classical logic.
The open sets of any topological space form a Heyting algebra.

## Explanations

### L1 human

In a Heyting algebra one can form "and", "or" and "implies", but "not $a$" need not satisfy "$a$ or not $a$".
The main picture is the family of open sets of the plane or the line.
"And" is intersection, "or" is union, and "not $U$" is the interior of the complement of $U$.
On the real line, the open set $U = \R \setminus \set{0}$ has "not $U$" equal to the empty set, so "$U$ or not $U$" is $\R \setminus \set{0}$, not the whole line.
This failure of the law of excluded middle is exactly what intuitionistic logic allows.
