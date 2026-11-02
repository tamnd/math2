---
tag: DV3PWY8NVW
kind: definition
name: Presheaf
msc: [18F20, 18A25]
defines: AND2WHZC8P
uses: [A2DE66937D, 28NQ0KRHD3, DAMK8XE1FR, KYCPCC57FT, 0CQHFPGJ45, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Presheaf_(category_theory)
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]], let $\mathcal{C}^{\mathrm{op}}$ be its [[opposite category|DAMK8XE1FR]], and let $\mathbf{Set}$ be the category of sets and functions.
A *presheaf* on $\mathcal{C}$ is a [[functor|28NQ0KRHD3]] $F \colon \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$.
So $F$ assigns a set $F(X)$ to each object $X$ and a function $F(f) \colon F(Y) \to F(X)$ to each morphism $f \colon X \to Y$, with $F(\id_X) = \id_{F(X)}$ and $F(g \circ f) = F(f) \circ F(g)$.
A morphism of presheaves is a [[natural transformation|KYCPCC57FT]], and the presheaves on $\mathcal{C}$ form the category $[\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$, often written $\widehat{\mathcal{C}}$.

## Remarks

Example: let $T$ be a [[topological space|0CQHFPGJ45]] and let $\mathcal{O}(T)$ be the category whose objects are the [[open sets|02BH3MCBQB]] of $T$, with one morphism $V \to U$ when $V \subseteq U$.
Let $F(U)$ be the set of continuous functions $U \to \R$ and let $F(V \to U)$ be restriction $s \mapsto s|_V$.
Restriction to $U$ is the identity and restricting to $V$ then to $W$ equals restricting to $W$, so $F$ is a presheaf.

Non-example: on $\mathcal{O}(T)$, let $G(U)$ be the set of all functions $U \to \R$ and send $V \subseteq U$ to extension by zero $G(V) \to G(U)$.
This is a functor $\mathcal{O}(T) \to \mathbf{Set}$, but its maps go from $V$ to $U$, so it is covariant and not a presheaf on $\mathcal{O}(T)$.

Every hom functor $\Hom(-, A)$ is a presheaf, and a presheaf on $\mathcal{O}(T)$ is a presheaf on $T$ in the sense of sheaf theory.
