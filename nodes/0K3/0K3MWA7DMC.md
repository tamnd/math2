---
tag: 0K3MWA7DMC
kind: statement
role: theorem
name: Factor theorem
msc: [13F20]
uses: [0TEDQH56RW, 00EHX6FWC0]
sources:
  - url: https://en.wikipedia.org/wiki/Factor_theorem
    locator: lead section
same_as:
  wikidata: Q1108687
  wikipedia: Factor theorem
---

## Statement

Let $R$ be a [[commutative ring|0GYGHKX834]], let $f \in R[x]$ and let $c \in R$.
Then $x - c$ divides $f$ in $R[x]$ if and only if $c$ is a [[root|00EHX6FWC0]] of $f$.

## Remarks

The proof uses the [[remainder theorem|0TEDQH56RW]]: $f = (x - c) q + f(c)$. So $x - c$ divides $f$ exactly when $f(c) = 0$.
For example, $1$ is a root of $x^3 - 1$, and $x^3 - 1 = (x - 1)(x^2 + x + 1)$.
The theorem gives the bound on the [[number of roots|0KJVQV3E0F]] of a polynomial over a field.

## Explanations

### L1 human

Each root gives a linear factor.
If $f(c) = 0$, then you can write $f$ as $(x - c)$ times another polynomial.
Conversely, a factor $x - c$ makes $f(c) = 0$.
