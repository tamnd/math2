---
tag: 3J89REV9WQ
kind: concept
name: Derivation
msc: [13N15, 12H05, 16W25]
sources:
  - url: https://en.wikipedia.org/wiki/Derivation_(differential_algebra)
same_as:
  wikidata: Q451323
  wikipedia: Derivation (differential algebra)
---

## Summary

A derivation is a linear map on an algebra that satisfies the product rule $D(ab) = D(a) b + a D(b)$, see the [[definition|R1F0HCCE6F]].
It is the algebraic form of the [[derivative|0V1EJCT8G6]], and it makes sense without limits.
Derivations are basic in [[differential algebra|GA5PTQGC6G]], algebraic geometry and Lie theory.
The derivations of a Lie algebra obey the same rule for the Lie bracket.
The commutator of two derivations is again a derivation, so the derivations of an algebra form a Lie algebra.

## Explanations

### L1 human

The derivative of a product obeys the product rule: $(fg)' = f'g + fg'$.
A derivation is any map that adds up linearly and obeys this rule.
For polynomials, $d/dX$ is a derivation: it sends $X^3$ to $3X^2$ without using limits.
Another example on polynomials in $X$ and $Y$ is $X \, \partial/\partial Y$, which sends $Y^2$ to $2XY$.
