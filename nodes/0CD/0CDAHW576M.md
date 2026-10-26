---
tag: 0CDAHW576M
kind: statement
role: theorem
name: A finite field of order q is the splitting field of x^q - x
msc: ["12E20"]
uses: [0QWR8WTZEW, 02NZZ1J0FH, 0H5WWC8RZX]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Existence and uniqueness
---

## Statement

Let $F$ be a [[finite field|08RTDHX1SK]] of order $q = p^n$, with $p$ prime.
Then $F$ is a [[splitting field|02NZZ1J0FH]] of $x^q - x$ over its prime subfield $\mathbb{F}_p$.

## Remarks

The proof: [[$x^q - x = \prod_{a \in F} (x - a)$|0QWR8WTZEW]], so $x^q - x$ splits over $F$, and its roots are all the elements of $F$. So the roots generate $F$.
With the [[uniqueness of splitting fields|069A3BC3EP]], this gives the [[uniqueness of finite fields|010PKCQPXP]].

## Explanations

### L1 human

A finite field consists exactly of the roots of $x^q - x$.
So it is the smallest field that contains all these roots.
