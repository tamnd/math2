---
tag: EC6C1MR0C1
kind: definition
name: Extensive category
msc: [18B50]
defines: 5H16H7FY5D
uses: [4FJ0S71P58, 1TC7W7BQT3, AFNE9C4NH6, K7A04ZBD92, Q05K04QJ71]
sources:
  - url: https://en.wikipedia.org/wiki/Extensive_category
---

## Definition

Let $\mathcal{C}$ be a category with finite [[coproducts|4FJ0S71P58]].
For objects $A$ and $B$ consider the functor
$$+ \colon \mathcal{C}/A \times \mathcal{C}/B \to \mathcal{C}/(A + B)$$
that sends a pair $(f \colon X \to A, \, g \colon Y \to B)$ to $f + g \colon X + Y \to A + B$.
Here $\mathcal{C}/A$ is the [[slice category|1TC7W7BQT3]] over $A$ and the domain is a [[product category|AFNE9C4NH6]].
The category $\mathcal{C}$ is *extensive*, or finitarily extensive, if this functor is an [[equivalence of categories|K7A04ZBD92]] for all objects $A$ and $B$.

## Remarks

An equivalent form: $\mathcal{C}$ has [[pullbacks|Q05K04QJ71]] along the coproduct injections, and the following holds.
For every commutative diagram whose bottom row is $A \to A + B \leftarrow B$ and whose top row is $X_1 \to X \leftarrow X_2$, the top row is a coproduct if and only if both squares are pullbacks.
In an extensive category coproducts are disjoint, and the initial object is strict.

Example: the category of sets is extensive.
A map $h \colon X \to A + B$ is, up to isomorphism, the sum of its restrictions $h^{-1}(A) \to A$ and $h^{-1}(B) \to B$, and this decomposition is unique.

Non-example: the category of real vector spaces, where the coproduct is the direct sum.
Let $\Delta \colon \R \to \R \oplus \R$ be the diagonal $x \mapsto (x, x)$.
The pullbacks of $\Delta$ along both injections are the zero space, since $(x, x) = (a, 0)$ forces $x = 0$.
But $0 \oplus 0 = 0$ is not $\R$, so in the equivalent form the squares are pullbacks while the top row is not a coproduct.
