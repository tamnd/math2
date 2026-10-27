---
tag: BV08DGBD7C
kind: example
name: Reduction modulo n is a homomorphism
msc: [20A05]
instance_of: [0JYTG5K9Y4]
illustrates: [0CXXJNG5B6]
uses: [0C4JS9RF5M, 03VFZ2WETT, 0Z424HK8CQ]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Examples
---

## Example

Let $n \ge 1$. Define $\varphi : \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ by $\varphi(u) = u \bmod n$.
Then $\varphi(u + v) = \varphi(u) + \varphi(v)$, so $\varphi$ is a group homomorphism.
The map is onto, and its [[kernel|0Z424HK8CQ]] is $n\mathbb{Z}$, the integers that $n$ divides.
By the [[first isomorphism theorem|0CXXJNG5B6]], $\mathbb{Z}/n\mathbb{Z}$ as a quotient of $\mathbb{Z}$ is isomorphic to the image, the [[integers modulo $n$|03VFZ2WETT]].
