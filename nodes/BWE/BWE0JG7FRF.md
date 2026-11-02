---
tag: BWE0JG7FRF
kind: definition
name: Monadic functor
msc: [18C15, 18C20]
defines: DNTDCKZBKK
uses: [TZHF6ZM92S, DF5N0PK3ZS, FEPRJR3MND, K7A04ZBD92]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(category_theory)
---

## Definition

Let $U \colon \mathcal{D} \to \mathcal{C}$ be a functor with a [[left adjoint|TZHF6ZM92S]] $F$ and counit $\varepsilon \colon F U \Rightarrow \mathrm{Id}_{\mathcal{D}}$.
Let $T = U F$ be the [[monad of the adjunction|DF5N0PK3ZS]], and let $\mathcal{C}^T$ be its [[Eilenberg–Moore category|FEPRJR3MND]].
The *comparison functor* $K \colon \mathcal{D} \to \mathcal{C}^T$ sends an object $d$ to the algebra $(U(d), U(\varepsilon_d))$ and a morphism $f$ to $U(f)$.
The functor $U$ is *monadic* if $K$ is an [[equivalence of categories|K7A04ZBD92]].

## Remarks

A functor without a left adjoint is never monadic.
Some authors call $U$ strictly monadic when $K$ is an isomorphism of categories.
The comparison functor always satisfies $U^T \circ K = U$, where $U^T$ is the forgetful functor of $\mathcal{C}^T$.

Example: the forgetful functor from groups to sets is monadic.
Its left adjoint is the free group functor.
An algebra of the monad $T$ is a set $A$ with a map from the free group on $A$ to $A$ satisfying the algebra laws.
Such a map comes from a unique group structure on $A$, and algebra morphisms are group homomorphisms, so $K$ is an isomorphism.

Non-example: the forgetful functor $U$ from topological spaces to sets has the discrete space functor as left adjoint.
The monad $U F$ is the identity monad, whose algebras are just sets, so $\mathcal{C}^T$ is the category of sets.
The comparison functor sends a space to its underlying set, and it is not full, since not every function between spaces is continuous.
So $K$ is not an equivalence and $U$ is not monadic.
