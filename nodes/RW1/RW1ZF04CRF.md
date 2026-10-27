---
tag: RW1ZF04CRF
kind: proof
name: Proof of the uniqueness of inverses
msc: [20A05]
proves: 0D9NDGE9KP
uses: [G5S1M9, 0BRHKKP333]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Group_(mathematics)
    locator: Uniqueness of inverses
---

## Proof

1. Let $a$ be an element of a [[group|G5S1M9]] $G$ with identity $e$. Let $b$ and $c$ both be [[inverses|0BRHKKP333]] of $a$, so $ba = e$ and $ac = e$.
2. Then $b = be = b(ac)$.
3. By associativity, $b(ac) = (ba)c$.
4. Since $ba = e$, $(ba)c = ec = c$.
5. Thus $b = c$, and $a$ has only one inverse.

## Idea

Multiply one inverse by the element and then by the other inverse. Associativity lets the product collapse in two ways.
