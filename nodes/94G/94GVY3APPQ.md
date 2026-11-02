---
tag: 94GVY3APPQ
kind: concept
name: Quasi-identity
msc: ["08C15", "03C52"]
sources:
  - url: https://en.wikipedia.org/wiki/Quasivariety
---

## Summary

A quasi-identity is a law of the form "if these finitely many equations between terms hold, then this further equation holds".
It is required for all values of the variables.
It generalizes an [[identity|PKD440G2XW]], which is the case with no hypotheses.
Quasi-identities are exactly the axioms of [[quasivarieties|WRXEKT4NQS]], just as identities are the axioms of varieties.
They are the strict universal [[Horn clauses|QR92EZDTKF]] of an algebraic language.

## Explanations

### L1 human

An identity such as $x \cdot y = y \cdot x$ must hold for every choice of $x$ and $y$.
A quasi-identity only demands its conclusion when some equations already hold, like a conditional rule.
The cancellation law "if $x z = y z$ then $x = y$" is a typical example.
It holds in every group, since one can multiply by $z^{-1}$ on the right.
It fails in the integers under multiplication, because $1 \cdot 0 = 2 \cdot 0$ while $1 \ne 2$.
