---
tag: N5NTPAR2KT
kind: example
name: The cosets of a subgroup that is not normal do not form a group
msc: [20B30]
not_instance_of:
  - target: 0KYX2N69J0
    note: the product of cosets depends on the choice of representatives
uses: [0515A6D2Y1, 05FD317V2W, 0YYWCNTPWR, 0W77CVBCHQ]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Definition
---

## Example

In the [[symmetric group|0515A6D2Y1]] $S_3$, let $H = \{e, (1\,2)\}$. Compose permutations from right to left.
Two of the [[left cosets|05FD317V2W]] are $(1\,3)H = \{(1\,3), (1\,2\,3)\}$ and $(2\,3)H = \{(2\,3), (1\,3\,2)\}$.
Try to set $(aH)(bH) = (ab)H$. With $a = (1\,3)$ and $b = (2\,3)$, we get $ab = (1\,3\,2)$, which is in $(2\,3)H$.
With $a = (1\,2\,3)$ from the same coset, we get $ab = (1\,2)$, which is in $H$.
The two results are in different cosets. Thus this product is not defined, and the cosets of $H$ do not form a [[quotient group|0YYWCNTPWR]].

## Remarks

$H$ is not [[normal|0W77CVBCHQ]] in $S_3$. For a normal subgroup the product of cosets is always defined.
