---
tag: 0NP5N5PYW5
kind: example
name: Cantor pairing function
aliases: [cantor-pairing]
msc: ["03E10"]
instance_of: [0GG9TVW90M]
uses: [0SNQEF7Z53, 0C81YBVTWH]
sources:
  - url: https://en.wikipedia.org/wiki/Pairing_function
    locator: Cantor pairing function
same_as:
  wikidata: Q1033906
  wikipedia: Pairing function
---

## Example

The Cantor pairing function is the function $\pi \colon \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ with
$$\pi(x, y) = \frac{(x + y)(x + y + 1)}{2} + y.$$
It is a [[bijection|0SNQEF7Z53]].
It lists the pairs along the diagonals $x + y = 0, 1, 2, \dots$: $\pi(0, 0) = 0$, $\pi(1, 0) = 1$, $\pi(0, 1) = 2$, $\pi(2, 0) = 3$.

## Remarks

So $\mathbb{N} \times \mathbb{N}$ is [[countably infinite|0SEZ3JGZP7]]. See [[product of countable sets is countable|08G4XH86JC]].
The value $(x + y)(x + y + 1)/2$ is the number of pairs on the earlier diagonals, and $y$ is the position on the diagonal.

## Explanations

### L1 human

Write the pairs $(x, y)$ in an infinite grid.
Walk through the grid along the short diagonals, one after the other, and number the pairs as you go.
Each pair gets exactly one number, and each number gets exactly one pair.
