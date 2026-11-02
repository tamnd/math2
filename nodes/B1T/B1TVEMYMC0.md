---
tag: B1TVEMYMC0
kind: definition
name: Eilenberg–Moore category
msc: [18C20]
defines: FEPRJR3MND
uses: [A2DE66937D, QG1ZXRC8EH, TZHF6ZM92S, 0N6R902FG1]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(category_theory)
---

## Definition

Let $(T, \eta, \mu)$ be a monad on a [[category|A2DE66937D]] $\mathcal{C}$.
The *Eilenberg–Moore category* $\mathcal{C}^T$ has these parts.

1. Its objects are the [[$T$-algebras|QG1ZXRC8EH]] $(A, a)$.
2. Its morphisms $(A, a) \to (B, b)$ are the morphisms of $T$-algebras, that is, the $f \colon A \to B$ with $f \circ a = b \circ T(f)$.
3. Composition and identities are those of $\mathcal{C}$.

The forgetful functor $U^T \colon \mathcal{C}^T \to \mathcal{C}$ sends $(A, a)$ to $A$.
The free functor $F^T \colon \mathcal{C} \to \mathcal{C}^T$ sends $X$ to $(T(X), \mu_X)$ and $f$ to $T(f)$.

## Remarks

The functor $F^T$ is [[left adjoint|TZHF6ZM92S]] to $U^T$, and $U^T F^T = T$.
The unit of the adjunction is $\eta$, and the monad of the adjunction is $(T, \eta, \mu)$.

Example: for the list monad on sets, $\mathcal{C}^T$ is isomorphic to the category of [[monoids|0N6R902FG1]] and monoid homomorphisms.
A morphism of algebras $f$ satisfies $f(m_1 \cdots m_n) = f(m_1) \cdots f(m_n)$, which is exactly the condition to be a monoid homomorphism.

Non-example: the category whose objects are monoids and whose morphisms are all functions between them is not $\mathcal{C}^T$.
A function such as $n \mapsto n + 1$ on $(\N, +)$ does not satisfy clause 2, since it does not send $0 + 0$ to $1 + 1$.

The notation $\mathcal{C}^T$ is standard.
The full subcategory of free algebras is equivalent to the Kleisli category of $T$.
