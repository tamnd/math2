---
tag: 9VY3JT31RW
kind: definition
name: Sheafification
msc: [18F20, 18F10]
defines: 2HYK3KBQNA
uses: [NYE0Z94MME, AND2WHZC8P, RT8A8FJ566, TZHF6ZM92S]
sources:
  - url: https://en.wikipedia.org/wiki/Sheaf_(mathematics)
---

## Definition

Let $(\mathcal{C}, J)$ be a small [[site|NYE0Z94MME]] and let $P$ be a [[presheaf|AND2WHZC8P]] of sets on $\mathcal{C}$.
A *sheafification* of $P$ is a [[sheaf|RT8A8FJ566]] $aP$ for $J$ together with a morphism of presheaves $\eta \colon P \to aP$ with this property.
For every sheaf $F$ and every morphism $\varphi \colon P \to F$, there is exactly one morphism of sheaves $\psi \colon aP \to F$ with $\psi \circ \eta = \varphi$.

## Remarks

A sheafification exists for every presheaf on a small site and is unique up to unique isomorphism.
So $P \mapsto aP$ is a functor $\mathrm{PSh}(\mathcal{C}) \to \mathrm{Sh}(\mathcal{C}, J)$, [[left adjoint|TZHF6ZM92S]] to the inclusion, and it preserves finite limits.
One construction is $aP = (P^+)^+$, where $P^+(c)$ is the colimit over covering sieves $S \in J(c)$ of the sets of matching families for $S$.
If $P$ is already a sheaf, then $\eta$ is an isomorphism.
Example: on the site of open sets of a space $X$, the sheafification of the constant presheaf $U \mapsto A$ is the sheaf of locally constant functions $U \to A$.
Non-example: let $A = \set{0, 1}$.
The constant presheaf itself, with $\eta = \id$, is not a sheafification, since it is not a sheaf.
Indeed, the empty sieve covers $\emptyset$, and its unique (empty) matching family has two amalgamations in $P(\emptyset) = A$.
The sheafification repairs this: the sheaf of locally constant functions has exactly one section over $\emptyset$.
