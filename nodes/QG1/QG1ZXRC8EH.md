---
tag: QG1ZXRC8EH
kind: concept
name: Algebra over a monad
msc: [18C20, 18C15]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(category_theory)
---

## Summary

An algebra over a [[monad|FF6XXA6D1A]] $T$ on a category $\mathcal{C}$ is an object $A$ with a structure map $a \colon T(A) \to A$.
The structure map must be compatible with the unit and the multiplication of $T$.
These algebras, with the maps that respect the structure maps, form the Eilenberg–Moore category of $T$.
Many algebraic structures are algebras over a monad on sets.
Examples are monoids for the list monad, complete join-semilattices for the power set monad, and modules for the free module monad.

## Explanations

### L1 human

A monad describes formal expressions, and an algebra is a way to evaluate them.
The structure map $a$ takes a formal expression in elements of $A$ and returns an element of $A$.
The first law says that evaluating a single element gives back that element.
The second law says that evaluating in stages gives the same result as flattening first and evaluating once.
For the list monad, a monoid $M$ is an algebra: a list $(m_1, \dots, m_n)$ evaluates to the product $m_1 \cdots m_n$.
