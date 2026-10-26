---
tag: 0H5WWC8RZX
kind: statement
role: theorem
name: The order of a finite field is a prime power
msc: ["12E20"]
uses: [08RTDHX1SK, 00758QM6JJ, 0VPFBAY7MW, 0GS74FGFEK]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Properties
---

## Statement

Let $F$ be a [[finite field|08RTDHX1SK]].
Then the [[characteristic|0P7CH1CND5]] of $F$ is a prime number $p$, and $|F| = p^n$ with $n = [F : \mathbb{F}_p]$.

## Remarks

The proof: a finite field has nonzero characteristic, and [[the characteristic of a domain is $0$ or prime|00758QM6JJ]]. The [[prime subfield|0VPFBAY7MW]] is $\mathbb{F}_p$, and $F$ is a vector space of dimension $n$ over it, so it has $p^n$ elements.
So there is no field with $6$ or $10$ elements.
The converse, that a field of order $p^n$ exists for each $n \ge 1$, is the [[existence theorem|0T8M3YC5RG]].

## Explanations

### L1 human

A finite field is a vector space over the field with $p$ elements.
A vector space of dimension $n$ over it has $p^n$ elements.
So the size of a finite field is always a power of a prime.
