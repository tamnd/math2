---
tag: XD0WBC1MWB
kind: example
name: A subgroup of order two in S3 is not normal
msc: [20B30]
instance_of: [0X1JXT47GA]
not_instance_of:
  - target: 0CB0DX5BVV
    note: a left coset and a right coset differ
  - target: 0W77CVBCHQ
    note: (1 2 3)H is not H(1 2 3)
uses: [0515A6D2Y1, 05FD317V2W]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Examples
---

## Example

In the [[symmetric group|0515A6D2Y1]] $S_3$, let $H = \{e, (1\,2)\}$. Compose permutations from right to left.
$H$ is a subgroup, because $(1\,2)(1\,2) = e$.
The [[left coset|05FD317V2W]] of $(1\,2\,3)$ is $(1\,2\,3)H = \{(1\,2\,3), (1\,3)\}$.
The right coset of $(1\,2\,3)$ is $H(1\,2\,3) = \{(1\,2\,3), (2\,3)\}$.
These cosets are different. Thus $H$ is not [[normal|0W77CVBCHQ]] in $S_3$.

## Remarks

$H$ has index $3$. Thus the result for index two does not apply to $H$.
