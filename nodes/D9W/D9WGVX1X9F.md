---
tag: D9WGVX1X9F
kind: proof
name: Proof of the naturality of the evaluation map
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug2
proves: R19758JQWE
methods: [0NTF6DMVAP]
uses: [0ZJM9D7NPS, 0C2TQMW5A1]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_transformation
    locator: Double dual of a vector space
---

## Proof

We evaluate both sides at a vector $v$ and then at a form $\varphi$, and unwind the definitions until both give $\varphi(f(v))$.
Two elements of $W^{**}$ are equal when they agree on every $\varphi \in W^*$, so it is enough to fix $v \in V$ and $\varphi \in W^*$.

1. By the definition of the [[dual map|0C2TQMW5A1]], applied to $f^*$, we have $f^{**}(\Psi) = \Psi \circ f^*$ for each $\Psi \in V^{**}$.
2. So $f^{**}(\operatorname{ev}_V(v))(\varphi) = \operatorname{ev}_V(v)(f^*(\varphi))$.
3. By the definition of the [[evaluation map|0ZJM9D7NPS]] $\operatorname{ev}_V$, this value is $(f^*(\varphi))(v)$.
4. By the definition of $f^*$, we have $f^*(\varphi) = \varphi \circ f$, so the value is $\varphi(f(v))$.
5. On the other side, the definition of $\operatorname{ev}_W$ gives $\operatorname{ev}_W(f(v))(\varphi) = \varphi(f(v))$.
6. Steps 4 and 5 give the same value, and $\varphi$ was arbitrary, so $f^{**}(\operatorname{ev}_V(v)) = \operatorname{ev}_W(f(v))$.
7. Since $v$ was arbitrary, $f^{**} \circ \operatorname{ev}_V = \operatorname{ev}_W \circ f$.

## Idea

Nothing is computed here, and no basis appears.
Both sides of the square are machines that take a vector $v$ and a form $\varphi$ on $W$ and return a number.
Unwinding the definitions shows that both machines return $\varphi(f(v))$.
This is typical of naturality proofs: when the maps are defined without choices, they commute with everything for formal reasons.

## Variants

In finite dimension one can check the square in bases instead.
Choose bases $(b_i)$ of $V$ and $(c_j)$ of $W$, and let $A$ be the matrix of $f$.
The evaluation map sends $b_i$ to the dual basis of the dual basis, so $\operatorname{ev}_V$ and $\operatorname{ev}_W$ have identity matrices in these bases.
By the theorem on the [[matrix of the dual map|0ZPB3180AY]] applied twice, $f^{**}$ has matrix $(A^{\mathsf{T}})^{\mathsf{T}} = A$.
So both paths around the square have matrix $A$.
This proof needs finite dimension, while the proof above does not.
