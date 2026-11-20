---
tag: 10GERNF8QM
kind: proof
name: Proof that every complement is isomorphic to the quotient
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
proves: 244KTXDJHW
methods: [0NTF6DMVAP]
uses: [04C3BAHV03, 0SVR29SV1V, 0J0SK5FF4M, 0BJBYCGMWE, 02YFME3RGW]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Properties
---

## Proof

1. The [[quotient map|0J0SK5FF4M]] $\pi$ is linear, so its restriction $\pi|_W$ to the subspace $W$ is linear.
2. Kernel. Let $w \in W$ with $\pi(w) = 0$, that is, $w + U = 0 + U$ in the [[quotient space|0SVR29SV1V]]. Then $w - 0 = w \in U$.
3. So $w \in U \cap W$. Since $W$ is a [[complement|04C3BAHV03]] of $U$, $U \cap W = \{0\}$, and $w = 0$.
4. So the [[kernel|02YFME3RGW]] of $\pi|_W$ is $\{0\}$, and $\pi|_W$ is injective by [[injectivity and the kernel|0BJBYCGMWE]].
5. Image. Let $v + U$ be a coset. Since $U + W = V$, we can write $v = u + w$ with $u \in U$ and $w \in W$.
6. Then $v - w = u \in U$, so $v + U = w + U = \pi|_W(w)$.
7. So $\pi|_W$ is surjective.
8. A bijective linear map is an isomorphism, so $\pi|_W \colon W \to V / U$ is an isomorphism.
9. If $W'$ is another complement, then $(\pi|_{W'})^{-1} \circ \pi|_W \colon W \to W'$ is an isomorphism.

## Idea

The intersection condition makes $\pi|_W$ injective, and the sum condition makes it surjective.

## Variants

- Apply the [[first isomorphism theorem|0MTBGVZ4XJ]] to $\pi|_W$, which is surjective with kernel $U \cap W = \{0\}$.
- Define the inverse directly: send $v + U$ to the $W$-component of $v$. It is well defined because two representatives differ by a vector of $U$, which has $W$-component $0$.
