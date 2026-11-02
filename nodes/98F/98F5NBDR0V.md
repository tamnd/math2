---
tag: 98F5NBDR0V
kind: definition
name: F-algebra
msc: ["18C15", "08C05", "08A70"]
defines: 4RB8834SEJ
uses: [A2DE66937D, 28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/F-algebra
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $F \colon \mathcal{C} \to \mathcal{C}$ be a [[functor|28NQ0KRHD3]].
An *$F$-algebra* is a pair $(A, \alpha)$ of an object $A$ of $\mathcal{C}$ and a morphism $\alpha \colon F A \to A$.
A *homomorphism* of $F$-algebras $(A, \alpha) \to (B, \beta)$ is a morphism $h \colon A \to B$ with $h \circ \alpha = \beta \circ F h$.
With these morphisms, $F$-algebras form a category.

## Remarks

Example: on $\mathbf{Set}$, let $F X = \set{\ast} \sqcup X$.
The natural numbers with $\alpha(\ast) = 0$ and $\alpha(n) = n + 1$ form an $F$-algebra $(\N, \alpha)$.
More generally, for an algebraic signature $\sigma$ with $\sigma_n$ the set of $n$-ary symbols, the $F_\sigma$-algebras for $F_\sigma X = \bigsqcup_n \sigma_n \times X^n$ are exactly the $\sigma$-algebras, and their homomorphisms are the usual ones.

Non-example: a morphism $\gamma \colon A \to F A$ in the other direction does not make $A$ an $F$-algebra; such a pair $(A, \gamma)$ is an [[F-coalgebra|6BS0300CMV]].
For $F X = \set{\ast} \sqcup X$ on $\mathbf{Set}$, a coalgebra describes a system in which each state either stops or has one next state.

If $(T, \eta, \mu)$ is a monad, every algebra over the monad is a $T$-algebra in this sense, but not conversely, since no unit or associativity law is required here.
