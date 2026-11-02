---
tag: DF5N0PK3ZS
kind: statement
role: proposition
name: Monad from an adjunction
msc: [18C15, 18A40]
uses: [TZHF6ZM92S, MYGWT305AB, FF6XXA6D1A, 97NPWM3S6E]
about: [FF6XXA6D1A, TZHF6ZM92S]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(category_theory)
---

## Statement

Let $F \colon \mathcal{C} \to \mathcal{D}$ be [[left adjoint|TZHF6ZM92S]] to $G \colon \mathcal{D} \to \mathcal{C}$.
Let $\eta \colon \mathrm{Id}_{\mathcal{C}} \Rightarrow G F$ be the [[unit and $\varepsilon \colon F G \Rightarrow \mathrm{Id}_{\mathcal{D}}$ the counit|MYGWT305AB]] of the adjunction.
Then $(G F, \eta, G \varepsilon F)$ is a [[monad|FF6XXA6D1A]] on $\mathcal{C}$.
Here $G \varepsilon F$ is the natural transformation $G F G F \Rightarrow G F$ with components $G(\varepsilon_{F(X)})$.

## Remarks

The unit laws follow from the triangle identities $\varepsilon F \circ F \eta = \id_F$ and $G \varepsilon \circ \eta G = \id_G$.
Applying $G$ to the first gives $G\varepsilon F \circ G F \eta = \id_{G F}$, and whiskering the second by $F$ gives $G \varepsilon F \circ \eta G F = \id_{G F}$.
Associativity reduces to $\varepsilon \circ F G \varepsilon = \varepsilon \circ \varepsilon F G$, which is the naturality of $\varepsilon$.

Example: the free monoid functor from sets to monoids is left adjoint to the forgetful functor.
The monad $G F$ sends a set $X$ to the set of finite words in $X$, and its multiplication concatenates a word of words.
This is the list monad.

Dually, $(F G, \varepsilon, F \eta G)$ is a [[comonad|97NPWM3S6E]] on $\mathcal{D}$.
Conversely, every monad arises from some adjunction, for example from its Eilenberg–Moore category or its Kleisli category.
Different adjunctions can give the same monad.

## Explanations

### L1 human

When a free construction and a forgetful functor are adjoint, going free and then forgetting is a monad.
Its unit puts an element into the free object as a generator.
Its multiplication evaluates a free expression in free expressions as one free expression.
This is the main source of monads in practice.

### L2 human

This result is half of the link between adjunctions and monads.
The other half says that every monad comes from an adjunction, and that among these there is an initial one, the Kleisli adjunction, and a terminal one, the Eilenberg–Moore adjunction.
A right adjoint is called monadic when the comparison functor to the Eilenberg–Moore category is an equivalence.
Beck's monadicity theorem tells when this happens.
For example, the free group adjunction gives a monad on sets whose algebras are exactly the groups.
