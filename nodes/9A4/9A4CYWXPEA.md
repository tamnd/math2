---
tag: 9A4CYWXPEA
kind: concept
name: Universal Horn class
msc: ["03C52", "08C15"]
specializes: [ZSTEZ3PRT9]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_clause
---

## Summary

A universal Horn class is the class of all structures of a signature that satisfy a given set of universal Horn sentences.
Such a sentence is a universally quantified [[Horn clause|QR92EZDTKF]] built from first-order atomic formulas.
Universal Horn classes are [[universal classes|ZSTEZ3PRT9]], and in addition they are closed under direct products of nonempty families.
In an algebraic signature, the classes axiomatized by universal Horn sentences with a positive literal are exactly the [[quasivarieties|WRXEKT4NQS]].

## Explanations

### L1 human

A universal Horn sentence says: for all elements, if these basic facts hold, then that basic fact holds too, or else that these facts never hold together.
Partial orders form a universal Horn class: reflexivity, antisymmetry and transitivity all have this shape.
Total orders do not, because "$x \le y$ or $y \le x$" offers a choice between two facts.
Indeed the product of two 2-element chains is a square, in which two corners are incomparable.
