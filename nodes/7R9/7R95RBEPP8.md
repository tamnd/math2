---
tag: 7R95RBEPP8
kind: statement
role: theorem
name: Representation theorems for relation algebras
aliases: [representable-relation-algebras, non-finite-axiomatizability-of-rra]
msc: ["03G15", "03C05"]
topics: [QYA4H5Y7VR]
audience: research
about: [GQK4DSA11K]
uses: [RDSY11X6N2, GQK4DSA11K, BQ9EEFPS10, AJNZJD8442, AGYBSTD7BG, AX9Q86GB8M]
proofs: [95FB135Y91]
sources:
  - url: https://en.wikipedia.org/wiki/Relation_algebra
  - book: isbn:9780444509321
  - book: isbn:9780821810415
---

## Statement

Let $\mathsf{RA}$ be the class of [[relation algebras|RDSY11X6N2]].
A relation algebra is *representable* if it is isomorphic to a subalgebra of a direct product of [[full relation algebras|BQ9EEFPS10]] $\mathrm{Re}(U)$.
Let $\mathsf{RRA}$ be the class of representable relation algebras.

**Theorem.**

1. $\mathsf{RRA}$ is closed under subalgebras and direct products.
2. $\mathsf{RRA}$ is closed under homomorphic images, so it is a [[variety|AJNZJD8442]].
3. $\mathsf{RRA}$ is not axiomatizable by any finite set of first-order sentences.
4. In particular, $\mathsf{RRA} \ne \mathsf{RA}$.
5. There is no algorithm that decides whether a finite relation algebra is representable.

Part 2 is due to Tarski, part 3 to Monk and part 5 to Hirsch and Hodkinson.

## Remarks

### Why each hypothesis is needed

1. The word "finite" in part 3 matters: $\mathsf{RRA}$ is a variety, so it has an infinite equational basis.
2. Part 3 concerns arbitrary first-order sentences, not only equations; the result is stronger than the failure of a finite equational basis.
3. Part 5 is about finite algebras. The set of equations valid in $\mathsf{RRA}$ is recursively enumerable, since an equation holds in every $\mathrm{Re}(U)$ iff a corresponding first-order sentence is valid.

### Consequences

1. The axioms of [[the definition|RDSY11X6N2]] are finitely many equations, so part 3 gives part 4.
2. To prove an equation valid for all relations, the axioms of $\mathsf{RA}$ are not always enough.
3. By part 5, the set of finite representable relation algebras, given by their multiplication tables, is not recursive.

### Converse

Every representable relation algebra satisfies the axioms of $\mathsf{RA}$: this soundness is checked in remark 1 of [[the definition|RDSY11X6N2]].
The converse of soundness is exactly what part 4 denies.

### Generalizations

1. The analog for [[cylindric algebras|1MDT9BF81H]] holds in each finite dimension at least $3$; see [[this theorem|WZ1BZYVD5G]].
2. The same method of [[ultraproducts|AX9Q86GB8M]] of non-representable algebras applies to many classes of Boolean algebras with operators.
3. Every relation algebra embeds in a complete and atomic relation algebra, its canonical extension.

## History

Lyndon found the first non-representable relation algebras in 1950.
Tarski proved that $\mathsf{RRA}$ is a variety in 1955.
Monk proved in 1964 that $\mathsf{RRA}$ has no finite axiomatization.
Hirsch and Hodkinson proved the undecidability of representability for finite algebras, and they present it in their book "Relation algebras by games".

## Explanations

### L1 human

The axioms of relation algebra are true for every algebra of real relations.
This theorem says that the converse fails: some abstract relation algebras are not algebras of relations, and no finite list of extra axioms can fix this.

### L2 human

1. Start with an abstract relation algebra $A$, given by a multiplication table on its atoms.
2. A representation is a set $U$ and an assignment of a relation on $U$ to each atom, so that the table becomes true.
3. For some finite tables no such set exists, even though the table satisfies all axioms of $\mathsf{RA}$.
4. Part 5 says that no program can decide, given a finite table, whether a representation exists.

The typical use: part 3 explains why every finite axiom system for the calculus of relations is incomplete for relations.
The trap: part 3 does not say that $\mathsf{RRA}$ is not a variety; it is one, but it needs infinitely many equations.

### L3 human

A representation of a simple atomic algebra is a set of points with labeled edges such that each triangle is consistent with the composition table; games on such networks give the representability criteria of Hirsch and Hodkinson.
The finite-variable connection is close: an equation holds in $\mathsf{RRA}$ iff a corresponding three-variable sentence is valid, while by a result of Maddux the equations of $\mathsf{RA}$ correspond to the three-variable sentences with proofs that use four variables.
Monk's method is the same as for [[cylindric algebras|1MDT9BF81H]]: build non-representable algebras whose [[ultraproduct|AX9Q86GB8M]] is representable, and apply [[Łoś's theorem|AGYBSTD7BG]].
