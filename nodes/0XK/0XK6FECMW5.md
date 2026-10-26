---
tag: 0XK6FECMW5
kind: statement
role: theorem
name: Decomposition of a permutation into transpositions
msc: [20B30]
uses: [02DTRYKGE8, 0YWDAZPRPQ]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_group
    locator: Transpositions, sign, and the alternating group
  - url: https://en.wikipedia.org/wiki/Cyclic_permutation
    locator: Properties
---

## Statement

Let $n \geq 2$.
Each permutation in $S_n$ is a product of [[transpositions|0FWVRHBRWM]].

## Remarks

A $k$-cycle is a product of $k - 1$ transpositions, for example $(a_1\ a_2\ \dots\ a_k) = (a_1\ a_k)(a_1\ a_{k-1}) \cdots (a_1\ a_2)$.
With the [[disjoint cycle decomposition|0YWDAZPRPQ]], this gives the result, and the identity is $(1\ 2)(1\ 2)$.
The decomposition is not unique, but the parity of the number of factors is unique.

## Explanations

### L1 human

You can sort any arrangement of objects by swapping two objects at a time.
So each permutation is a chain of swaps.
Different chains can give the same permutation, but they are all of even length or all of odd length.
