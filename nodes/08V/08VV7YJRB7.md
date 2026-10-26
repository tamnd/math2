---
tag: 08VV7YJRB7
kind: definition
name: Content of a polynomial
msc: [13F20]
defines: 0R2X8K9QA7
uses: [06YMXJMXYS, 0F7KNJ1ZYN]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_part_and_content
    locator: lead section
---

## Definition

Let $R$ be a [[unique factorisation domain|06YMXJMXYS]] and let $f = a_0 + a_1 x + \dots + a_n x^n \in R[x]$.
The content of $f$, written $c(f)$, is a [[greatest common divisor|0F7KNJ1ZYN]] of the coefficients $a_0, a_1, \dots, a_n$.

## Remarks

The content is unique up to associates. Over $\mathbb{Z}$, one often takes the positive gcd, with the sign of the leading coefficient in the primitive part.
For $f = 6x^2 + 4x - 2$ in $\mathbb{Z}[x]$, $c(f) = 2$.
Each nonzero $f$ is $c(f) \cdot g$ with $g$ a [[primitive polynomial|0SP14DZN0G]], the primitive part of $f$.
The content is multiplicative up to units: $c(f g) \sim c(f) c(g)$. This is a form of [[Gauss's lemma|0QFV5Y1Z5X]].

## Explanations

### L1 human

The content is the largest common factor that you can pull out of all the coefficients.
For $6x^2 + 4x - 2$, you can pull out $2$ and get $2(3x^2 + 2x - 1)$.
