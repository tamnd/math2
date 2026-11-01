---
tag: 9FB0AZSEGM
kind: concept
name: Drazin inverse
msc: [15A09]
sources:
  - url: https://en.wikipedia.org/wiki/Drazin_inverse
same_as:
  wikidata: Q4521948
  wikipedia: Drazin inverse
---

## Summary

The Drazin inverse of a square matrix $A$ is a matrix $X$ that commutes with $A$ and satisfies $XAX = X$ and $A^{k+1}X = A^k$ for some $k$.
It exists and is unique for every square matrix over a field.
It inverts $A$ on the part of the space where $A$ acts invertibly, and it is $0$ on the rest.

## Explanations

### L1 human

A square matrix splits the space into two pieces that it keeps: one where it acts invertibly and one where some power of it is zero.
The Drazin inverse inverts the matrix on the first piece and is zero on the second.
For example, for $A = \operatorname{diag}(2, 0)$, the Drazin inverse is $\operatorname{diag}(1/2, 0)$.
Unlike the [[generalized inverse|FPHNJ5AAYF]], it is defined through powers of $A$, so it fits well with polynomials in $A$.
