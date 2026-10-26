---
tag: 0SP14DZN0G
kind: definition
name: Primitive polynomial
msc: [13F20]
defines: 0TXNRQZY0H
uses: [08VV7YJRB7]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_part_and_content
    locator: lead section
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]].
A polynomial $f \in R[x]$ is primitive if every $r \in R$ that divides $f$ in $R[x]$ is a unit.
Here $r$ divides $f$ when $r$ divides each coefficient of $f$.

## Remarks

If $R$ is a [[unique factorisation domain|06YMXJMXYS]], then $f$ is primitive if and only if its [[content|08VV7YJRB7]] is a unit.
In $\mathbb{Z}[x]$, $3x^2 + 2x - 1$ is primitive and $6x^2 + 4x - 2$ is not.
Every [[monic polynomial|0BDX4MBKT4]] is primitive.
The word primitive polynomial has another meaning over a finite field: a polynomial whose root is a [[primitive element|0YAA9CJQXF]].

## Explanations

### L1 human

A primitive polynomial has coefficients with no common factor.
Over the integers, this means that the gcd of the coefficients is $1$.
