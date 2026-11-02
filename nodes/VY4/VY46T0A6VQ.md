---
tag: VY46T0A6VQ
kind: concept
name: Boolean algebras canonically defined
msc: ["06E05", "03G05", "08B05"]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_algebras_canonically_defined
same_as:
  wikidata: Q4943350
  wikipedia: Boolean algebras canonically defined
---

## Summary

The canonical definition of a [[Boolean algebra|0XADJKM699]] avoids choosing a list of axioms.
It uses the operations of the [[two-element Boolean algebra|0WG43AC0EV]].
A Boolean algebra is then any algebra with these operations that satisfies every equation true in the two-element algebra.
This gives the same class of structures as the usual axioms.
It also explains why many different lists of axioms work.
A list of equations true in $\set{0, 1}$ is a complete axiom system exactly when it proves every equation true in $\set{0, 1}$.
It also connects Boolean algebra with truth tables and with the equational logic of universal algebra.

## Explanations

### L1 human

An equation such as $x \wedge (y \vee z) = (x \wedge y) \vee (x \wedge z)$ can be tested on true and false by a truth table.
The canonical view takes all equations that pass this test as the laws of Boolean algebra.
A Boolean algebra is then any set with "and", "or", "not", $0$ and $1$ that obeys all these laws.
The power set of a set is an example, because each law can be checked one point at a time.
