---
tag: TT0HJQ6QD7
kind: definition
name: Initial algebra
msc: ["18C15", "08C05", "68Q65"]
defines: R76EC56V9R
uses: [4RB8834SEJ, EK85VSSRMR]
sources:
  - url: https://en.wikipedia.org/wiki/Initial_algebra
---

## Definition

Let $\mathcal{C}$ be a category and let $F \colon \mathcal{C} \to \mathcal{C}$ be a functor.
An *initial $F$-algebra* is an [[F-algebra|4RB8834SEJ]] $(I, \iota)$ that is an [[initial object|EK85VSSRMR]] of the category of $F$-algebras.
That is, for every $F$-algebra $(B, \beta)$ there is exactly one morphism $h \colon I \to B$ with $h \circ \iota = \beta \circ F h$.

## Remarks

Example: on $\mathbf{Set}$, let $F X = \set{\ast} \sqcup X$, and let $\iota \colon F \N \to \N$ send $\ast$ to $0$ and $n$ to $n + 1$.
Then $(\N, \iota)$ is an initial $F$-algebra.
Given $(B, \beta)$, the condition on $h$ says $h(0) = \beta(\ast)$ and $h(n + 1) = \beta(h(n))$, and these equations define exactly one function $h$ by recursion.

Non-example: $(\Z, \iota')$ with $\iota'(\ast) = 0$ and $\iota'(n) = n + 1$ is an $F$-algebra but not an initial one.
There is no homomorphism $h$ from it to $(\N, \iota)$: it would satisfy $h(0) = 0$ and $h(-1) + 1 = h(0) = 0$, which has no solution in $\N$.

For an algebraic signature $\sigma$ and the functor $F_\sigma X = \bigsqcup_n \sigma_n \times X^n$, the initial $F_\sigma$-algebra is the algebra of closed terms of $\sigma$.
