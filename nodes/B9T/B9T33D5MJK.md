---
tag: B9T33D5MJK
kind: statement
role: theorem
name: Stone duality
msc: ["06E15", "18F70"]
uses: [0XADJKM699, ZV38HA5PAQ, CQM84EW10G, DQ4E55T3BW, K7A04ZBD92, S4QJ395PA5]
about: [0XADJKM699, ZV38HA5PAQ]
sources:
  - url: https://en.wikipedia.org/wiki/Stone_duality
---

## Statement

Let $\mathbf{Bool}$ be the category of [[Boolean algebras|0XADJKM699]] with Boolean algebra homomorphisms.
Let $\mathbf{Stone}$ be the category of [[Stone spaces|ZV38HA5PAQ]] with continuous maps.
Then $\mathbf{Bool}$ is [[equivalent|K7A04ZBD92]] to the opposite category of $\mathbf{Stone}$, by the following functors.

1. A Boolean algebra $B$ goes to its space $S(B)$ of [[ultrafilters|CQM84EW10G]], with basic open sets $\set{U : a \in U}$ for $a \in B$.
A homomorphism $h \colon A \to B$ goes to the continuous map $S(B) \to S(A)$, $U \mapsto h^{-1}(U)$.
2. A Stone space $X$ goes to the Boolean algebra $\operatorname{Clop}(X)$ of its [[clopen subsets|DQ4E55T3BW]]; a continuous map $f \colon X \to Y$ goes to the homomorphism $\operatorname{Clop}(Y) \to \operatorname{Clop}(X)$, $C \mapsto f^{-1}(C)$.
3. The maps $B \to \operatorname{Clop}(S(B))$, $a \mapsto \set{U : a \in U}$, and $X \to S(\operatorname{Clop}(X))$, $x \mapsto \set{C : x \in C}$, are natural isomorphisms.

## Remarks

The first isomorphism in clause 3 is [[Stone's representation theorem|S4QJ395PA5]].
The second one holds for this reason.
In a compact Hausdorff space with a basis of clopen sets, the members of an ultrafilter of clopen sets have exactly one common point.
Under the duality, injective homomorphisms correspond to surjective continuous maps, and quotients of $B$ correspond to closed subspaces of $S(B)$.
For example, the free Boolean algebra on a set $I$ corresponds to the product space $\set{0, 1}^I$, and the finite Boolean algebras correspond to the finite discrete spaces.

## Explanations

### L1 human

Boolean algebras and a certain kind of compact space are two pictures of the same thing.
Each algebra gives a space, each space gives an algebra, and going there and back returns what one started with.
Maps between algebras become maps between spaces, going in the opposite direction.

### L2 human

Stone duality lets one prove facts about Boolean algebras by topology and facts about Stone spaces by algebra.
For instance, a Boolean algebra is complete exactly when its Stone space is extremally disconnected, and an atom of the algebra corresponds to an isolated point of the space.
It is the model for many later dualities: [[Priestley duality|SA22SEC75K]] for distributive lattices, [[Esakia duality|CD9Y7YP4EJ]] for Heyting algebras, and the duality between spatial frames and sober spaces.
