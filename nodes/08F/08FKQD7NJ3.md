---
tag: 08FKQD7NJ3
kind: statement
role: proposition
name: Homomorphisms preserve identity and inverses
msc: [20A05]
uses: [0HV9Y7WG5R, 0VSNX4P2Q0, 0D9NDGE9KP]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Properties
---

## Statement

Let $G$ and $H$ be [[groups|G5S1M9]] with identity elements $e_G$ and $e_H$, and let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]].
Then $\varphi(e_G) = e_H$, and $\varphi(a^{-1}) = \varphi(a)^{-1}$ for each $a \in G$.

## Remarks

The first equation follows from $\varphi(e_G) \varphi(e_G) = \varphi(e_G) = \varphi(e_G) e_H$ and [[cancellation|0VSNX4P2Q0]].
The second follows from $\varphi(a) \varphi(a^{-1}) = \varphi(e_G) = e_H$ and [[the uniqueness of inverses|0D9NDGE9KP]].
A consequence is that $\varphi(a^n) = \varphi(a)^n$ for each integer $n$.

## Explanations

### L1 human

A map that respects products automatically respects the identity and the inverses.
You do not need to ask for these two properties in the definition of a homomorphism.
For example, the exponential map sends $0$ to $1$ and $-x$ to $1/e^x$.
