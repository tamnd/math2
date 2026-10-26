---
tag: 0YJ3WRR9RY
kind: example
name: Integers modulo n as a quotient group
msc: [20K01]
instance_of: [0KYX2N69J0]
uses: [0YYWCNTPWR, 0BSCJA5G53, 0SRATCFF1W]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Integer modular arithmetic
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Remainders of integer division
---

## Example

Let $n$ be a positive integer.
The subgroup $n\mathbb{Z}$ of the [[additive group of integers|0BSCJA5G53]] is normal, because $\mathbb{Z}$ is abelian.
The [[quotient group|0KYX2N69J0]] $\mathbb{Z}/n\mathbb{Z}$ has the $n$ cosets $0 + n\mathbb{Z}, 1 + n\mathbb{Z}, \ldots, (n-1) + n\mathbb{Z}$.
The operation is $(a + n\mathbb{Z}) + (b + n\mathbb{Z}) = (a + b) + n\mathbb{Z}$, which is addition modulo $n$.

## Remarks

The coset $a + n\mathbb{Z}$ is the set of integers with the same remainder as $a$ on division by $n$.
Thus $\mathbb{Z}/n\mathbb{Z}$ is the cyclic group of order $n$ of clock arithmetic.
For $n = 0$, the quotient $\mathbb{Z}/0\mathbb{Z}$ is isomorphic to $\mathbb{Z}$.

## Explanations

### L1 human

Two integers are in the same coset of $n\mathbb{Z}$ when their difference is a multiple of $n$.
So the quotient group keeps only the remainder modulo $n$.
Adding cosets is the same as adding remainders and reducing modulo $n$.
