---
tag: B6TJS37KQQ
kind: definition
name: Rigid monoidal category
msc: [18M10, 18M05]
defines: A10WW8GEKR
uses: [M3MSQ3NKAE, 8A7YXMW727]
sources:
  - url: https://en.wikipedia.org/wiki/Rigid_category
---

## Definition

A *rigid monoidal category* is a [[monoidal category|M3MSQ3NKAE]] $\mathcal{C}$ in which every object $A$ has both a right [[dual|8A7YXMW727]] $A^*$ and a left dual ${}^*A$.
That is, there is an object $A^*$ with morphisms $A^* \otimes A \to I$ and $I \to A \otimes A^*$ satisfying the zigzag identities.
There is also an object ${}^*A$ with morphisms $A \otimes {}^*A \to I$ and $I \to {}^*A \otimes A$ satisfying the zigzag identities.

## Remarks

Example: the category $\mathbf{FinVect}_k$ of finite-dimensional vector spaces over a field $k$ is rigid.
For $V$ both duals can be taken to be the dual space $V^*$, with evaluation and the coevaluation $1 \mapsto \sum_i e_i \otimes e^i$ or its flip.
Non-example: the category $\mathbf{Vect}_k$ of all vector spaces is not rigid, because an infinite-dimensional space has no dual.
In a rigid category, a morphism $f \colon A \to B$ has a transpose $f^* \colon B^* \to A^*$, and $A \mapsto A^*$ becomes a contravariant functor.
In a braided monoidal category, an object has a right dual if and only if it has a left dual, so asking for one kind suffices.
Rigid monoidal categories are also called autonomous categories; a symmetric rigid monoidal category is called compact closed.
