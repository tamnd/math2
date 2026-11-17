---
tag: W6V1XYH0K6
kind: proof
name: Proof that homomorphisms preserve identity and inverses
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
proves: 08FKQD7NJ3
uses: [0JYTG5K9Y4, 0VSNX4P2Q0, 0D9NDGE9KP, 00DRK90Z6K]
methods: [0NTF6DMVAP, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Properties
---

## Proof

1. Let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]], and let $e_G$ and $e_H$ be the identity elements of $G$ and $H$.
2. Since $e_G e_G = e_G$, we get $\varphi(e_G)\varphi(e_G) = \varphi(e_G e_G) = \varphi(e_G)$. This step uses the hypothesis that $\varphi$ is a homomorphism.
3. Since $e_H$ is the [[identity|07WYQPB8E3]] of $H$, we have $\varphi(e_G) = \varphi(e_G) e_H$.
4. By steps 2 and 3, $\varphi(e_G)\varphi(e_G) = \varphi(e_G)e_H$. By the [[cancellation laws|0VSNX4P2Q0]] in $H$, $\varphi(e_G) = e_H$. This step uses the hypothesis that $H$ is a group. This proves part 1.
5. Let $a \in G$. Since $aa^{-1} = e_G$, step 4 gives $\varphi(a)\varphi(a^{-1}) = \varphi(aa^{-1}) = \varphi(e_G) = e_H$.
6. By step 5 and the [[uniqueness of inverses|0D9NDGE9KP]], $\varphi(a^{-1}) = \varphi(a)^{-1}$. This proves part 2.
7. We prove part 3 for $n \ge 0$ by [[induction|0ASJVEFA9J]] on $n$. For $n = 0$, both sides are $e_H$, by step 4.
8. Suppose that $\varphi(a^n) = \varphi(a)^n$ for some $n \ge 0$. Then $\varphi(a^{n+1}) = \varphi(a^n a) = \varphi(a^n)\varphi(a) = \varphi(a)^n\varphi(a) = \varphi(a)^{n+1}$, because $\varphi$ is a homomorphism.
9. Now let $n = -m$ with $m > 0$. By the [[laws of exponents|00DRK90Z6K]], $a^{-m} = (a^m)^{-1}$, and the same holds in $H$.
10. By steps 6, 8 and 9, $\varphi(a^{-m}) = \varphi((a^m)^{-1}) = \varphi(a^m)^{-1} = (\varphi(a)^m)^{-1} = \varphi(a)^{-m}$.
11. Steps 7, 8 and 10 prove part 3 for each integer $n$. Together with steps 4 and 6, this proves the lemma.

## Idea

The identity is the only element $x$ of a group with $xx = x$, and $\varphi(e_G)$ has this property.
Once the identity is preserved, $\varphi(a^{-1})$ is an inverse of $\varphi(a)$, and inverses in a group are unique.
Positive powers follow by induction, and negative powers are inverses of positive powers.

## Variants

Part 1 also follows when both sides of $\varphi(e_G)\varphi(e_G) = \varphi(e_G)$ are multiplied on the right by $\varphi(e_G)^{-1}$ in $H$.
Part 2 also follows from $\varphi(a^{-1})\varphi(a) = e_H$, because a left inverse in a group is the inverse.
