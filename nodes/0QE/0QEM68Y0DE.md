---
tag: 0QEM68Y0DE
kind: statement
role: theorem
name: Cayley–Hamilton theorem for linear maps
msc: [15A04, 15A18]
uses: [0BZ81AJNWF, 0BNEXSKNRV]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley–Hamilton_theorem
    locator: lead section
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $T \colon V \to V$ be a linear map with [[characteristic polynomial|0J5EMJRRFM]] $p_T$.
Then $p_T(T) = 0$, where $p_T(T)$ is the [[value of $p_T$ at $T$|0E3MV6E6MG]].

## Remarks

It follows from the [[Cayley–Hamilton theorem for matrices|0F765KFC2J]] applied to the matrix of $T$ in a basis.
The map $p \mapsto p([T]_B)$ corresponds to $p \mapsto p(T)$ under $T \mapsto [T]_B$.
The statement also holds for endomorphisms of finitely generated modules over a commutative ring, with a suitable characteristic polynomial.

## Explanations

### L1 human

The theorem does not depend on a basis.
A linear map satisfies its characteristic polynomial, because each of its matrices does.
