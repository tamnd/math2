---
tag: CZWDNA1HA7
kind: definition
name: Algebra over a monad
msc: [18C20, 18C15]
defines: QG1ZXRC8EH
uses: [FF6XXA6D1A, CV013KHVJG, 0N6R902FG1]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(category_theory)
---

## Definition

Let $(T, \eta, \mu)$ be a [[monad|FF6XXA6D1A]] on a category $\mathcal{C}$.
A *$T$-algebra* is a pair $(A, a)$ of an object $A$ of $\mathcal{C}$ and a morphism $a \colon T(A) \to A$ with these two properties.

1. Unit law: $a \circ \eta_A = \id_A$.
2. Associativity law: $a \circ T(a) = a \circ \mu_A$ as morphisms $T(T(A)) \to A$.

A *morphism of $T$-algebras* $f \colon (A, a) \to (B, b)$ is a morphism $f \colon A \to B$ of $\mathcal{C}$ with $f \circ a = b \circ T(f)$.

## Remarks

Example: let $T$ be the list monad on sets, so $T(X)$ is the [[free monoid|CV013KHVJG]] of finite words in $X$.
For a [[monoid|0N6R902FG1]] $M$, let $a$ send a word $(m_1, \dots, m_n)$ to the product $m_1 m_2 \cdots m_n$ in $M$, with the empty word sent to the identity.
The unit law holds since a one-letter word $m$ evaluates to $m$.
The associativity law holds since multiplying the blocks of a word of words and then multiplying the results gives the product of the concatenated word.
Every $T$-algebra arises in this way, so $T$-algebras are the same as monoids.

Non-example: for the same monad, let $a \colon T(\N) \to \N$ send a word to its length.
Then $a(\eta_{\N}(5)) = 1 \ne 5$, so the unit law fails.

For every object $X$, the pair $(T(X), \mu_X)$ is a $T$-algebra, the free $T$-algebra on $X$.
