---
tag: 01E7SWYJX3
kind: statement
role: proposition
name: Normality via left and right cosets
msc: [20A05]
uses: [0W77CVBCHQ, 05FD317V2W, 060Z37VVB6]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Equivalent conditions
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $N$ be a [[subgroup|0X1JXT47GA]] of $G$.
Then $N$ is [[normal|0CB0DX5BVV]] in $G$ if and only if $gN = Ng$ for each $g \in G$.

## Remarks

Here $gN$ is a [[left coset|03DEH43F4H]] and $Ng$ is a [[right coset|0NE1DK7H4T]].
The equation $gN = Ng$ is equivalent to $gNg^{-1} = N$, by multiplying on the right by $g^{-1}$.
The condition does not say that $gn = ng$ for each $n \in N$; it says only that the two sets are equal.

## Explanations

### L1 human

For a normal subgroup, it does not matter if you multiply by $g$ on the left or on the right: you get the same coset.
Thus there is only one kind of coset, and we can just say "the cosets of $N$".
This is what makes the quotient group possible.
