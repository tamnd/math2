---
tag: 7FCN2KNWC0
kind: example
name: The integers modulo 2 and the group of signs are isomorphic
msc: [20A05]
instance_of: [08MG7H8JW5]
illustrates: [0736AXH2ME]
uses: [03VFZ2WETT, 085PND4KNT]
sources:
  - url: https://en.wikipedia.org/wiki/Group_isomorphism
    locator: Cyclic groups
---

## Example

Let $\mathbb{Z}/2\mathbb{Z} = \{0, 1\}$ be the [[integers modulo $2$|03VFZ2WETT]] with addition. Let $\{1, -1\}$ be a group under multiplication.
Define $f(0) = 1$ and $f(1) = -1$. Then $f$ is a bijection.
We check the four products: $f(0 + 0) = 1 = 1 \cdot 1$, $f(0 + 1) = -1 = 1 \cdot (-1)$, $f(1 + 0) = -1 = (-1) \cdot 1$ and $f(1 + 1) = f(0) = 1 = (-1) \cdot (-1)$.
Thus $f$ is a homomorphism and a bijection, so $f$ is an [[isomorphism|085PND4KNT]].

## Remarks

Both groups are cyclic of order $2$. This agrees with the result that [[cyclic groups of the same order are isomorphic|0736AXH2ME]].
