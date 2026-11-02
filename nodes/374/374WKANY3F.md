---
tag: 374WKANY3F
kind: definition
name: Well-powered category
msc: [18A32, 18A20]
defines: XVG7FPG227
uses: [A2DE66937D, FS1FKAE89H, 0BSJ7RQ9BW, 00E0YZCERH]
sources:
  - url: https://en.wikipedia.org/wiki/Subobject
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
The category $\mathcal{C}$ is *well-powered* if for every object $X$ of $\mathcal{C}$ the [[subobjects|FS1FKAE89H]] of $X$ form a [[set|0BSJ7RQ9BW]], rather than a proper class.
Dually, $\mathcal{C}$ is *co-well-powered* if for every object $X$ the quotient objects of $X$, the equivalence classes of epimorphisms out of $X$, form a set.

## Remarks

Example: the category of sets is well-powered.
Each subobject of a set $X$ is represented by the inclusion of a subset.
So the subobjects of $X$ are in bijection with the [[power set|00E0YZCERH]] of $X$, which is a set.
The same holds for groups, rings and modules, where subobjects correspond to substructures.
In the category of topological spaces, a subobject of $X$ corresponds to a subset of $X$ with a topology finer than the subspace topology.
These pairs also form a set.

Non-example: let $\mathcal{C}$ have as objects all sets and one more object $X$.
Besides identities, let $\mathcal{C}$ have exactly one morphism $m_S \colon S \to X$ for each set $S$, and nothing else.
It is a category, since no two non-identity morphisms compose.
Each $m_S$ is a monomorphism, since there are no two different morphisms into $S$ from one object, and $m_S \equiv m_T$ only when $S = T$, since there is no morphism between distinct sets.
So the subobjects of $X$ form a proper class, and $\mathcal{C}$ is not well-powered.
