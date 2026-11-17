---
tag: D05NAAC3XK
kind: proof
name: Proof that a homomorphism is injective iff its kernel is trivial
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
proves: 0N2P0XRTDF
uses: [0JYTG5K9Y4, 0W88CEGQP1, 08FKQD7NJ3, 09NWETVTNY]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Image and kernel
---

## Proof

1. Let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]], and let $K = \ker \varphi$ be its [[kernel|0W88CEGQP1]].
2. Suppose that $\varphi$ is [[injective|09NWETVTNY]], and let $k \in K$. By [[the preservation lemma|08FKQD7NJ3]], $\varphi(e_G) = e_H = \varphi(k)$. Since $\varphi$ is injective, $k = e_G$.
3. Since $e_G \in K$ by the same lemma, step 2 gives $K = \{e_G\}$. This proves the first direction.
4. Let $a, b \in G$ with $\varphi(a) = \varphi(b)$. Then $\varphi(a^{-1}b) = \varphi(a^{-1})\varphi(b) = \varphi(a^{-1})\varphi(a) = \varphi(a^{-1}a) = \varphi(e_G) = e_H$. This step uses the hypothesis that $\varphi$ is a homomorphism and that $G$ is a group, so that $a^{-1}$ exists.
5. So $a^{-1}b \in K$ by the definition of the kernel.
6. Now suppose that $K = \{e_G\}$. By step 5, $a^{-1}b = e_G$. This step uses the hypothesis that the kernel is trivial.
7. Multiply $a^{-1}b = e_G$ on the left by $a$. This gives $b = a$.
8. So any two elements with the same image are equal, and $\varphi$ is injective. This proves the second direction.

## Idea

Two elements $a$ and $b$ have the same image exactly when $a^{-1}b$ lies in the kernel.
So a trivial kernel leaves no room for two different elements with the same image.
The other direction holds because $e_G$ is already in the kernel.

## Variants

The second direction also follows by contrapositive.
If $a \ne b$ and $\varphi(a) = \varphi(b)$, then $a^{-1}b$ is an element of the kernel that differs from $e_G$.
