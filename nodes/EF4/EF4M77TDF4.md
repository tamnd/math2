---
tag: EF4M77TDF4
kind: definition
name: Equivalence of varieties
msc: [08B05]
defines: 9SNTXYEEBQ
uses: [32PDB3WQ4D, AJNZJD8442]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
---

## Definition

Let $\mathcal{V}$ and $\mathcal{W}$ be [[varieties|AJNZJD8442]] of algebras.
Let $\rho$ be an [[interpretation|32PDB3WQ4D]] of $\mathcal{V}$ in $\mathcal{W}$, which sends each $A \in \mathcal{W}$ to an algebra $A^{\rho} \in \mathcal{V}$ on the same set.
Let $\theta$ be an interpretation of $\mathcal{W}$ in $\mathcal{V}$, which sends each $B \in \mathcal{V}$ to an algebra $B^{\theta} \in \mathcal{W}$ on the same set.
The pair $(\rho, \theta)$ is an *equivalence* if $(A^{\rho})^{\theta} = A$ for all $A \in \mathcal{W}$ and $(B^{\theta})^{\rho} = B$ for all $B \in \mathcal{V}$.
The varieties $\mathcal{V}$ and $\mathcal{W}$ are *equivalent*, or *term equivalent*, if such a pair exists.

## Remarks

Example: Boolean algebras and Boolean rings are equivalent.
One translation is $x + y \mapsto (x \wedge \neg y) \vee (\neg x \wedge y)$, $x \cdot y \mapsto x \wedge y$, with $0$ and $1$ kept.
The other is $x \vee y \mapsto x + y + xy$, $x \wedge y \mapsto xy$, $\neg x \mapsto 1 + x$.
Going there and back recovers each operation, for example $x + y + xy$ becomes the join again in every Boolean algebra.
Non-example: the variety of Boolean algebras is not equivalent to the variety of distributive lattices with signature $\vee, \wedge$.
There is not even an interpretation of Boolean algebras in distributive lattices, because every lattice term contains a variable, so no term can stand for the constant $0$.
Equivalent varieties have, on each set, the same subalgebras, the same congruences and the same term operations.

## Explanations

### L1 human

Two varieties are equivalent when they describe the same structures with different but interchangeable basic operations.
