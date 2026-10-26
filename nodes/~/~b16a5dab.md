---
tag: ~b16a5dab
kind: definition
name: Monic polynomial
msc: [13F20]
defines: ~b75b51a2
uses: [~d7b17e0d]
sources:
  - url: https://en.wikipedia.org/wiki/Monic_polynomial
    locator: lead section
---

## Definition

Let $R$ be a [[ring|~447242bf]].
A polynomial $f \in R[x]$ is monic if its [[leading coefficient|~d7b17e0d]] is $1$.

## Remarks

The polynomial $x^2 - 2$ is monic, and $2x^2 - 1$ is not.
In a nonzero ring, a monic polynomial is not zero.
The product of two monic polynomials is monic, over every commutative ring.
Over a field, each nonzero polynomial is a constant times exactly one monic polynomial.

## Explanations

### L1 human

A monic polynomial starts with $x^d$, with no number in front.
Over a field, you can make any nonzero polynomial monic by dividing by its leading coefficient.
