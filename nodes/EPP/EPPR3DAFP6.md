---
tag: EPPR3DAFP6
kind: concept
name: Noncommutative Gröbner basis
msc: [16Z10, 16S15]
sources:
  - url: https://en.wikipedia.org/wiki/Gr%C3%B6bner_basis
---

## Summary

A noncommutative Gröbner basis, or Gröbner–Shirshov basis, generates a two-sided ideal of a [[free algebra|2P3Y2FRCSZ]] $k\langle X \rangle$.
Its leading words control the leading words of all elements of the ideal.
It extends the commutative [[Gröbner basis|C83KPT47R0]] from polynomial rings to free algebras, with words in place of monomials.
The words that avoid all leading words give a linear basis of the quotient algebra.
So a Gröbner basis solves the normal form problem for an algebra given by generators and relations.
Unlike the commutative case, a finitely generated ideal may have no finite Gröbner basis, and the completion procedure need not terminate.

## Explanations

### L1 human

An algebra given by generators and relations, such as $yx = xy$, raises the question of when two expressions are equal.
The idea is to orient each relation as a rewriting rule from a larger word to a smaller one, such as $yx \to xy$.
If the rules are complete, every expression rewrites to a unique normal form, and two expressions are equal exactly when their normal forms agree.
A Gröbner basis is such a complete set of rules.
With the single rule $yx \to xy$ the normal forms are the words $x^a y^b$, which recovers the polynomial ring $k[x, y]$.
