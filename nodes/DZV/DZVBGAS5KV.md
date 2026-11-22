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

We check each identity by evaluating both sides, since two forms are equal when they agree at every vector and two linear maps are equal when they agree at every input.

1. For part 1, let $\varphi, \psi \in W^*$, let $a, b \in F$ and let $v \in V$. By the definition of the [[dual map|0C2TQMW5A1]] and the pointwise operations of $W^*$, $f^*(a\varphi + b\psi)(v) = (a\varphi + b\psi)(f(v)) = a\varphi(f(v)) + b\psi(f(v))$.
2. The right side of step 1 is $(a f^*(\varphi) + b f^*(\psi))(v)$, by the pointwise operations of $V^*$. Since $v$ was arbitrary, $f^*$ is linear.
3. For part 2, let $f, g \colon V \to W$, let $\varphi \in W^*$ and let $v \in V$. Since $\varphi$ is linear, $(af + bg)^*(\varphi)(v) = \varphi(a f(v) + b g(v)) = a\varphi(f(v)) + b\varphi(g(v))$.
4. The right side of step 3 is $(a f^* + b g^*)(\varphi)(v)$. Since $\varphi$ and $v$ were arbitrary, $(af + bg)^* = a f^* + b g^*$.
5. For part 3, let $f \colon U \to V$, $g \colon V \to W$ and $\varphi \in W^*$. By definition, $(g \circ f)^*(\varphi) = \varphi \circ (g \circ f)$.
6. [[Composition|00BKRZKMSS]] of maps is associative, so $\varphi \circ (g \circ f) = (\varphi \circ g) \circ f$. This is $f^*(\varphi \circ g) = f^*(g^*(\varphi))$, so $(g \circ f)^* = f^* \circ g^*$.
7. For part 4, let $\varphi \in V^*$. Then $(\id_V)^*(\varphi) = \varphi \circ \id_V = \varphi$, so $(\id_V)^* = \id_{V^*}$.
8. For part 5, let $f \colon V \to W$ have the inverse $f^{-1} \colon W \to V$. By parts 3 and 4, $f^* \circ (f^{-1})^* = (f^{-1} \circ f)^* = (\id_V)^* = \id_{V^*}$.
9. In the same way, $(f^{-1})^* \circ f^* = (f \circ f^{-1})^* = (\id_W)^* = \id_{W^*}$.
10. By steps 8 and 9, $(f^{-1})^*$ is a two-sided inverse of $f^*$, so $f^*$ is an isomorphism with $(f^*)^{-1} = (f^{-1})^*$.

## Idea

Every part comes down to the definition $f^*(\varphi) = \varphi \circ f$.
Linearity comes from the fact that the operations on forms act value by value.
The order reversal is associativity of composition read in a new way: $\varphi \circ g \circ f$ can be grouped as $(\varphi \circ g) \circ f$, so $\varphi$ is first pulled back along $g$ and then along $f$.
Part 5 then follows from parts 3 and 4 with no further work.

## Variants

In finite dimension, part 3 also follows from matrices.
In dual bases the matrix of $(g \circ f)^*$ is $(BA)^{\mathsf{T}}$ and the matrix of $f^* \circ g^*$ is $A^{\mathsf{T}} B^{\mathsf{T}}$, by the theorem on the [[matrix of the dual map|0ZPB3180AY]], and the [[transpose of a product|09GK5PS824]] says these are equal.
This route needs bases, and it gives nothing in infinite dimension, so the direct proof above is the better one.
