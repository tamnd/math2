---
tag: EPAAKD80H9
kind: concept
name: Homotopy type theory
msc: ["03B38", "55U35", "03F55"]
uses: [ESVYD9CZ8C, Q48KGV33AH]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_type_theory
same_as:
  wikidata: Q5891840
  wikipedia: Homotopy type theory
---

## Summary

Homotopy type theory reads [[intuitionistic type theory|ESVYD9CZ8C]] in terms of homotopy theory: types are spaces, terms are points, and terms of identity types are paths.
It adds Voevodsky's univalence axiom, which says that equivalent types are equal, and higher inductive types such as the circle.
These additions give a new foundation of mathematics, called univalent foundations.
The book "Homotopy Type Theory: Univalent Foundations of Mathematics", written in 2013 at the Institute for Advanced Study, set out the theory.

## Explanations

### L1 human

In ordinary [[type theory|Q48KGV33AH]], a proof that $a = b$ is just a certificate.
In homotopy type theory, it is a path from $a$ to $b$ in a space, and two such paths need not be the same.
A proof that two proofs of $a = b$ are equal is then a deformation of one path into the other.
The univalence axiom says that two types with a one-to-one correspondence between them are equal, so isomorphic structures can always be swapped.
This matches how mathematicians already treat isomorphic objects.
