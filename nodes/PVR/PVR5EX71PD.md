---
tag: PVR5EX71PD
kind: example
name: Doubling on the integers is not an isomorphism
msc: [20A05]
instance_of: [0JYTG5K9Y4]
not_instance_of:
  - target: 08MG7H8JW5
    note: the image is the even integers, so the map is not onto
uses: [0C4JS9RF5M, 085PND4KNT, 0PVG1CRAJN, 0XKH881BZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Group_isomorphism
    locator: Definition and notation
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Types
---

## Example

Let $G = (\mathbb{Z}, +)$ be the [[integers|0C4JS9RF5M]] with addition. Define $d : G \to G$ by $d(u) = 2u$.
Then $d(u + v) = 2u + 2v = d(u) + d(v)$, so $d$ is a homomorphism.
If $2u = 0$, then $u = 0$. Thus the kernel is $\{0\}$, and $d$ is [[injective|0PVG1CRAJN]].
The image of $d$ is the set of even integers. Thus $1$ is not in the image, and $d$ is not [[surjective|0XKH881BZ7]].
Thus $d$ is not an [[isomorphism|085PND4KNT]].

## Remarks

The image $2\mathbb{Z}$ is isomorphic to $\mathbb{Z}$. Thus $d$ is an isomorphism from $\mathbb{Z}$ onto $2\mathbb{Z}$, but not onto $\mathbb{Z}$.
