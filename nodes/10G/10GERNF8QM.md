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

We show that $\pi|_W$ is linear, then that its kernel is zero, then that it is onto.

1. The [[quotient map|0J0SK5FF4M]] $\pi$ is linear, so its restriction $\pi|_W$ to the subspace $W$ is linear.
2. Let $w \in W$ with $\pi(w) = 0$, that is, $w + U = 0 + U$ in the [[quotient space|0SVR29SV1V]].
   Two cosets are equal exactly when the representatives differ by a vector of $U$, so $w = w - 0 \in U$.
3. So $w \in U \cap W$.
   Since $W$ is a [[complement|04C3BAHV03]] of $U$, we have $U \cap W = \{0\}$, and so $w = 0$.
4. So the [[kernel|02YFME3RGW]] of $\pi|_W$ is $\{0\}$, and $\pi|_W$ is injective by [[injectivity and the kernel|0BJBYCGMWE]].
5. Now let $v + U$ be any coset.
   Since $U + W = V$, we can write $v = u + w$ with $u \in U$ and $w \in W$.
6. Then $v - w = u \in U$, so $v + U = w + U = \pi|_W(w)$.
   Hence $\pi|_W$ is surjective.
7. A bijective linear map is an isomorphism, so $\pi|_W \colon W \to V / U$ is an isomorphism.
8. If $W'$ is a second complement of $U$, then $\pi|_{W'}$ is also an isomorphism, by steps 1 to 7 for $W'$.
   So the composite $(\pi|_{W'})^{-1} \circ \pi|_W \colon W \to W'$ is an isomorphism.

## Idea

The two conditions of a complement do the two halves of the work.
The intersection condition $U \cap W = \{0\}$ makes $\pi|_W$ injective, because a vector of $W$ that dies in the quotient lies in $U$.
The sum condition $U + W = V$ makes it surjective, because every coset has a representative in $W$.

## Variants

A shorter route applies the [[first isomorphism theorem|0MTBGVZ4XJ]] to $\pi|_W$.
Steps 5 and 6 show that it is surjective, and its kernel is $U \cap W = \{0\}$, so $W \cong W / \{0\} \cong V / U$.

One can also write down the inverse directly.
Send the coset $v + U$ to the $W$-component of $v$ in the decomposition $V = U \oplus W$.
This is well defined, because two representatives of one coset differ by a vector of $U$, and a vector of $U$ has $W$-component $0$.
