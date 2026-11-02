---
tag: G0MYA3D9ZZ
kind: definition
name: Subobject
msc: [18A20, 18A32]
defines: FS1FKAE89H
uses: [A2DE66937D, 859F0TFVA3, Y2NP1JFR86, 0G8VEZ3WTK, 0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Subobject
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $X$ be an object of $\mathcal{C}$.
For [[monomorphisms|Y2NP1JFR86]] $m \colon A \to X$ and $m' \colon A' \to X$, write $m \le m'$ if there is a [[morphism|859F0TFVA3]] $k \colon A \to A'$ with $m = m' \circ k$, and write $m \equiv m'$ if $m \le m'$ and $m' \le m$.
A *subobject* of $X$ is an equivalence class of monomorphisms into $X$ for the [[equivalence relation|0G8VEZ3WTK]] $\equiv$.

## Remarks

Since $m'$ is a monomorphism, the factor $k$ in $m = m' \circ k$ is unique when it exists.
If $m \equiv m'$, the two factors are inverse isomorphisms, so $m \equiv m'$ holds exactly when $m = m' \circ k$ for an isomorphism $k$.
The relation $\le$ induces a partial order on the subobjects of $X$.

Example: in the category of sets, the monomorphisms are the injective functions.
An injective $m \colon A \to X$ is equivalent to the inclusion of its image $m(A) \subseteq X$, since $m$ is a bijection onto $m(A)$.
So the subobjects of $X$ correspond to the [[subsets|0BJR9QR08E]] of $X$.

Non-example: the map $\{a, b\} \to \{1\}$ that sends both points to $1$ does not represent a subobject of $\{1\}$, since it is not injective and hence not a monomorphism of sets.
