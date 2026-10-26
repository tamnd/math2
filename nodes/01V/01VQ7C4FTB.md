---
tag: 01VQ7C4FTB
kind: statement
role: theorem
name: Uniqueness of the algebraic closure
msc: [12F05]
uses: [0MCXX29HWY, 069A3BC3EP]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_closure
    locator: lead section
---

## Statement

Let $K$ be a [[field|0QA8CHH8MG]], and let $L$ and $L'$ be [[algebraic closures|0MCXX29HWY]] of $K$.
Then there is a ring isomorphism $\sigma \colon L \to L'$ with $\sigma(c) = c$ for every $c \in K$.

## Remarks

The proof uses Zorn's lemma on the partial isomorphisms between subfields of $L$ and $L'$ that fix $K$.
The isomorphism is not unique in general. For example, complex conjugation and the identity are two such isomorphisms from $\mathbb{C}$ to $\mathbb{C}$ over $\mathbb{R}$.
So one often writes "the" algebraic closure $\overline{K}$.
The statement is an infinite form of the [[uniqueness of splitting fields|069A3BC3EP]].

## Explanations

### L1 human

Two algebraic closures of the same field are the same field with different names for the elements.
There can be many ways to match them, so the matching is not part of the structure.
