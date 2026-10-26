---
tag: ~f1ef1bde
kind: statement
role: theorem
name: Remainder theorem
aliases: [polynomial-remainder-theorem]
msc: [13F20]
uses: [~0ad30747, ~4f7f20ad]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_remainder_theorem
    locator: lead section
same_as:
  wikidata: Q1071948
  wikipedia: Polynomial remainder theorem
---

## Statement

Let $R$ be a [[commutative ring|~79bc52c4]], let $f \in R[x]$ and let $c \in R$.
Then the remainder of the [[division|~0ad30747]] of $f$ by $x - c$ is the constant polynomial $f(c)$.
That is, there is $q \in R[x]$ with $f = (x - c) q + f(c)$.

## Remarks

The proof: division by the monic polynomial $x - c$ gives $f = (x - c) q + r$ with $r$ a constant. [[Evaluation|~4f7f20ad]] at $c$ gives $r = f(c)$.
For example, the remainder of $x^3 - 2x + 5$ divided by $x - 2$ is $2^3 - 4 + 5 = 9$.

## Explanations

### L1 human

You do not need long division to find the remainder of $f$ divided by $x - c$.
You only compute $f(c)$.
