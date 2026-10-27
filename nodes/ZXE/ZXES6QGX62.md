---
tag: ZXES6QGX62
kind: proof
name: Proof of the cancellation laws
msc: [20A05]
proves: 0VSNX4P2Q0
uses: [G5S1M9, 0BRHKKP333]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Group_(mathematics)
    locator: Division
---

## Proof

1. Let $a$, $b$ and $c$ be elements of a [[group|G5S1M9]] $G$ with identity $e$, and suppose that $ab = ac$.
2. Multiply both sides on the left by the [[inverse|0BRHKKP333]] $a^{-1}$. This gives $a^{-1}(ab) = a^{-1}(ac)$.
3. By associativity, $(a^{-1}a)b = (a^{-1}a)c$, so $eb = ec$ and $b = c$.
4. Now suppose that $ba = ca$. Multiply both sides on the right by $a^{-1}$.
5. By associativity, $b(aa^{-1}) = c(aa^{-1})$, so $be = ce$ and $b = c$.

## Idea

Multiply both sides of the equation by the inverse of the common factor, on the same side as that factor.
