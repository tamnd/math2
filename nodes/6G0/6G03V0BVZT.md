---
tag: 6G03V0BVZT
kind: concept
name: Co-Heyting algebra
msc: ["06D20", "03G10"]
specializes: [0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/Heyting_algebra
---

## Summary

A co-Heyting algebra is a bounded lattice with a difference operation $a \setminus b$, the least element $c$ such that $a \le b \vee c$.
It is the order dual of a [[Heyting algebra|NG943XNQWH]]: turning a co-Heyting algebra upside down gives a Heyting algebra, and conversely.
Every co-Heyting algebra is a [[distributive lattice|0HM0HQCK6N]].
The closed sets of a topological space form a co-Heyting algebra, and co-Heyting algebras serve as algebraic models of paraconsistent logics.

## Explanations

### L1 human

In a Heyting algebra one asks for the largest element that, together with $a$, stays below $b$.
In a co-Heyting algebra one asks instead for the smallest piece $c$ that one must add to $b$ in order to cover $a$.
The picture is the family of closed sets of the plane, where $A \setminus B$ is the closure of the ordinary set difference.
For example, on the real line, if $A = [0, 2]$ and $B = [1, 2]$, then the difference is $[0, 1]$, not $[0, 1)$, since it must be closed.
