---
tag: DSF8C6QPAG
kind: conjecture
name: Kaplansky's conjectures
msc: [16S34, 16U60, 16U40]
uses: [4NMTSX0XDS, PEMNN32A43, 0NNRDW10RZ, 0N5NJZKKN3, 0XVEZDE9J8, E1NE8V7EX8]
about: [4NMTSX0XDS]
sources:
  - url: https://en.wikipedia.org/wiki/Kaplansky%27s_conjectures
    locator: Group rings
same_as:
  wikidata: Q6366842
  wikipedia: Kaplansky's conjectures
history:
  posed_by: "Irving Kaplansky"
---

## Statement

Let $K$ be a field and let $G$ be a [[torsion-free group|PEMNN32A43]].
That is, every element of $G$ other than the identity has infinite order.
Let $K[G]$ be the [[group ring|4NMTSX0XDS]] of $G$ over $K$.

1. (Zero divisor conjecture) $K[G]$ has no [[zero divisors|0NNRDW10RZ]] other than $0$; see [[Kaplansky's zero divisor conjecture|E1NE8V7EX8]].
2. (Idempotent conjecture) The only [[idempotents|0N5NJZKKN3]] of $K[G]$ are $0$ and $1$.
3. (Unit conjecture) Every [[unit|0XVEZDE9J8]] of $K[G]$ has the form $c g$ with $c \in K$ nonzero and $g \in G$.

## Remarks

The conjectures are linked: the unit conjecture implies the zero divisor conjecture, and the zero divisor conjecture implies the idempotent conjecture, since an idempotent $e$ satisfies $e(1 - e) = 0$.
The hypothesis that $G$ is torsion-free is needed: if $g \ne 1$ has finite order $n$, then $(1 - g)(1 + g + \cdots + g^{n-1}) = 1 - g^n = 0$.
The unit conjecture goes back to the 1940 thesis of Graham Higman.
In 2021 Giles Gardam disproved the unit conjecture over the field with two elements, with a nontrivial unit in the group ring of the fundamental group of the Hantzsche–Wendt manifold.
All three conjectures hold for groups with the unique product property, and the zero divisor conjecture holds for torsion-free elementary amenable groups.
The zero divisor and idempotent conjectures are open in general.
Kaplansky also made conjectures in other fields, on Banach algebras and on quadratic forms; they are separate questions.

## Explanations

### L1 human

The group ring of a group mixes the group with a field, and elements of finite order in the group always create zero divisors and idempotents in it.
Kaplansky asked whether these are the only sources: if the group has no elements of finite order, is the group ring as well behaved as a ring of polynomials?
Three precise forms of the question concern zero divisors, idempotents and units.
The one about units turned out to be false, and the other two are still open.
