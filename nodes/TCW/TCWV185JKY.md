---
tag: TCWV185JKY
kind: definition
name: F-coalgebra
msc: [18C15, 68Q85]
defines: 6BS0300CMV
uses: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/F-coalgebra
---

## Definition

Let $\mathcal{C}$ be a category and let $F \colon \mathcal{C} \to \mathcal{C}$ be a [[functor|28NQ0KRHD3]].
An *$F$-coalgebra* is a pair $(A, \alpha)$ of an object $A$ of $\mathcal{C}$ and a morphism $\alpha \colon A \to F(A)$.
A *homomorphism* of $F$-coalgebras $f \colon (A, \alpha) \to (B, \beta)$ is a morphism $f \colon A \to B$ with $\beta \circ f = F(f) \circ \alpha$.

## Remarks

The $F$-coalgebras and their homomorphisms form a category.
An $F$-coalgebra is the same as an algebra for the functor $F^{\mathrm{op}}$ on $\mathcal{C}^{\mathrm{op}}$.

Example: on the category of sets let $F(X) = \N \times X$, so $F(f) = \id_{\N} \times f$.
The map $\alpha \colon \N \to \N \times \N$ with $\alpha(n) = (n, n + 1)$ makes $(\N, \alpha)$ an $F$-coalgebra.
The set $\N^{\N}$ of streams with $\sigma(s) = (s_0, (s_1, s_2, \dots))$ is the terminal $F$-coalgebra.
The unique homomorphism from $(\N, \alpha)$ sends $n$ to the stream $(n, n + 1, n + 2, \dots)$.

Non-example: the map $f \colon \N \to \N$ with $f(n) = n + 1$ is not a homomorphism from $(\N, \alpha)$ to itself.
Indeed $\alpha(f(n)) = (n + 1, n + 2)$, while $F(f)(\alpha(n)) = (n, n + 2)$.
