---
tag: 0T8M3YC5RG
kind: statement
role: theorem
name: Existence of finite fields of every prime power order
msc: ["12E20"]
uses: [01441KDGBY, 0AD4VS02H3, 067F8YVYMH, 08RTDHX1SK]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Existence and uniqueness
---

## Statement

Let $p$ be a prime number and let $n \ge 1$.
Then there is a [[finite field|08RTDHX1SK]] of order $q = p^n$.

## Remarks

The proof: let $L$ be a [[splitting field|01441KDGBY]] of $f = x^q - x$ over $\mathbb{F}_p$. The [[derivative|0AD4VS02H3]] $f' = q x^{q-1} - 1 = -1$ has no common root with $f$, so $f$ has $q$ distinct roots in $L$, by the [[criterion for repeated roots|067F8YVYMH]].
The roots of $f$ form a subfield of $L$, because $(a + b)^q = a^q + b^q$ and $(a b)^q = a^q b^q$. This subfield has $q$ elements.
So for each $n$ there is an irreducible polynomial of degree $n$ over $\mathbb{F}_p$.

## History

E. H. Moore first proved the classification of finite fields in 1893: there is a field of each prime power order, and all fields of a given order are isomorphic.

## Explanations

### L1 human

The field with $p^n$ elements is made of the roots of $x^{p^n} - x$.
The proof checks that these roots are distinct and closed under the field operations.
