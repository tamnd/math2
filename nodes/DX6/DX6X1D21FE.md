---
tag: DX6X1D21FE
kind: example
name: The Klein four-group is abelian but not cyclic
msc: [20A05]
instance_of: [082GHNPJ53]
not_instance_of:
  - target: 0KVGH0J5B3
    note: no element generates the group
  - target: 0B85Q41RP6
    note: each element generates a subgroup with at most two elements
uses: [0PMRQJVTME, 0JPYSD5E0B]
sources:
  - url: https://en.wikipedia.org/wiki/Klein_four-group
    locator: lead section
---

## Example

The [[Klein four-group|0PMRQJVTME]] is $V = \{e, a, b, c\}$, where $a^2 = b^2 = c^2 = e$ and $ab = ba = c$.
The group is abelian.
Each element that is not $e$ has [[order|0JPYSD5E0B]] $2$. Thus each element generates a subgroup with at most $2$ elements.
No element generates all $4$ elements, so $V$ is not [[cyclic|0B85Q41RP6]].

## Remarks

Thus the converse of the result that cyclic groups are abelian is false.
Up to isomorphism, $V$ and $\mathbb{Z}/4\mathbb{Z}$ are the only groups of order $4$.
