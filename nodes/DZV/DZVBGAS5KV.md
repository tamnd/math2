---
tag: DZVBGAS5KV
kind: proof
name: Proof of the functoriality of the dual map
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug2
proves: XBKREPBM9D
methods: [0NTF6DMVAP]
uses: [0C2TQMW5A1, 00BKRZKMSS]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Properties
---

## Proof

Two forms are equal when they agree at every vector, and two linear maps are equal when they agree at every input.

1. Let $\varphi, \psi \in W^*$ and $a, b \in F$. For $v \in V$, $f^*(a\varphi + b\psi)(v) = (a\varphi + b\psi)(f(v)) = a\varphi(f(v)) + b\psi(f(v))$.
2. The right side is $(a f^*(\varphi) + b f^*(\psi))(v)$. So $f^*$ is linear, which is part 1.
3. Let $f, g \colon V \to W$ and $\varphi \in W^*$. For $v \in V$, $(af + bg)^*(\varphi)(v) = \varphi(a f(v) + b g(v)) = a\varphi(f(v)) + b\varphi(g(v))$, by linearity of $\varphi$.
4. The right side is $(a f^* + b g^*)(\varphi)(v)$. So $(af + bg)^* = a f^* + b g^*$, which is part 2.
5. Let $f \colon U \to V$, $g \colon V \to W$ and $\varphi \in W^*$. Then $(g \circ f)^*(\varphi) = \varphi \circ (g \circ f)$.
6. Composition is associative, so $\varphi \circ (g \circ f) = (\varphi \circ g) \circ f = f^*(g^*(\varphi))$. This is part 3.
7. For $\varphi \in V^*$, $(\id_V)^*(\varphi) = \varphi \circ \id_V = \varphi$. This is part 4.
8. Let $f$ be an isomorphism with inverse $f^{-1}$. By parts 3 and 4, $f^* \circ (f^{-1})^* = (f^{-1} \circ f)^* = (\id_V)^* = \id_{V^*}$.
9. In the same way, $(f^{-1})^* \circ f^* = (f \circ f^{-1})^* = \id_{W^*}$. So $f^*$ is invertible with inverse $(f^{-1})^*$, which is part 5.

## Idea

Every part reduces to the associativity of composition and the definition $f^*(\varphi) = \varphi \circ f$.

## Variants

In finite dimension, one can prove part 3 with matrices: the matrix of $(g \circ f)^*$ is $(BA)^{\mathsf{T}}$, and the [[transpose of a product|09GK5PS824]] is $A^{\mathsf{T}} B^{\mathsf{T}}$.
This uses the theorem on the [[matrix of the dual map|0ZPB3180AY]] and needs bases.
