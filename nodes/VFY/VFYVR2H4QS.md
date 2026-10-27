---
tag: VFYVR2H4QS
kind: example
name: The odd integers are not a subgroup of the integers
msc: [20A05]
not_instance_of:
  - target: 0X1JXT47GA
    note: the sum of two odd integers is even
uses: [0C4JS9RF5M, 0N0PXCTYA7]
sources:
  - url: https://en.wikipedia.org/wiki/Subgroup
    locator: Subgroup tests
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Even and odd integers
---

## Example

Let $G = (\mathbb{Z}, +)$ be the [[integers|0C4JS9RF5M]] with addition, and let $O$ be the set of odd integers.
The identity $0$ is not odd, so $0 \notin O$.
Also, $1 \in O$ and $1 + 1 = 2 \notin O$. Thus $O$ is not closed under addition.
Thus $O$ is not a [[subgroup|0N0PXCTYA7]] of $G$.

## Remarks

$O$ is a coset of the even integers. A coset $g + H$ is a subgroup only when $g \in H$.
