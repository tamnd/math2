---
tag: 4SCS55K5MA
kind: example
name: The integers modulo the even integers
msc: [20A05]
instance_of: [0KYX2N69J0]
uses: [0C4JS9RF5M, 0YYWCNTPWR, 03VFZ2WETT]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Even and odd integers
---

## Example

Let $G = (\mathbb{Z}, +)$ be the [[integers|0C4JS9RF5M]] with addition, and let $N = 2\mathbb{Z}$ be the even integers. $N$ is normal, because $G$ is abelian.
$N$ has two cosets: $N$, the even integers, and $1 + N$, the odd integers.
The sum of two odd integers is even, so $(1 + N) + (1 + N) = N$.
Thus the [[quotient group|0YYWCNTPWR]] $\mathbb{Z}/2\mathbb{Z}$ has two elements, with identity $N$. It is the [[integers modulo $2$|03VFZ2WETT]].
