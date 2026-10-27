---
tag: 6VFF2TTXYZ
kind: example
name: The left cosets of a subgroup of order two in S3
msc: [20B30]
instance_of: [03DEH43F4H]
illustrates: [3C53TD]
uses: [0515A6D2Y1, 05FD317V2W]
sources:
  - url: https://en.wikipedia.org/wiki/Coset
    locator: First example
---

## Example

In the [[symmetric group|0515A6D2Y1]] $S_3$, let $H = \{e, (1\,2)\}$. Compose permutations from right to left.
The [[left cosets|05FD317V2W]] of $H$ are $eH = \{e, (1\,2)\}$, $(1\,3)H = \{(1\,3), (1\,2\,3)\}$ and $(2\,3)H = \{(2\,3), (1\,3\,2)\}$.
Each of the $6$ elements of $S_3$ is in exactly one of these cosets.
Each coset has $2$ elements. Thus $6 = 3 \cdot 2$, as [[Lagrange's theorem|3C53TD]] states.

## Remarks

The right cosets of $H$ are different sets, because $H$ is not normal in $S_3$.
