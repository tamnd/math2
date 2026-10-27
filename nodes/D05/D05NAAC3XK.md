---
tag: D05NAAC3XK
kind: proof
name: Proof that a homomorphism is injective iff its kernel is trivial
msc: [20A05]
proves: 0N2P0XRTDF
uses: [0Z424HK8CQ, 08FKQD7NJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Image and kernel
---

## Proof

1. Let $\varphi : G \to H$ be a group homomorphism with [[kernel|0Z424HK8CQ]] $K$.
2. Suppose that $\varphi$ is injective, and let $k \in K$. [[$\varphi(e) = e$|08FKQD7NJ3]], so $\varphi(k) = \varphi(e)$. Thus $k = e$, and $K = \{e\}$.
3. Now suppose that $K = \{e\}$, and let $a, b \in G$ with $\varphi(a) = \varphi(b)$.
4. Then $\varphi(a^{-1}b) = \varphi(a)^{-1}\varphi(b) = e$, so $a^{-1}b \in K$.
5. Thus $a^{-1}b = e$, so $a = b$, and $\varphi$ is injective.

## Idea

Two elements have the same image exactly when their quotient is in the kernel.
