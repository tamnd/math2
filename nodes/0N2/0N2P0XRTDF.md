---
tag: 0N2P0XRTDF
kind: statement
role: proposition
name: A homomorphism is injective iff its kernel is trivial
msc: [20A05]
uses: [0Z424HK8CQ, 08FKQD7NJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(algebra)
    locator: Group homomorphisms
---

## Statement

Let $G$ and $H$ be [[groups|G5S1M9]], let $e_G$ be the identity element of $G$, and let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]].
Then $\varphi$ is injective if and only if $\ker \varphi = \{e_G\}$.

## Remarks

If $\varphi(a) = \varphi(b)$, then $\varphi(a^{-1}b) = e_H$, so $a^{-1}b \in \ker \varphi$.
More generally, $\varphi(a) = \varphi(b)$ exactly when $a$ and $b$ lie in the same coset of $\ker \varphi$.

## Explanations

### L1 human

To check that a homomorphism is injective, you only need to check one fibre: the elements that go to the identity.
If only the identity goes to the identity, then no two elements can go to the same place.
This is much easier than comparing all pairs of elements.
