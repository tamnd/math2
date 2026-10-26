---
tag: 010PKCQPXP
kind: statement
role: theorem
name: Uniqueness of finite fields of a given order
msc: ["12E20"]
uses: [0CDAHW576M, 069A3BC3EP]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Existence and uniqueness
---

## Statement

Let $F$ and $F'$ be [[finite fields|08RTDHX1SK]] with $|F| = |F'|$.
Then $F$ and $F'$ are isomorphic.

## Remarks

The proof: let $q = |F|$. Both fields have characteristic $p$ and prime subfield $\mathbb{F}_p$. Both are [[splitting fields of $x^q - x$ over $\mathbb{F}_p$|0CDAHW576M]], so they are isomorphic by the [[uniqueness of splitting fields|069A3BC3EP]].
Also, a field contains at most one subfield of order $q$: its elements must be the $q$ roots of $x^q - x$.

## History

E. H. Moore first proved the classification of finite fields in 1893.

## Explanations

### L1 human

Two finite fields with the same number of elements have the same structure.
Only the names of the elements can differ.
